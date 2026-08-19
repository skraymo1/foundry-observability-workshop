# Phase 14 sample — Foundry evaluations in GitHub Actions

Drop-in sample for the bonus CI/CD phase of the Foundry Governance and Observability workshop.

> **Use the NEW Microsoft Foundry portal** for project, deployment, and evaluation review.
> **Verify in the current Microsoft Foundry portal** before claiming a specific menu path in front of a customer.
> **Do not use Agent 365.** Nothing here depends on it.

## What this does

On every pull request and on pushes to `main`, the workflow:

1. Authenticates to Azure with **OIDC federated credentials** — no stored secrets.
2. Runs a small evaluation set against a Foundry model deployment using `azure-ai-evaluation`.
3. Compares aggregate scores against thresholds in `eval-config.yaml`.
4. Fails the build when a metric drops below its gate.
5. Uploads results as a build artifact and writes a summary table to the job summary.

The point of the phase is not the script. It is the argument: **an evaluation with a threshold is a release control; an evaluation without one is a report nobody reads.**

## Files

| File | Purpose |
|---|---|
| `.github/workflows/foundry-eval.yml` | The GitHub Actions workflow (copy to repo root `.github/workflows/`) |
| `scripts/run_eval.py` | Runs evaluators, aggregates scores, enforces thresholds |
| `eval-config.yaml` | Evaluators, dataset path, and pass/fail thresholds |
| `data/eval-dataset.jsonl` | Synthetic workshop evaluation set |
| `requirements.txt` | Python dependencies |

## Setup

### 1. Placeholders

| Placeholder | Example |
|---|---|
| `<SUBSCRIPTION_ID>` | `00000000-0000-0000-0000-000000000000` |
| `<RESOURCE_GROUP>` | `rg-foundry-workshop` |
| `<RESOURCE_NAME>` | `foundry-workshop-01` |
| `<FOUNDRY_PROJECT_ENDPOINT>` | `https://<RESOURCE_NAME>.services.ai.azure.com/api/projects/<PROJECT_NAME>` |
| `<MODEL_DEPLOYMENT_NAME>` | `gpt-4o-mini` |
| `<JUDGE_DEPLOYMENT_NAME>` | `gpt-4o` |

### 2. Entra app registration + federated credential

```bash
az ad app create --display-name "gh-foundry-eval"
az ad sp create --id <APP_ID>
```

Add a federated credential for the repository (Entra portal → App registration → Certificates & secrets → Federated credentials → GitHub Actions deploying Azure resources). For this repository, enter:

| Portal field | Value |
|---|---|
| Organization | `skraymo1` |
| Organization ID | `117292869` |
| Repository | `foundry-observability-workshop` |
| Repository ID | `1339577896` |
| Entity type | `Branch` |
| GitHub branch name | `main` |
| Credential name | `gh-main` |

The portal calls the owner an **Organization** even when the repository belongs to a personal GitHub account. The Organization ID and Repository ID are GitHub's immutable numeric IDs, not the names. The generated branch subject should be:

```text
repo:skraymo1@117292869/foundry-observability-workshop@1339577896:ref:refs/heads/main
```

When adapting this sample for another repository, retrieve the IDs with:

```bash
gh api users/<OWNER> --jq .id
gh api repos/<OWNER>/<REPO> --jq .id
```

Add a second credential for pull-request runs. Use the same organization and repository values, select `Pull request` as the entity type, and name it `gh-pull-request`. Its generated subject should be:

```text
repo:skraymo1@117292869/foundry-observability-workshop@1339577896:pull_request
```

### 3. Role assignment

The service principal needs data-plane access to the Foundry project:

```bash
az role assignment create \
  --assignee <APP_ID> \
  --role "Foundry User" \
  --scope /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>
```

> **Foundry User** was previously named **Azure AI User**. The role ID and core permissions did not change, but the old name might still appear while the rename rolls out. See [Role-based access control for Microsoft Foundry](https://learn.microsoft.com/azure/foundry/concepts/rbac-foundry). If evaluation calls return 403, check this assignment and its scope first.

### 4. Repository configuration

GitHub → Settings → Secrets and variables → Actions → **Variables**:

| Variable | Value |
|---|---|
| `AZURE_CLIENT_ID` | app registration client ID |
| `AZURE_TENANT_ID` | directory tenant ID |
| `AZURE_SUBSCRIPTION_ID` | `<SUBSCRIPTION_ID>` |
| `FOUNDRY_PROJECT_ENDPOINT` | `<FOUNDRY_PROJECT_ENDPOINT>` |
| `MODEL_DEPLOYMENT_NAME` | `<MODEL_DEPLOYMENT_NAME>` |
| `JUDGE_DEPLOYMENT_NAME` | `<JUDGE_DEPLOYMENT_NAME>` |

These are **variables**, not secrets — none of them are credentials. That is the OIDC selling point.

### 5. Branch protection

Settings → Branches → protect `main` → require the `foundry-eval` check. Until you do this, the gate is advisory only.

## Run it locally first

```powershell
cd ci-cd
python -m venv .venv; .venv\Scripts\Activate.ps1
pip install -r requirements.txt
az login

# Create ci-cd/.env (it is gitignored):
# FOUNDRY_PROJECT_ENDPOINT="https://<FOUNDRY_PROJECT_ENDPOINT>"
# MODEL_DEPLOYMENT_NAME="gpt-5.4-mini"
# JUDGE_DEPLOYMENT_NAME="gpt-5.5"

python scripts/run_eval.py --config eval-config.yaml --output results
```

The local runner loads `ci-cd/.env`. Environment variables already set in the
shell take precedence, and GitHub Actions continues to use the workflow's
repository variables.

Exit code `0` = gates passed. Exit code `1` = a threshold was breached.

## Deliberate failure

`eval-config.yaml` sets `groundedness` at `4.0`. The dataset includes the international-return-window row, which the synthetic policy deliberately does not cover. Raise the threshold to `4.5` in the demo to show a **red build**, then relax it to show green — the contrast is the whole lesson.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `AADSTS70021` / no matching federated credential | Subject string mismatch. Use the portal-generated ID-based subject and ensure it matches the branch or `pull_request` exactly. |
| `403` on evaluation calls | Role assignment missing or scoped to the wrong resource. See step 3. |
| `429` rate limits | Lower `parallel` in the config, or raise deployment TPM quota. |
| Judge model not found | `JUDGE_DEPLOYMENT_NAME` must be a deployment that exists in the same project. |
| Results empty | Check the dataset path in `eval-config.yaml` is repo-relative. |
| Evaluator import errors | Package APIs move. Pin versions in `requirements.txt` and re-verify against current Microsoft Learn docs. |

## Cleanup

```bash
az role assignment delete --assignee <APP_ID> --scope <SCOPE>
az ad app delete --id <APP_ID>
```

Then remove the repository variables and the workflow file.
