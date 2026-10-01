# adlc-intent — Agent-ready specs

**ADLC phase:** 1 · Intent

## Overview

Intent specification for coding agents: Agentic PRDs, spec-driven development (constitution, spec, plan, tasks), testable acceptance criteria (Given/When/Then, EARS), spec clarification, and task decomposition.

## Install

```
claude plugin marketplace add braightwave/adlc-skills
claude plugin install adlc-intent@adlc-skills
```

## Skills (5)

- `acceptance-criteria` — Write precise, testable acceptance criteria an agent can verify: Given/When/Then scenarios, EARS-style requirements (When/While/If/Where … the system shall …), edge cases, negative paths, and non-functional thresholds, each mapped to a verification method
- `agentic-prd` — Write an Agentic PRD (Agent Execution Specification): a product spec a coding agent can execute without guessing
- `spec-clarification` — Stress-test a spec before an agent builds it: find ambiguities, contradictions, missing edge cases, unstated assumptions, and decisions an agent would otherwise make silently; return a prioritized question list with suggested defaults
- `spec-driven-development` — Run Spec-Driven Development (SDD) for agentic coding: constitution (project principles) → specify (what and why) → clarify → plan (how) → tasks → implement → converge, with each artifact versioned in the repo
- `task-decomposition` — Break a spec or plan into small, agent-sized tasks: each independently verifiable, ordered by dependency, marked for parallel execution where safe, with explicit inputs, outputs, files touched, and a done check

## Commands (3)

- `/clarify-spec` — Hunt for ambiguities, contradictions, and silent decisions in a spec before an agent builds it
- `/spec-feature` — Run the full spec-driven loop for a feature — constitution check, spec, clarify, plan, tasks — before any code is written
- `/write-agentic-prd` — Turn a feature idea or ticket into an Agentic PRD a coding agent can execute without guessing

---

Part of [ADLC Skills](../README.md). MIT licensed.
