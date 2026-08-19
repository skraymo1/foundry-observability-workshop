#!/usr/bin/env python3
"""
Foundry evaluation gate.

Runs a small evaluation set against a Microsoft Foundry model deployment,
scores it with AI-assisted (LLM-judge) and deterministic evaluators, compares
aggregate scores to thresholds, and exits non-zero when a gate is breached.

Design notes for the workshop:
  * Auth uses DefaultAzureCredential so the same script runs locally (az login)
    and in GitHub Actions (OIDC federated credential). No API keys.
  * Judge prompts are inline and explicit. Participants can read exactly what
    the "score" means -- that transparency is the point of the phase.
  * Row-level results are always written out. Aggregates decide whether to
    worry; rows decide what to fix.

Usage:
    python scripts/run_eval.py --config eval-config.yaml --output results
"""

from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import yaml
from azure.identity import DefaultAzureCredential
from openai import OpenAI
from dotenv import load_dotenv

COGNITIVE_SERVICES_SCOPE = "https://ai.azure.com/.default"
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

JUDGE_RUBRICS = {
    "groundedness": (
        "Score how well the RESPONSE is supported by the POLICY CONTEXT and the "
        "EXPECTED BEHAVIOR. A response that invents policy, dates, or approvals "
        "scores 1. A response that correctly states the policy is insufficient "
        "when it truly is scores 5."
    ),
    "relevance": (
        "Score how directly the RESPONSE addresses the QUERY. Off-topic or "
        "evasive answers score low. Asking a clarifying question for a genuinely "
        "ambiguous query is relevant and scores high."
    ),
    "coherence": (
        "Score the RESPONSE for internal consistency, clarity, and readability. "
        "Contradictions, rambling, or broken structure score low."
    ),
}

JUDGE_TEMPLATE = """You are a strict evaluation judge. Score a single response on one dimension.

DIMENSION: {dimension}
RUBRIC: {rubric}

QUERY:
{query}

EXPECTED BEHAVIOR:
{ground_truth}

RESPONSE:
{response}

Return ONLY a JSON object, no prose, in this exact shape:
{{"score": <integer 1-5>, "reason": "<one sentence>"}}
"""


# ---------------------------------------------------------------- infrastructure


def build_client(endpoint: str) -> OpenAI:
    """Foundry project endpoint + Entra token. Works locally and in CI."""
    access_token = DefaultAzureCredential().get_token(COGNITIVE_SERVICES_SCOPE).token
    base_url = endpoint.rstrip("/")
    if not base_url.endswith("/openai/v1"):
        base_url = f"{base_url}/openai/v1"
    return OpenAI(base_url=base_url, api_key=access_token)


def complete(client: OpenAI, deployment: str, messages: list[dict],
             *, max_completion_tokens: int = 512, temperature: float = 0.0) -> str:
    request = {
        "model": deployment,
        "messages": messages,
        "max_completion_tokens": max_completion_tokens,
    }
    if temperature != 0.0:
        request["temperature"] = temperature

    resp = client.chat.completions.create(
        **request,
    )
    return (resp.choices[0].message.content or "").strip()


# ------------------------------------------------------------------- evaluation


def judge(client: OpenAI, judge_deployment: str, dimension: str,
          row: dict, response: str) -> dict:
    prompt = JUDGE_TEMPLATE.format(
        dimension=dimension,
        rubric=JUDGE_RUBRICS.get(dimension, "Score from 1 (worst) to 5 (best)."),
        query=row.get("query", ""),
        ground_truth=row.get("ground_truth", ""),
        response=response,
    )
    raw = complete(
        client, judge_deployment,
        [{"role": "user", "content": prompt}],
        max_completion_tokens=200, temperature=0.0,
    )
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not match:
        # A judge that fails to answer is a failed measurement, not a pass.
        return {"score": 1, "reason": f"judge returned unparseable output: {raw[:120]}"}
    try:
        parsed = json.loads(match.group(0))
        score = int(parsed.get("score", 1))
        return {"score": max(1, min(5, score)), "reason": str(parsed.get("reason", ""))}
    except (ValueError, TypeError) as exc:
        return {"score": 1, "reason": f"judge parse error: {exc}"}


def check_refusal(response: str, markers: list[str]) -> dict:
    lowered = response.lower()
    hit = next((m for m in markers if m.lower() in lowered), None)
    return {
        "score": 1.0 if hit else 0.0,
        "reason": f"matched marker '{hit}'" if hit else "no refusal/escalation language found",
    }


def evaluate_row(client: OpenAI, cfg: dict, system_prompt: str,
                 target_deployment: str, judge_deployment: str, row: dict) -> dict:
    result = {"id": row.get("id"), "query": row.get("query"),
              "tags": row.get("tags", []), "metrics": {}}

    try:
        response = complete(
            client, target_deployment,
            [{"role": "system", "content": system_prompt},
             {"role": "user", "content": row["query"]}],
            max_completion_tokens=cfg["target"].get("max_tokens", 512),
            temperature=cfg["target"].get("temperature", 0.0),
        )
    except Exception as exc:  # noqa: BLE001 - surface any target failure as a row failure
        result["error"] = str(exc)
        result["response"] = ""
        return result

    result["response"] = response

    for evaluator in cfg.get("evaluators", []):
        name = evaluator["name"]
        result["metrics"][name] = judge(client, judge_deployment, name, row, response)

    for det in cfg.get("deterministic", []):
        tag = det.get("applies_to_tag")
        if tag and tag not in row.get("tags", []):
            continue
        result["metrics"][det["name"]] = check_refusal(response, det.get("refusal_markers", []))

    return result


