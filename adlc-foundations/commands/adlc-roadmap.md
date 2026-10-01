---
name: adlc-roadmap
description: Build a phased 90-day ADLC adoption roadmap (Map → Prioritize → Build → Scale) for an engineering organization
argument-hint: "<org context, readiness findings, or goals>"
---

# /adlc-roadmap -- 90-Day ADLC Adoption Roadmap

## Invocation

```
/adlc-roadmap 60-engineer SaaS company, Level 1 maturity, goal: agent-built PRs for 40% of backlog by Q2
/adlc-roadmap [attach an ADLC readiness report]
```

## Workflow

Input: $ARGUMENTS

### Step 0: Load the method
Your first action must be a Skill tool call for each of these skills: `adlc-foundations:adlc-readiness-assessment`, `adlc-foundations:adlc-metrics`, `adlc-foundations:sdlc-to-adlc-mapping`, `adlc-foundations:ai-stance-policy`, `adlc-foundations:autonomy-levels`, `adlc-foundations:ai-champions-program`, `adlc-foundations:role-transitions`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Ground the roadmap
Use any readiness report in context. If none exists, run a short version of the **adlc-readiness-assessment** skill first.

### Step 2: Structure the phases

**Map (weeks 1–2):** baseline metrics (**adlc-metrics**), workflow mapping (**sdlc-to-adlc-mapping**), AI stance published (**ai-stance-policy**).

**Prioritize (weeks 3–4):** choose one pilot team and three task types using **autonomy-levels**; define success criteria and guardrail metrics.

**Build (weeks 5–10):** pilot runs with context files, spec-driven work, verification gates; champions selected (**ai-champions-program**).

**Scale (weeks 11–13):** expand to the next teams through champions; update role expectations (**role-transitions**); publish an internal skills/plugin library.

### Step 3: Make it executable
For each phase: deliverables, owner, exit criteria, risks. Add a decision gate between phases: go / extend / stop, based on metrics, not sentiment.

### Step 4: Output
```
## ADLC Roadmap: [Org]
### Goal and success metrics
### Phase plan (table: phase | weeks | deliverables | owner | exit criteria)
### Pilot selection rationale
### Risks and mitigations
### Decision gates
```
Save as markdown.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- Continue here: Want me to draft the AI stance announcement?
- Continue here: Should I design the champions program in detail?
- `/init-agent-context` (in `adlc-context`; install it if needed): first build-phase move: context files
- `/governance-pack` (in `adlc-govern`; install it if needed): policy and permissions before scaling
- `/fix-review-queue` (in `adlc-verify`; install it if needed): if review will become the bottleneck
