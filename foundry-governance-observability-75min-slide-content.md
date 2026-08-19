# Foundry Governance and Observability — 75-Minute Slide Content

**PowerPoint-ready slide content for the condensed session**

> **Deck standard:** Every portal screen in this deck is the **Microsoft Foundry portal** (`https://ai.azure.com`). Where a label or path can change, the slide carries a **Portal verification note**.
>
> **Scope standard:** Microsoft Foundry and Azure are the center of the story. Agent 365 is out of scope and is not required for any demo or lab step.

## Deck map

| # | Slide | Type | Approx. time |
|---:|---|---|---:|
| 1 | Title | Title | 1 min |
| 2 | Agenda — 75 minutes | Content | 2 min |
| 3 | Audience, prerequisites, and modes | Content | 2 min |
| 4 | Section — Governance | Divider | — |
| 5 | The operating questions | Content | 3 min |
| 6 | Microsoft Foundry positioning | Content | 4 min |
| 7 | Governance model: scope, identity, guardrails | Content | 5 min |
| 8 | Section — Observability | Divider | — |
| 9 | Observability signals that matter | Content | 4 min |
| 10 | Traces and telemetry | Content | 5 min |
| 11 | Evaluation and responsible AI | Content | 4 min |
| 12 | Reference architecture | Content | 4 min |
| 13 | Section — Hands-on lab | Divider | — |
| 14 | Lab modules and rules of engagement | Content | 3 min |
| 15 | Multi-model strategy and agent frameworks | Content | 4 min |
| 16 | Foundry observability and partner platforms | Content | 3 min |
| 17 | Takeaways and next steps | Closing | 5 min |
| A1 | Appendix — Preview capabilities to validate | Appendix | — |
| A2 | Appendix — Troubleshooting quick reference | Appendix | — |
| A3 | Appendix — Competitive positioning caveats | Appendix | — |

Slide-facing time is roughly 42 minutes with Slides 15 and 16 held for competitive audiences; the remaining time is the 30-minute lab plus transitions. If Slides 15 and 16 are delivered, trim the portal orientation and observability segments as described in the workshop agenda.

---

## Slide 1 — Foundry Governance and Observability

**Subtitle / key message:** From AI experimentation to a governed, observable operating model — in 75 minutes.

**Bullets**

- Govern access, deployments, and safety boundaries.
- Observe behavior with traces, telemetry, and evaluations.
- Turn evidence into release and operational decisions.
- Practice the workflow in the **Microsoft Foundry portal**.

**Speaker notes:** Open by setting expectations: this is an operational-readiness briefing with a short hands-on lab, not an AI hype session. State plainly that Agent 365 is out of scope and not required. Tell the room they will leave with a trace record, an evaluation read, and a next action.

**Suggested visual:** Dark full-bleed title slide with the evidence path **Govern → Run → Observe → Evaluate → Decide** as a horizontal chevron strip.

**Demo or lab tie-in:** Preview the lab: one prompt, one trace, one evaluation, one decision.

**Portal verification note:** Use a **Microsoft Foundry portal** landing screenshot captured within 48 hours of delivery.

---

## Slide 2 — Agenda: 75 minutes

**Subtitle / key message:** Short on theory, heavy on evidence.

**Bullets**

- 5 min — Welcome and framing
- 10 min — **Microsoft Foundry portal** orientation
- 25 min — Governance and observability foundations
- 30 min — Hands-on lab: run, trace, evaluate, decide
- 5 min — Wrap-up and next steps

**Speaker notes:** Emphasize the 30-minute lab block; that is where the value lands. Note that no formal break is scheduled — if delivering in person, offer a 5-minute break after the observability segment and trim the lab to 25 minutes. Confirm who is hands-on and who is review-only before the lab begins.

**Suggested visual:** Horizontal timeline with the 30-minute lab block visually dominant in the accent color.

**Demo or lab tie-in:** Point at the lab block and name the three modules.

**Portal verification note:** None.

---

## Slide 3 — Audience, prerequisites, and modes

**Subtitle / key message:** Everyone participates, even without full permissions.

**Bullets**