# ------------------------------------------------------------------ aggregation


def aggregate(rows: list[dict], cfg: dict) -> tuple[list[dict], bool]:
    gates: list[dict] = []
    all_metrics = {e["name"]: e["threshold"] for e in cfg.get("evaluators", [])}
    all_metrics.update({d["name"]: d["threshold"] for d in cfg.get("deterministic", [])})

    passed_overall = True
    for metric, threshold in all_metrics.items():
        scores = [r["metrics"][metric]["score"] for r in rows if metric in r.get("metrics", {})]
        if not scores:
            continue
        mean = round(statistics.fmean(scores), 3)
        ok = mean >= threshold
        passed_overall = passed_overall and ok
        gates.append({
            "metric": metric,
            "mean": mean,
            "threshold": threshold,
            "rows": len(scores),
            "passed": ok,
            "worst_rows": sorted(
                [r["id"] for r in rows
                 if metric in r.get("metrics", {})
                 and r["metrics"][metric]["score"] < threshold]
            ),
        })

    if any("error" in r for r in rows):
        passed_overall = False

    return gates, passed_overall


def write_summary(path: Path, gates: list[dict], rows: list[dict], passed: bool) -> None:
    verdict = "PASSED" if passed else "FAILED"
    lines = [
        f"### Foundry evaluation gate: **{verdict}**",
        "",
        f"`{len(rows)}` rows · commit `{os.getenv('GIT_SHA', 'local')[:7]}` · "
        f"ref `{os.getenv('GIT_REF', 'local')}`",
        "",
        "| Metric | Mean | Threshold | Result | Failing rows |",
        "|---|---:|---:|:--:|---|",
    ]
    for g in gates:
        mark = "✅" if g["passed"] else "❌"
        failing = ", ".join(f"`{r}`" for r in g["worst_rows"]) or "—"
        lines.append(
            f"| {g['metric']} | {g['mean']} | {g['threshold']} | {mark} | {failing} |"
        )

    errored = [r for r in rows if "error" in r]
    if errored:
        lines += ["", "#### Rows that failed to execute", ""]
        lines += [f"- `{r['id']}` — {r['error'][:160]}" for r in errored]

    lines += [
        "",
        "> Aggregate scores decide whether to worry. Row-level results decide what to fix — "
        "download the `foundry-eval-results` artifact for per-row responses and judge reasons.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


# ------------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description="Foundry evaluation gate")
    parser.add_argument("--config", default="eval-config.yaml")
    parser.add_argument("--output", default="results")
    parser.add_argument("--no-fail", action="store_true",
                        help="Report results but always exit 0 (advisory mode)")
    args = parser.parse_args()

    root = Path(args.config).resolve().parent
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))

    endpoint = os.environ.get("FOUNDRY_PROJECT_ENDPOINT")
    if not endpoint:
        print("FOUNDRY_PROJECT_ENDPOINT is not set.", file=sys.stderr)
        return 2

    target_deployment = os.environ.get("MODEL_DEPLOYMENT_NAME") or cfg["target"]["deployment"]
    judge_deployment = os.environ.get("JUDGE_DEPLOYMENT_NAME") or cfg["judge"]["deployment"]

    system_prompt = (root / cfg["target"]["system_prompt_file"]).read_text(encoding="utf-8")
    dataset_path = root / cfg["dataset"]
    rows_in = [json.loads(line) for line in dataset_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    print(f"Endpoint : {endpoint}")
    print(f"Target   : {target_deployment}")
    print(f"Judge    : {judge_deployment}")
    print(f"Rows     : {len(rows_in)}")

    client = build_client(endpoint)

    with ThreadPoolExecutor(max_workers=cfg.get("parallel", 4)) as pool:
        rows = list(pool.map(
            lambda r: evaluate_row(client, cfg, system_prompt,
                                   target_deployment, judge_deployment, r),
            rows_in,
        ))

    gates, passed = aggregate(rows, cfg)

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    (out / "rows.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    (out / "gates.json").write_text(json.dumps({
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "commit": os.getenv("GIT_SHA", "local"),
        "target_deployment": target_deployment,
        "judge_deployment": judge_deployment,
        "passed": passed,
        "gates": gates,
    }, indent=2), encoding="utf-8")
    write_summary(out / "summary.md", gates, rows, passed)

    print()
    for g in gates:
        mark = "PASS" if g["passed"] else "FAIL"
        print(f"[{mark}] {g['metric']:<22} mean={g['mean']:<6} threshold={g['threshold']}")
    print(f"\nOverall: {'PASSED' if passed else 'FAILED'}  (results in {out}/)")

    if not passed and not args.no_fail:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
