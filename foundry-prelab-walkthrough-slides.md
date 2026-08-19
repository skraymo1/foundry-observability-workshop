# Foundry Governance and Observability — Pre-Walkthrough Slides

**Purpose:** A short deck to run **before** you open the portal. It frames the vocabulary, the phase order, and what the audience should watch for — so the walkthrough itself is narration rather than explanation.

**Companion document:** `foundry-lab-dryrun-guide.md` (Phases 0–12). Every slide here maps to a phase there.

> **Delivery mode:** instructor-led walkthrough. Participants do **not** provision resources or click along. Say this on Slide 3 and mean it.
>
> **Deck standard:** Every portal screen is the **Microsoft Foundry portal** (`https://ai.azure.com`), with the **New Foundry** toggle on.
>
> **Scope standard:** Microsoft Foundry and Azure only. **Agent 365 is out of scope** and is not required for any step.

---

## Deck map

| # | Slide | Maps to | Time |
|---:|---|---|---:|
| 1 | Title | — | 1 min |
| 2 | What this session is (and isn't) | Delivery mode | 2 min |
| 3 | Audience, prerequisites, rules of engagement | Phase 0 | 2 min |
| 4 | The operating questions | Framing | 3 min |
| 5 | The evidence path | Framing | 2 min |
| 6 | Microsoft Foundry positioning | Framing | 3 min |
| 7 | Portal orientation — the map | Phases 1–2 | 4 min |
| 8 | Vocabulary you need before we start | Phases 8–9 | 4 min |
| 9 | Governance surfaces | Phases 3–4 | 3 min |
| 10 | Observability surfaces | Phases 6–7 | 3 min |
| 11 | Guardrails vs. guardrail policies | Phases 8–9 | 4 min |
| 12 | Evaluation: what it is and isn't | Phase 10 | 4 min |
| 13 | Foundry vs. dedicated observability platforms | Phase 11 | 3 min |
| 14 | Reference architecture | All | 3 min |
| 15 | Walkthrough roadmap — what you'll see | All | 3 min |
| 16 | How to participate | — | 2 min |
| 17 | Takeaways and next steps | Phase 12 | 3 min |
| 18 | Bonus: red teaming and adversarial testing | Phase 13 | 3 min |
| A1 | Appendix — Preview capabilities | — | — |
| A2 | Appendix — Portal verification checklist | — | — |
| A3 | Appendix — Out of scope | — | — |

**Slide-facing time:** ~48 minutes. Compress to ~20 by delivering Slides 1, 2, 4, 8, 11, 15 only — that is the minimum set that makes the walkthrough land.

---

## Slide 1 — Foundry Governance and Observability

**Main message:** Moving from AI experimentation to a governed, observable operating model.

**Bullets**

- Govern access, deployments, and safety boundaries.
- Observe behavior with traces, telemetry, and evaluations.
- Enforce minimum controls across a fleet, not one project at a time.
- Turn evidence into release and operational decisions.

**Speaker notes:** Set expectations in the first thirty seconds. This is an operational-readiness walkthrough, not an AI capability pitch. You will drive the portal; they will watch and argue with you. State plainly that Agent 365 is out of scope. Tell them the one thing you want them to leave with: *they can explain what these controls do, when they fire, and what they would tell a customer.*

**Suggested visual:** Dark full-bleed title with the evidence path as a horizontal chevron strip: **Govern → Run → Observe → Evaluate → Enforce → Decide**.

**Walkthrough tie-in:** Preview the arc — one prompt, one trace, one guardrail, one policy, one evaluation, one decision.

> **Show the NEW Microsoft Foundry portal:** use a landing screenshot captured within 48 hours of delivery.

---

## Slide 2 — What this session is (and isn't)

**Main message:** This is a demonstration, not a hands-on lab. That is a deliberate choice.

**Bullets**

- **Is:** a guided tour of real governance and observability surfaces, driven live.
- **Isn't:** a click-along lab — no per-person environment, no access requests, no quota to split.
- **Success:** you can explain the controls, not that you completed the steps.
- A true hands-on version exists if you want it later.

**Speaker notes:** Get this out of the way early or people will spend the first fifteen minutes waiting for credentials. Explain the trade: by not spending time on provisioning, you cover guardrail creation, policy enforcement, and evaluation depth that a hands-on lab has no time for. Invite interruption explicitly — a walkthrough with no questions has failed.

**Suggested visual:** Two-column contrast card — "Walkthrough" vs. "Hands-on lab" — with the walkthrough column highlighted.

**Walkthrough tie-in:** Note which phases are **[DEMO]** (you create something live) vs. **[TOUR]** (read-only navigation).

---

## Slide 3 — Audience, prerequisites, and rules of engagement

**Main message:** Everything you need is on screen. Here is what governs what you see.

**Bullets**

- Audience: technical sellers, solution engineers, cloud architects, AI platform owners.
- No participant Azure access required for this session.
- All data on screen is **synthetic** — no customer data, no production identifiers.
- Roles matter: creating a **guardrail** and creating a **guardrail policy** need different rights.

**Speaker notes:** The synthetic-data statement is not boilerplate — say it out loud so nobody screenshots something they shouldn't. On roles: mention that you personally hold both **Foundry Account Owner** (for guardrails) and **Owner** or **Resource Policy Contributor** (for policies), and that this split is itself a governance teaching point you will return to in Phase 9.

**Suggested visual:** Simple role table — action, role required, scope.

| Action | Role required | Scope |
|---|---|---|
| Create/edit a **guardrail** | Foundry Account Owner or higher | Azure AI resource |
| Create/edit a **guardrail policy** | Owner or Resource Policy Contributor | Subscription / resource group |
| View compliance status | Project access only | Project |

**Walkthrough tie-in:** Phase 0 preflight.

---

## Slide 4 — The operating questions

**Main message:** Governance and observability exist to answer questions someone will eventually ask you under pressure.

**Bullets**

- *Who can deploy a model, and what stops them deploying an ungoverned one?*
- *What did the system actually do on request `X` at 02:14?*
- *Is it getting better or worse, and how would we know?*
- *When it produces something harmful, what stopped it — and what recorded it?*

**Speaker notes:** This is the slide that earns you the room. Frame every subsequent surface as an answer to one of these four questions, not as a feature. Ask the audience which of the four they cannot currently answer for their own AI workloads — the honest answer is usually two or three of them, and that discomfort is the motivation for the rest of the session.

**Suggested visual:** Four question cards, each tagged with the Foundry surface that answers it.

**Walkthrough tie-in:** Return to this slide at the end of Phase 7 and Phase 10 to check the questions off.

---

## Slide 5 — The evidence path

**Main message:** Governance is not a document. It is a chain of evidence you can produce on demand.

**Bullets**

- **Govern** — scope, identity, deployment boundaries.
- **Run** — the workload actually executes.
- **Observe** — traces, logs, metrics record what happened.
- **Evaluate** — scored judgment about whether it was good enough.
- **Enforce** — guardrails block at runtime; policy mandates across the fleet.
- **Decide** — ship, hold, or remediate, with the evidence attached.

**Speaker notes:** Emphasize that the loop has to close. Most organizations do the first two steps and then substitute a spreadsheet for the rest. The distinguishing feature of a mature AI practice is that the decision at the end cites the evidence from the middle.

**Suggested visual:** Circular loop diagram, with **Enforce** feeding back into **Govern**.

**Walkthrough tie-in:** The phase order of the walkthrough deliberately follows this loop.

---

## Slide 6 — Microsoft Foundry positioning

**Main message:** Foundry is the governed runtime and control plane for AI workloads on Azure.

**Bullets**

- One place to deploy models, attach controls, and observe behavior.
- Identity is **Entra ID**; access is **Azure RBAC** — not a separate directory.
- Telemetry lands in **Application Insights / Log Analytics** — the same tooling as the rest of your estate.
- Enforcement runs through **Azure Policy** — the same mechanism as tagging and networking.

**Speaker notes:** The line to land: *Foundry does not ask you to adopt a new governance model. It extends the one you already run.* This is the argument that matters most to platform teams, and it is the foundation of the Phase 11 competitive contrast. Avoid a feature-list read — three sentences and move on.

**Suggested visual:** Layered diagram — Azure platform (identity, policy, monitor) at the base, Foundry control plane above it, models and agents on top.

**Walkthrough tie-in:** Everything after this is proof of this claim.

> **Show the NEW Microsoft Foundry portal:** the top navigation itself is the evidence — Build, Operate, Manage as distinct planes.

---

## Slide 7 — Portal orientation: the map

**Main message:** Learn this map now so navigation during the walkthrough is not a distraction.

**Bullets**

- **Top nav:** Home · Discover · **Build** · **Operate** · **Manage** · Docs. Project selector upper-left.
- **Build > Create:** Agents, Deployments, Services, Tools, Knowledge, **Guardrails**, Memory, Data.
- **Build > Optimize:** **Evaluations**, Fine-tune.
- **Operate > Compliance:** Policies, Assets, Guardrails, Security posture, Data security and governance.
- **Manage > Project details:** Users, Connected resources.

**Speaker notes:** Two corrections worth stating explicitly because they trip up anyone coming from the classic experience. First: **there is no "Models" node in the left pane** — model deployments live under **Build > Deployments**, and that page carries a **Models** *(preview)* tab. Second: the playground is reached from **Build > Deployments > select deployment > Open in playground**, not from a standalone playground node.

**Suggested visual:** Annotated portal screenshot with the three planes color-coded — Build (create), Operate (govern), Manage (administer).

**Walkthrough tie-in:** Phases 1–2.

> **Show the NEW Microsoft Foundry portal.** Confirm the **New Foundry** toggle is on before you share your screen.
>
> **Verify current portal navigation** — labels move. If a path differs on the day, say so out loud rather than clicking silently until you find it.

---

## Slide 8 — Vocabulary you need before we start

**Main message:** Four terms, precisely defined. Getting these wrong makes the rest incoherent.

**Bullets**

- **Guardrail** — a control set attached to specific models or agents. Blocks or annotates at runtime.
- **Guardrail policy** — an Azure Policy object that defines and assesses minimum controls across a subscription or resource group; it does **not** automatically assign a guardrail.
- **Trace** — the recorded execution of a single request, span by span.
- **Evaluation** — a scored judgment about output quality or safety, run against a dataset or against traces.

**Speaker notes:** Spend real time here — this is the highest-leverage slide in the pre-deck. The guardrail vs. guardrail policy distinction is the one that separates a governance-literate presenter from a feature-tour presenter. Say it as: *a guardrail is the lock on the door; a policy is the building code that says every door must have one — it does not install the lock for you.* Also draw the line between trace and evaluation: **a trace tells you what happened; an evaluation tells you whether it was good.**

**Suggested visual:** Four-quadrant definition card, with guardrail and guardrail policy visually paired.

**Walkthrough tie-in:** Phases 8, 9, 6, and 10 respectively.

---

## Slide 9 — Governance surfaces

**Main message:** Governance in Foundry is scope, identity, deployment control, and compliance visibility.

**Bullets**

- **Project boundary** — organizes the workload; the parent Azure resource carries shared quota and blast radius.
- **Manage > Project details > Users** — project access is governed separately from connected Azure resources.
- **Build > Deployments** — what is deployed, on what hosting, with which controls attached.
- **Operate > Compliance** — policy compliance, asset status, guardrail coverage, security posture.

**Speaker notes:** The point that lands with architects: connected Azure services have **independent RBAC, network, retention, and cost settings**. A project is not a security boundary by itself. Also set expectations for what you are about to show — a freshly created project shows empty or not-evaluated compliance states, and that is correct, not broken.

**Suggested visual:** Nested scope diagram — subscription → resource group → Foundry resource → project → deployment.

**Walkthrough tie-in:** Phases 3–4.

> **Show the NEW Microsoft Foundry portal** for both **Manage > Project details** and **Operate > Compliance**.

---

## Slide 10 — Observability surfaces

**Main message:** Observability is evidence about a specific execution, plus aggregate operational signal.

**Bullets**

- **Traces** — per-request execution detail, reached from **Build > Agents > `<AGENT>` > Traces**.
- **Trace Replay** *(preview)* — step through an interaction after the fact.
- **Monitor** *(preview)* — aggregate operational signals across runs.
- Telemetry lands in **Application Insights / Log Analytics** and is queryable with KQL.

**Speaker notes:** Warn the room about **ingestion delay** before you demo it — traces do not appear instantly, and a presenter refreshing a blank page looks broken. Reinforce the boundary argument: this data stays in your subscription, under your RBAC and your retention policy. That fact returns in Phase 11 as one of the strongest Foundry claims.

**Suggested visual:** Trace waterfall screenshot with spans annotated — model call, tool call, latency, token counts.

**Walkthrough tie-in:** Phases 6–7.

> **Show the NEW Microsoft Foundry portal.** Preview features may be unavailable — have fallback screenshots ready.

---

## Slide 11 — Guardrails vs. guardrail policies

**Main message:** One protects a workload. The other protects you from workloads you have not seen yet.

**Bullets**

- **Guardrail** — built in **Build > Guardrails** via a 3-step wizard: Add Controls → Assign → Review.
- The current **Add controls** screen is a grouped table: select a control row, then review its available intervention point and behavior, such as **Block**.
- **Guardrail policy** — built in **Operate > Compliance > Policies**, backed by **Azure Policy**, scoped to a subscription or resource group; it assesses the minimum posture but does not auto-assign a guardrail.
- Policy shows non-compliant assets and offers **Fix now** — but can take up to **30 minutes** to scan.

**Speaker notes:** This is the pair of demos that has no clean equivalent in an analysis-only observability tool, so flag it as a highlight before you show it. In the current New Foundry portal, the **Add controls** step uses grouped rows — Jailbreak, Indirect prompt injections, Content harms, Protected materials, and Blocklists — rather than the older risk-picker and **Add control** interaction. Two operational cautions worth pre-announcing: **Try in Playground only appears once a guardrail is assigned** to a model or agent, and the default risk controls (violence, hate, sexual, self-harm) **cannot be deleted** — only overridden. Both surprise presenters live.

**Suggested visual:** Side-by-side comparison table — object, where built, scope, what it does, who can create it.

**Walkthrough tie-in:** Phases 8–9. Tell them you will create both live.

> **Show the NEW Microsoft Foundry portal** for both surfaces. Compliance tabs are NEW-portal only.

---

## Slide 12 — Evaluation: what it is and isn't

**Main message:** Evaluation is a measurement instrument. Instruments have error rates.

**Bullets**

- **AI-assisted (LLM-judge)** — relevance, coherence, groundedness, task adherence. Flexible, subjective, costs a model call per row per evaluator.
- **Safety evaluators** — backed by Foundry safety services rather than your judge model.
- **Deterministic / NLP** — exact match, F1, similarity. Cheap and reproducible, but needs ground truth.
- **Aggregate scores tell you whether to worry. Row-level results tell you what to fix.**

**Speaker notes:** Do not overclaim here — an audience that catches you presenting LLM-judge scores as objective truth will discount everything else you said. The strongest moment in the evaluation phase is a **predicted failure**: the sample policy context deliberately omits an international return window, so the eval set surfaces a groundedness failure you called in advance. That proves the dataset was designed rather than generated.

**Suggested visual:** Evaluator taxonomy table, plus a small aggregate-vs-rows contrast graphic.

**Walkthrough tie-in:** Phase 10. Also connects back to Phase 5 (the prompt scenario) and Phase 6 (the trace behind a failing row).

> **Show the NEW Microsoft Foundry portal:** **Build > Evaluations**, in the Optimize group.

---

## Slide 13 — Foundry vs. dedicated observability platforms

**Main message:** The question is not *which tool*. It is *which layer*.

**Bullets**

- **Foundry** is part of the **control plane** — it can enforce, because it owns the runtime.
- A specialist platform (Arize, Phoenix, LangSmith, Langfuse) is an **analysis layer** on top of whatever you run.
- Specialists genuinely win on **multi-provider reach**, **drift and embedding analysis**, and **human-labeling UX**.
- Foundry wins on **enforcement**, **data boundary**, and **no second governance island**.
- **OpenTelemetry** makes coexistence an architecture choice, not a rewrite.

**Speaker notes:** Someone in the room is already using one of these, or has been pitched one. Never disparage the competing product — being fair to their decision is exactly what makes your Foundry claims land. State the concessions before the strengths. Keep all claims at the architectural-category level; do not assert specifics about a third party's current feature set from a slide.

**Suggested visual:** Two-layer diagram — control plane (enforce) beneath analysis layer (observe), with an OTel arrow connecting them.

**Walkthrough tie-in:** Phase 11 — a discussion, not a demo. No third-party accounts are required at any point.

---

## Slide 14 — Reference architecture

**Main message:** How the pieces fit in a real Azure landing zone.

**Bullets**

- **Entra ID + Azure RBAC** — identity and access, no separate directory.
- **Foundry resource → project → deployments** — scope and blast radius.
- **Guardrails at the inference endpoint**; **Azure Policy** above for fleet enforcement.
- **App Insights / Log Analytics** — traces, metrics, KQL, retention, and cost under existing governance.

**Speaker notes:** Keep this to ninety seconds. The purpose is to give architects a mental slot for each thing they are about to see, not to design their environment. Point out that nothing on this diagram is AI-specific except the guardrail and evaluation boxes — that is the whole argument for running AI governance inside the platform you already govern.

**Suggested visual:** Single-page architecture diagram, layered, with the AI-specific components highlighted.

**Walkthrough tie-in:** Every phase maps to a box on this diagram.

---

## Slide 15 — Walkthrough roadmap: what you'll see

**Main message:** Here is the order, and here is when to speak up.

**Bullets**

- **[TOUR]** phases are read-only navigation. **[DEMO]** phases are live creation — that is where things can break.
- The order is deliberate: build the concrete control first, then show the mechanism that mandates it.
- Discussion is scheduled, not squeezed in. Every phase has prompts.
- Total: about 2.5 hours of walkthrough plus discussion.

**Speaker notes:** Show the phase table and name the two moments you most want them present for: the **live guardrail block** in Phase 8 and the **row-level evaluation failure** in Phase 10. Tell them plainly that if a preview feature is unavailable on the day, you will switch to a prepared screenshot and say so rather than improvising.

**Suggested visual:** The phase table below, with [DEMO] rows highlighted.

| Phase | Content | Mode | Time |
|---|---|---|---:|
| 1 | Environment and access validation | [TOUR] | 5 min |
| 2 | Create or open a Foundry project | [TOUR] | 5 min |
| 3 | Governance and observability feature tour | [TOUR] | 15 min |
| 4 | Model deployment and access controls | [TOUR] | 10 min |
| 5 | Run a prompt scenario | **[DEMO]** | 10 min |
| 6 | Capture traces, logs, metrics | **[DEMO]** | 10 min |
| 7 | Review observability signals | [TOUR] | 10 min |
| 8 | **Create a custom guardrail** | **[DEMO]** | 20 min |
| 9 | **Create a guardrail policy** | **[DEMO]** | 20 min |
| 10 | Evaluation deep dive | **[DEMO]** | 30 min |
| 11 | Contrast vs. dedicated observability platforms | Discussion | 20 min |
| 12 | Responsible AI wrap-up and cleanup | Discussion | 10 min |

**Walkthrough tie-in:** This is the agenda. Leave it up during breaks.

---

## Slide 16 — How to participate

**Main message:** Interrupt. A silent walkthrough has failed.

**Bullets**

- Ask about **your** environment — the useful questions are specific.
- Challenge the claims, especially in the competitive discussion.
- Flag anything you cannot do today because of access, policy, or region.
- Capture your own follow-ups; we will collect open items at the end.

**Speaker notes:** Give explicit permission to interrupt, then honor it the first time someone does — the first interruption sets the tone for the whole session. Note that you are recording open items and unverified portal paths as you go, and that they will get that list afterward.

**Suggested visual:** Three prompts — "Ask", "Challenge", "Flag" — as large cards.

---

## Slide 17 — Takeaways and next steps

**Main message:** Six things to remember, one thing to do.

**Bullets**

- Governance is a chain of evidence, not a document.
- A **guardrail** protects a workload; a **guardrail policy** protects the fleet.
- A **trace** says what happened; an **evaluation** says whether it was good enough.
- **Aggregate scores decide whether to worry; rows decide what to fix.**
- Foundry governs the runtime; an observability platform analyzes behavior — pick the layer, not the vendor.
- Telemetry, identity, and enforcement stay inside the Azure boundary you already govern.

**Speaker notes:** Close on the one action you want from each role in the room: platform owners should identify which of the four operating questions from Slide 4 they cannot answer today; architects should decide whether AI guardrails belong in their existing Azure Policy estate; sellers should note which customers already have an incumbent observability tool, because that changes the conversation. Then hand off to the walkthrough.

**Suggested visual:** Six takeaway cards, plus a single "your next action" call-out.

**Walkthrough tie-in:** Phase 12.

---

## Slide 18 — Bonus: red teaming and adversarial testing

**Main message:** Red teaming helps you answer one question explicitly: *What breaks when someone tries to misuse or manipulate the system?*

**Bullets**

- It complements guardrails and evaluations — it does not replace them.
- Use synthetic prompt sets to test prompt injection, sensitive data requests, and risky policy bypass attempts.
- Record outcomes as refuse, clarify, safe complete, escalate, or fail.
- Tie the result back to release criteria and human review decisions.
- Keep it optional, scoped, and aligned to Foundry + Azure governance practices.

**Speaker notes:** This is an advanced add-on, not the center of the workshop. Say plainly that red teaming is not a stunt; it is a formal risk assessment step. If a new customer asks about it, the relevant question is not whether they can run a red-team tool, but whether they know what they are testing, what counts as failure, and what the release decision is after the results come back.

**Suggested visual:** Diagram of a red-team loop — test → classify → log → decide → remediate.

**Walkthrough tie-in:** Optional follow-on after the main governance and observability path. Use it to show how offensive testing complements the preventive and detective controls already covered.

> **Use the NEW Microsoft Foundry portal** for any live feature reference. If the capability is preview or hidden, say *Verify in the current Microsoft Foundry portal* and proceed without guessing a path.

---

## Slide 19 — Bonus: evaluations as a release gate (GitHub Actions)

**Main message:** An evaluation without a threshold is a report. An evaluation with a threshold is a control.

**Bullets**

- A GitHub Actions workflow runs the Phase 10 evaluation set on every pull request.
- **Entra OIDC federated credentials** — no client secret stored in the repository.
- Aggregate scores are compared to thresholds in `eval-config.yaml`; a breach **fails the build**.
- Row-level results ship as an artifact and a PR comment, so failures are inspectable.
- Branch protection is what turns the check from advisory into enforcing.

**Speaker notes:** This is the third leg of the control story. Phase 8 was a **runtime** control, Phase 9 a **platform** control, and this is a **change** control. Most customers already have all three for their conventional software and none of them for AI. The demo beat to plan for is deliberately failing the gate by tightening the groundedness threshold, then reading the failing row's judge reason out loud — that is where aggregate-vs-rows stops being a slogan. Sample code lives in `ci-cd/`; pre-stage the Entra app registration and role assignment, because creating them live teaches nothing about Foundry.

**Suggested visual:** Split screen — the red failing check on a pull request, next to the `eval-config.yaml` threshold line that caused it.

**Walkthrough tie-in:** Phase 14. Optional and advanced; skip it if the room is not build-pipeline literate.

> **Use the NEW Microsoft Foundry portal** to review the same evaluation under **Build > Evaluations** and to trace failing rows. **Verify in the current Microsoft Foundry portal** before asserting a menu path. Foundry data-plane role names change — verify the current role name before quoting it.

---

## Appendix A1 — Preview capabilities to validate before delivery

Anything below can be unavailable, regional, or renamed. Confirm each one **within 48 hours** of delivery and prepare a fallback screenshot for any that fails.

- Trace Replay *(preview)*
- Agent Monitoring Dashboard *(preview)*
- Routines *(preview)* and Workflows *(preview)* tabs on the Agents page
- Models *(preview)* tab on the Deployments page
- Trace-based evaluation, conversation-level evaluation, synthetic-data evaluation
- Security posture and Data security and governance tabs under Operate > Compliance

---

## Appendix A2 — Portal verification checklist

Run this immediately before you present.

- [ ] **New Foundry** toggle is on
- [ ] Correct project selected in the upper-left selector
- [ ] **Build > Deployments** shows the expected deployment
- [ ] **Open in playground** works from the deployment details pane
- [ ] Guardrail exists **and is assigned** — *Try in Playground* only appears when assigned
- [ ] Guardrail policy pre-created, with at least one non-compliant asset visible (Azure Policy can take 30 minutes to scan)
- [ ] A completed evaluation result is available as a fallback
- [ ] Unrelated tabs closed; API key pane hidden; demo tenant in use
- [ ] All data on screen is synthetic

---

## Appendix A3 — Explicitly out of scope

State these once, early, so nobody waits for them.

- **Agent 365** — no license, entitlement, configuration, or dependency anywhere in this session.
- **Microsoft 365 Copilot extensibility** and productivity-agent workflows.
- Third-party observability platform **demos** — discussed architecturally in Phase 11, never demonstrated.
- Participant-provisioned environments — this is a walkthrough; the hands-on variant is a separate deliverable.
