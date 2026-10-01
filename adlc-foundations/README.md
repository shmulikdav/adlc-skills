# adlc-foundations — Readiness, operating model & adoption

**ADLC phase:** 0 · Foundations

## Overview

ADLC foundations: readiness assessment on the DORA AI capabilities, SDLC-to-ADLC workflow mapping, agent autonomy levels, AI stance policy, ROI metrics, AI champions program, role transitions, and comprehension debt.

## Install

```
claude plugin marketplace add shmulikdav/adlc-skills
claude plugin install adlc-foundations@adlc-skills
```

## Skills (8)

- `adlc-metrics` — Use when someone asks how to measure the ROI or productivity impact of coding agents (Claude Code, Cursor, Copilot, Codex), wants an AI engineering dashboard, needs a baseline before a rollout, or is about to report self-reported speedups as results
- `adlc-readiness-assessment` — Use when an organization asks whether it is ready for agentic development or coding agents at scale, wants an AI-readiness or maturity baseline for R&D, is starting an AI transformation of engineering, or reports that AI coding tools are not delivering the expected productivity
- `ai-champions-program` — Use when a company wants to spread agentic development practices beyond early adopters, build an AI champions or AI enablers community, set up train-the-trainer for engineering teams, or adoption has stalled after licenses were bought
- `ai-stance-policy` — Use when an engineering organization needs an AI usage or acceptable-use policy for developers and coding agents, when teams are unsure which tools or data are allowed, or before announcing an AI rollout
- `autonomy-levels` — Use when someone asks whether an agent can do a task on its own, when setting agent permissions or approval requirements per repo or task type, when writing an agent delegation policy, or after an agent did more than it should have
- `comprehension-debt` — Use when teams ship code faster than they understand it, nobody can explain or debug agent-written modules, juniors learn mostly through AI, incident response slows on AI-built code, or leaders worry about skill atrophy and the long-term ability to verify agent output
- `role-transitions` — Use when leaders ask how developer, PM, QA, tech lead, manager, or designer roles change with coding agents, when updating career ladders or job descriptions for agentic development, or when people worry what their job becomes
- `sdlc-to-adlc-mapping` — Use when redesigning a development process around coding agents, explaining SDLC vs ADLC to managers, deciding where agents should enter an existing workflow first, or when a team asks what changes in each lifecycle stage when agents do the work

## Commands (3)

- `/adlc-assess` — Assess a team's readiness for the Agentic Development Lifecycle and get a maturity level, gaps, and first moves
- `/adlc-roadmap` — Build a phased 90-day ADLC adoption roadmap (Map → Prioritize → Build → Scale) for an engineering organization
- `/map-to-adlc` — Map your current SDLC workflow to the Agentic Development Lifecycle and pick where agents should enter first

## Evals (9 cases)

Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.

```
claude plugin eval ./adlc-foundations
```

---

Part of [ADLC Skills](../README.md). MIT licensed.
