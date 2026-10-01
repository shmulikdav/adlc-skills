# adlc-foundations — Readiness, operating model & adoption

**ADLC phase:** 0 · Foundations

## Overview

ADLC foundations: readiness assessment on the DORA AI capabilities, SDLC-to-ADLC workflow mapping, agent autonomy levels, AI stance policy, ROI metrics, AI champions program, and role transitions.

## Install

```
claude plugin marketplace add braightwave/adlc-skills
claude plugin install adlc-foundations@adlc-skills
```

## Skills (7)

- `adlc-metrics` — Design a measurement framework for agentic development: delivery metrics (DORA four keys), agent-specific metrics (rework rate, PR acceptance, review time, escaped defects, cost per merged change), and a method to separate perceived from actual productivity
- `adlc-readiness-assessment` — Assess how ready an engineering organization is to move from SDLC to an Agentic Development Lifecycle (ADLC)
- `ai-champions-program` — Design an internal AI Champions / AI Enablers program (train-the-trainer) that spreads agentic development practices across engineering teams: champion selection, enablement curriculum, office hours, shared skills library, cadence, and success metrics
- `ai-stance-policy` — Draft a clear, communicated AI stance for an engineering organization: approved tools, data classification rules for prompts, what agents may and may not do, code ownership and review expectations, IP and licensing, and how the policy evolves
- `autonomy-levels` — Decide how much autonomy to give a coding agent for a given type of task, using a five-level delegation ladder (suggest → draft → execute-with-review → execute-with-gate → autonomous) based on blast radius, reversibility, and verifiability
- `role-transitions` — Describe how each engineering role changes in an Agentic Development Lifecycle (developer, PM, QA, tech lead, engineering manager, designer): what they stop doing, start doing, new skills required, and how to evaluate performance
- `sdlc-to-adlc-mapping` — Map a team's current SDLC workflow, step by step, to its Agentic Development Lifecycle (ADLC) equivalent: who executes each step (human, agent, or both), what artifact changes, what gate a human keeps, and what new failure mode appears

## Commands (3)

- `/adlc-assess` — Assess a team's readiness for the Agentic Development Lifecycle and get a maturity level, gaps, and first moves
- `/adlc-roadmap` — Build a phased 90-day ADLC adoption roadmap (Map → Prioritize → Build → Scale) for an engineering organization
- `/map-to-adlc` — Map your current SDLC workflow to the Agentic Development Lifecycle and pick where agents should enter first

---

Part of [ADLC Skills](../README.md). MIT licensed.
