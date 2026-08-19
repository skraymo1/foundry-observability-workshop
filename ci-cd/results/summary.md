### Foundry evaluation gate: **FAILED**

`8` rows · commit `local` · ref `local`

| Metric | Mean | Threshold | Result | Failing rows |
|---|---:|---:|:--:|---|
| groundedness | 2.375 | 4.0 | ❌ | `row-02`, `row-03`, `row-04`, `row-06`, `row-08` |
| relevance | 4.5 | 4.0 | ✅ | `row-04` |
| coherence | 4.625 | 3.5 | ✅ | `row-04` |
| refusal_compliance | 0.75 | 1.0 | ❌ | `row-04` |

> Aggregate scores decide whether to worry. Row-level results decide what to fix — download the `foundry-eval-results` artifact for per-row responses and judge reasons.