- Azure subscription access in a supported Microsoft Entra tenant.
- Ability to open the prepared Foundry project `<FOUNDRY_PROJECT>`.
- Access to `<MODEL_DEPLOYMENT>` or an approved instant-access model.
- Read access to `<APPLICATION_INSIGHTS>` where telemetry review is planned.
- No Agent 365 license, entitlement, or configuration is required.

**Speaker notes:** Offer two modes: hands-on and review-only. Reassure review-only participants they will still complete every worksheet using instructor-shared evidence. Never distribute shared credentials or API keys. Set the data rule now: synthetic data only, no secrets in prompts, traces, or screenshots.

**Suggested visual:** Two-column mode matrix — Hands-on versus Review-only — with permitted activities per row.

**Demo or lab tie-in:** Maps directly to Lab Module 1.

**Portal verification note:** Show how to confirm project access without publishing a fixed click path. **Verify in the current Microsoft Foundry portal.**

---

## Slide 4 — Section divider: Governance

**Subtitle / key message:** Who can do what, where, with which model, under which guardrails.

**Bullets**

- Scope: subscription, resource, project.
- Identity: Microsoft Entra ID and Azure RBAC.
- Guardrails: preventive safety configuration.
- Evidence: recorded decisions with named owners.

**Speaker notes:** Transition line: "Observability tells you what happened. Governance decides what should have been possible in the first place." Keep this slide to 20 seconds.

**Suggested visual:** Full-bleed dark divider with a single large numeral and the section name.

**Demo or lab tie-in:** Leads into the governance portion of the portal demo.

**Portal verification note:** None.

---

## Slide 5 — The operating questions

**Subtitle / key message:** Five questions every AI platform owner has to answer.

**Bullets**

- Who can build, deploy, invoke, and administer?
- Which model, version, and guardrail configuration served the request?
- What happened during the interaction, and where did time go?
- Did the result meet quality and safety criteria?
- What triggers rollback, escalation, or investigation?

**Speaker notes:** Use these five questions as the spine of the entire session. Tell participants that every artifact they produce in the lab answers one of them. Ask the room which question they currently cannot answer for a production or pilot workload — the answers make excellent discussion fuel for the wrap-up.

**Suggested visual:** Five question cards arranged around a central "production AI decision" hub.

**Demo or lab tie-in:** Participants answer all five with their own lab evidence.

**Portal verification note:** Note where **Microsoft Foundry portal** evidence contributes to each answer.

---

## Slide 6 — Microsoft Foundry positioning

**Subtitle / key message:** Models, projects, evaluations, and enterprise controls under an Azure-governed resource model.

**Bullets**

- Foundry resources provide top-level governance and shared configuration.
- Foundry projects isolate use cases, assets, and team activity.
- Microsoft Entra ID and Azure RBAC provide identity and access control.
- Connected Azure services keep their own governance boundaries.
- Agent capabilities are framed only within Microsoft Foundry and Azure.

**Speaker notes:** Position Foundry as an application and operations platform, not just a model catalog. The most important architectural point: a Foundry project is a governance boundary, not just a workspace. Reinforce that Agent 365 is out of scope — if agents come up, keep the conversation inside Microsoft Foundry and Azure.

**Suggested visual:** Layered diagram — subscription → resource group → Foundry resource → Foundry project → connected Azure services.

**Demo or lab tie-in:** Lab Module 1 asks participants to record the parent resource and connected resources.

**Portal verification note:** Label the screen explicitly as the **Microsoft Foundry portal**. **Verify in the current Microsoft Foundry portal.**

---

## Slide 7 — Governance model: scope, identity, and guardrails

**Subtitle / key message:** Apply each control at the scope where it can actually be enforced.

**Bullets**

- Subscription and resource group: policy, cost, region, ownership.
- Foundry resource: shared deployments, connections, and governance.
- Foundry project: team access and use-case isolation.
- Guardrails and content controls: preventive safety behavior.
- Every control needs an owner and an evidence source.

**Speaker notes:** Governance fails in two predictable ways: a control with no owner, and a metric with no decision rule. Call out the most common surprise — Foundry project access does not automatically grant Application Insights or Log Analytics access. Note that Foundry RBAC roles were renamed, so older role names may still appear during rollout; treat display names as a verification item, not a fixed fact.

**Suggested visual:** Scope pyramid with two columns beside it: Control and Owner.

**Demo or lab tie-in:** Lab Module 1 — participants map one control they own to its evidence source.

**Portal verification note:** Use current administration and compliance views. **Verify in the current Microsoft Foundry portal.**

---

## Slide 8 — Section divider: Observability

**Subtitle / key message:** Evidence, not assumptions.

**Bullets**

- Traces explain execution.
- Telemetry explains operations.
- Evaluations explain quality and safety.
- Correlation ties the three together.

**Speaker notes:** Transition line: "A 200 response does not prove the answer was grounded, safe, or useful." Keep this slide to 20 seconds.

**Suggested visual:** Full-bleed dark divider matching Slide 4's motif.

**Demo or lab tie-in:** Leads into the trace portion of the portal demo.

**Portal verification note:** None.

---

## Slide 9 — Observability signals that matter

**Subtitle / key message:** No single view proves an AI application is working.

**Bullets**

- Traces: sequence, timing, status, tools, and model calls.
- Telemetry: volume, latency, errors, and token consumption.
- Evaluations: quality, groundedness, and safety outcomes.
- Correlation: trace ID, deployment, and evaluation run.
- Start in the **Microsoft Foundry portal**; use Azure Monitor as support.

**Speaker notes:** The central point: three independent evidence streams converge on one decision. Ask participants to name one signal they currently do not have. Common answers — no correlation between a user complaint and a specific trace, or no repeatable quality measure — set up the lab perfectly.

**Suggested visual:** Three evidence streams converging on a single decision gate.

**Demo or lab tie-in:** The lab collects one item from each stream.

**Portal verification note:** Show the current observability entry points. **Verify in the current Microsoft Foundry portal.**

---

## Slide 10 — Traces and telemetry

**Subtitle / key message:** The fastest path from a symptom to a reproducible case.

**Bullets**

- Inspect spans for prompts, model calls, retrieval, and tools.
- Record duration, status, errors, and correlation identifiers.
- Protect trace content with access, retention, and redaction controls.
- Treat availability, retention, and preview scope as validation items.
- Trace Replay and the Agent Monitoring Dashboard are preview capabilities.

**Speaker notes:** Two messages carry this slide. First, tracing turns a vague complaint into a specific, reproducible case. Second, trace data can include prompt content, outputs, and tool arguments — treat it as sensitive by default and apply access and retention controls accordingly. Mention Trace Replay and the Agent Monitoring Dashboard as preview capabilities with prepared evidence; do not build live time around them.

**Suggested visual:** Waterfall trace with labeled spans and one visibly slow span highlighted in the accent color.

**Demo or lab tie-in:** Lab Module 2 — record trace ID, duration, slowest span, and any sensitive content observed.

**Portal verification note:** Use the current tracing experience. **Verify in the current Microsoft Foundry portal.**

---

## Slide 11 — Evaluation and responsible AI

**Subtitle / key message:** Turn subjective expectations into repeatable evidence.

**Bullets**

- Select a target: model, Foundry agent, dataset, or eligible traces.
- Test normal, edge, and adversarial scenarios.
- Version prompts, models, datasets, evaluators, and thresholds.
- Pair AI-assisted evaluators with human review.
- Evaluator availability varies by target, scope, and region.

**Speaker notes:** Be explicit: AI-assisted evaluators are useful but not objective truth. Reference the current risk and safety evaluations transparency note for intended use, limitations, and human-review expectations. Note that trace evaluation, conversation-level evaluation, synthetic-data evaluation, and recurring evaluations are preview or scope-dependent — mention them, but do not run them live in a 75-minute session.

**Suggested visual:** Pipeline — **Dataset → Target → Evaluators → Results → Release gate**.

**Demo or lab tie-in:** Lab Module 3 — review `<EVALUATION_NAME>` and record a Pass, Conditional pass, or Fail decision.

**Portal verification note:** Select **Build** > **Evaluations** (under **Optimize**), or use the target model or agent's **Evaluation** tab > **Create**. Target and evaluator availability varies; **verify in the current Microsoft Foundry portal.**

---

## Slide 12 — Reference architecture

**Subtitle / key message:** One governed path from request to release decision.

**Bullets**

- Client request enters through an application or the portal playground.
- `<FOUNDRY_PROJECT>` applies identity, guardrails, and deployment policy.
- `<MODEL_DEPLOYMENT>` serves the request within approved region and quota.
- Traces and telemetry flow to `<APPLICATION_INSIGHTS>` and Log Analytics.
- Evaluations produce the evidence that gates the release.

**Speaker notes:** Walk the diagram left to right once, then walk it right to left as an investigation path: a complaint leads to a trace, the trace leads to a deployment and configuration, and the evaluation determines whether behavior is acceptable. Call out the two governance boundaries on the diagram — the Foundry project boundary and the monitoring-resource boundary — because they are governed separately.

**Suggested visual:** Left-to-right architecture flow with two dashed governance boundaries and a return arrow labeled "investigation path."

**Demo or lab tie-in:** All three lab modules map to a labeled stage on this diagram.

**Portal verification note:** Confirm current connected-resource behavior. **Verify in the current Microsoft Foundry portal.**

---

## Slide 13 — Section divider: Hands-on lab

**Subtitle / key message:** 30 minutes. Three modules. One decision.

**Bullets**

- Module 1 — Access, project context, and governance review.
- Module 2 — Run a prompt and inspect the trace.
- Module 3 — Review an evaluation and make a readiness call.
- Synthetic data only. Agent 365 is not required.

**Speaker notes:** Transition line: "You will not build a platform in 30 minutes. You will produce the evidence a platform owner needs." Confirm hands-on versus review-only participants before releasing the room.

**Suggested visual:** Full-bleed dark divider with three numbered module chips.

**Demo or lab tie-in:** This slide stays on screen during the lab.

**Portal verification note:** None.

---

## Slide 14 — Lab modules and rules of engagement

**Subtitle / key message:** Every module produces one recorded artifact.

**Bullets**

- Module 1 (10 min) — record project context and one owned control.
- Module 2 (12 min) — record two responses and one trace record.
- Module 3 (8 min) — record a readiness decision with justification.
- Use the **Microsoft Foundry portal** as the central experience.
- No secrets, no real customer data, no Agent 365 dependencies.

**Speaker notes:** Set the fallback expectations up front: traces can take a few minutes to appear, and prepared traces and a prepared evaluation are available for anyone blocked. Tell participants that if they hit an authorization error, that is a finding worth recording — not a failure. Emphasize that the goal is a written decision, not a completed checklist.

**Suggested visual:** Three module cards with duration, activity, and "artifact produced" on each.

**Demo or lab tie-in:** This is the lab briefing slide.

**Portal verification note:** Instructions are outcome-based. **Verify in the current Microsoft Foundry portal** for any changed label or path.

---

## Slide 15 — Multi-model strategy and agent frameworks

**Subtitle / key message:** Govern once, change models freely.

**Bullets**

- **All current Claude models are available in the Microsoft Foundry catalog** — Azure-native endpoint, Entra ID auth, Azure Marketplace billing.
- Each deployment picks a **hosting option**: Hosted on Azure (data stays in Azure, US Data Zone Standard) or Hosted on Anthropic.
- Azure-hosted deployments trade some provider features — server-side tools, MCP connector, Agent Skills, structured outputs.
- Microsoft Agent Framework is the build-time layer; Foundry Agent Service is the governed run time.
- **Agent SDK pattern:** Claude Agent SDK runs the agent loop in the customer's Python or TypeScript application; `CLAUDE_CODE_USE_FOUNDRY=1` routes its Claude calls through Foundry.
- Agent 365 is out of scope and not required for anything discussed here.

**Speaker notes:** Lead with availability, then the design choice. Every current Claude model is in the Foundry catalog — verified against the portal, the live catalog API, and Anthropic's own Foundry documentation. Do not underclaim here; a customer arriving from the Claude Platform docs often assumes Azure has nothing, and that assumption is wrong. The real design decision is the hosting option, selected per deployment and surfaced as a model version: Hosted on Azure keeps prompts and completions inside Azure and supports US Data Zone Standard but blocks certain provider features by design; Hosted on Anthropic runs on Anthropic infrastructure with the full feature set. Both go through the same Foundry endpoint, RBAC, and Azure bill, and a customer can run both in the same resource. Do not claim blanket feature parity and do not speculate on roadmap. A useful clarification: `code.claude.com/docs/en/microsoft-foundry` documents **Claude Code / Agent SDK access through Microsoft Foundry**. The Claude Agent SDK is a real provider agent library: it supplies the agent loop, tools, permissions, sessions, hooks, and MCP support in a Python or TypeScript application. For Foundry, set `CLAUDE_CODE_USE_FOUNDRY=1`, configure the resource plus Azure credentials, and pin actual deployment names. The customer application owns tool orchestration; Foundry provides the model endpoint and Azure control boundary. Do not promise that an external Agent SDK application automatically appears in **Build > Agents > Traces** — that is a Foundry-agent surface. Instrument the host application with OpenTelemetry when end-to-end Azure observability is required. Compare like for like: Microsoft Agent Framework and the Claude Agent SDK sit at the build-time orchestration layer; Foundry Agent Service is the governed managed runtime.

**Suggested visual:** Two-layer diagram — build time (Microsoft Agent Framework beside a provider agent SDK) above run time (Foundry Agent Service spanning the full width) with a shared governance band underneath. Optional inset: the Hosted on Azure vs Hosted on Anthropic comparison.

**Demo or lab tie-in:** Search the model catalog for "Claude" live to show the full list, then point back to the Module 1 project context: the governance boundary did not change with the model.

**Portal verification note:** Catalog contents, hosting options, versions, deployment types, and regions change frequently. **Verify in the current Microsoft Foundry portal** and in current Anthropic Foundry documentation before making any parity claim.

---

## Slide 16 — Foundry observability and partner platforms

**Subtitle / key message:** OpenTelemetry means coexistence, not a replacement decision.

**Bullets**

- Foundry tracing follows OpenTelemetry semantic conventions, so spans are portable.
- Default destination is the connected `<APPLICATION_INSIGHTS>` resource.
- An additional exporter or span processor can send the same spans to a partner platform such as Arize.
- Foundry-native fits the governed release gate; partner platforms fit cross-application AI observability.
- Duplicated trace data needs the same access, retention, and redaction controls.

**Speaker notes:** If the customer already runs Arize, do not position this as a rip-and-replace. The honest answer is that most enterprises end up with both: Foundry-native evaluation and safety evaluators for the release gate, and a partner platform for cross-application analysis and a shared data-science workflow. Note that Arize is available as an Azure Native ISV integration, so procurement can stay in Azure. Close with the governance warning — exporting spans duplicates potentially sensitive prompt and response content, so the second destination needs the same controls and a named owner. That is a governance decision, not just a tooling decision.

**Suggested visual:** Single OpenTelemetry stream branching to two destinations — Application Insights and a partner platform — with one shared governance boundary drawn around both.

**Demo or lab tie-in:** Reuse the Module 2 trace and ask where else that content would land under the customer's current architecture.

**Portal verification note:** Confirm current tracing export behavior and partner integration mechanics. **Verify in the current Microsoft Foundry portal** and against current partner documentation.

---

## Slide 17 — Takeaways and next steps

**Subtitle / key message:** Govern the system, observe the behavior, evaluate the outcome, decide with evidence.

**Bullets**

- Standardize on the **Microsoft Foundry portal** for these workflows.
- Separate project access from monitoring access explicitly.
- Require trace plus evaluation evidence before a release decision.
- Pilot on one use case, then scale the reusable controls.
- Recommended follow-ups: name owners, set thresholds, schedule a readiness review.

**Speaker notes:** Close with three concrete actions: pick one pilot use case, name an owner for each governance control, and schedule a readiness review within 30 days. Ask each participant to state one gap they found today and who will own it. Reiterate that Agent 365 is out of scope and was not required for anything in this session.

**Suggested visual:** Three-step roadmap — **Pilot → Prove → Scale** — with follow-up actions listed under each step.

**Demo or lab tie-in:** Participants leave with a trace record, an evaluation read, and a named next action.

**Portal verification note:** End on a current **Microsoft Foundry portal** view showing project context and evidence.

---

## Appendix A1 — Preview capabilities to validate

**Subtitle / key message:** Mention them, prepare evidence, never depend on them live.

**Bullets**

- Trace Replay — step through agent interactions; requires trace data and monitoring access.
- Agent Monitoring Dashboard — per-agent monitoring with recurring evaluations and alerts.
- Trace evaluation and trace-to-dataset conversion — evaluate real interactions.
- Cloud AI red teaming — automated adversarial scanning, limited regional availability.
- All of the above are preview and subject to change.

**Speaker notes:** Use this slide only if the audience asks about roadmap or advanced observability. Preview capabilities change quickly in permissions, limits, and regional availability. Validate each one against current Microsoft Learn documentation before delivery, and demonstrate with prepared screenshots rather than live navigation.

**Suggested visual:** Five capability chips with a preview badge on each.

**Demo or lab tie-in:** None. These are not lab requirements.

**Portal verification note:** **Verify in the current Microsoft Foundry portal** and confirm preview status before every delivery.

---

## Appendix A2 — Troubleshooting quick reference

**Subtitle / key message:** Keep the room moving.

**Bullets**

- Project not visible → confirm account, tenant, and membership; switch to review-only.
- No trace appears → ingestion delay; wait, refresh, then use a prepared trace.
- Authorization error on telemetry → monitoring access is separate; record it as a finding.
- Model unavailable → use `<MODEL_DEPLOYMENT>` or the instructor-approved fallback.
- Evaluation not visible → use the instructor's shared result view.

**Speaker notes:** Do not troubleshoot individual RBAC issues in front of the room. Move blocked participants to review-only mode immediately and continue. Every blocker on this slide has a prepared fallback, so no participant should be idle.

**Suggested visual:** Two-column issue-and-fix table with a muted background.

**Demo or lab tie-in:** Supports all three lab modules.

**Portal verification note:** None.

---

## Appendix A3 — Competitive positioning caveats

**Subtitle / key message:** Say what is true, and say what you must verify.

**Bullets**

- All current Claude models are available in the Foundry catalog — do not underclaim; verify hosting options and regions.
- Hosting option is the real design choice: Hosted on Azure keeps data in Azure; Hosted on Anthropic has the full feature set.
- Azure-hosted deployments block server-side tools, MCP connector, Agent Skills, structured outputs, and the Files API.
- Microsoft Agent Framework compares to a provider agent SDK, not to the whole Foundry platform.
- Partner observability is coexistence via OpenTelemetry, not a replacement argument.

**Speaker notes:** Use this as a presenter guardrail rather than a customer-facing slide. Overstating parity loses a technical audience — but so does underclaiming, and underclaiming is the more common error here. Every current Claude model is genuinely in Foundry; the honest nuance is the per-deployment hosting option and the documented Azure-hosted feature gap. Other verified specifics worth having ready: hosting option appears as a model version in the deployment pane, models expose the Anthropic Messages API surface, Claude Consumption Unit billing runs through Azure Marketplace, Foundry SDK support covers C#, Java, PHP, Python, and TypeScript but not Go or Ruby, Foundry does not return Anthropic rate-limit headers, and Anthropic acts as an independent processor for Microsoft under its own data use terms. Claude Mythos Preview is invitation-only and should stay out of customer material. Where you are unsure, say "let me confirm the current state" rather than guessing.

**Suggested visual:** Two-column "Say this / Verify this" table in muted tones.

**Demo or lab tie-in:** None. Presenter reference only.

**Portal verification note:** **Verify in the current Microsoft Foundry portal** before every delivery.

---

## Presenter checklist

- [ ] Every portal screenshot is from the **Microsoft Foundry portal**, captured within 48 hours.
- [ ] No legacy portal name, product name, or navigation path appears as a workflow.
- [ ] Agent 365 appears only as out-of-scope or not-required.
- [ ] Governance and observability each have dedicated slides and lab evidence.
- [ ] Preview capabilities are labeled and supported by prepared evidence.
- [ ] `<FOUNDRY_PROJECT>`, `<MODEL_DEPLOYMENT>`, `<APPLICATION_INSIGHTS>`, and `<EVALUATION_NAME>` are preprovisioned and tested.
- [ ] At least two recent traces exist, including one slow or failed span.
- [ ] The prepared evaluation contains at least one failing row.
- [ ] Slide-facing time plus the 30-minute lab fits inside 75 minutes.
- [ ] Synthetic data only; no secrets or real customer data.
- [ ] If Slides 15–16 are used, model catalog availability and framework GA status re-verified today.
- [ ] No feature-parity claim is made that has not been verified.
