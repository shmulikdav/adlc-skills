# adlc-intent — Agent-ready specs

**ADLC phase:** 1 · Intent

## Overview

Intent specification for coding agents: Agentic PRDs, spec-driven development, testable acceptance criteria (Given/When/Then, EARS), spec clarification, task decomposition, and architecture guardrails (ADRs, invariants, dependency rules).

## Install

```
claude plugin marketplace add shmulikdav/adlc-skills
claude plugin install adlc-intent@adlc-skills
```

## Skills (6)

- `acceptance-criteria` — Use when writing or fixing acceptance criteria for a feature an agent will build or test, when criteria are vague or untestable, or before generating tests from a spec or user story
- `agentic-prd` — Use when a PM or engineer is about to hand a feature, ticket, or PRD to a coding agent, asks to make a spec agent-ready, or when an agent built the wrong thing from a vague requirement
- `architecture-guardrails` — Use when agent-built code drifts from the intended architecture, modules start depending on each other in ways they shouldn't, design decisions live only in Slack or people's heads, or a team wants agents to respect architectural rules without micromanaging every implementation
- `spec-clarification` — Use when reviewing a spec, PRD, or ticket before an agent builds it, when the user asks what is missing from a spec or says 'interview me about this feature', or when requirements may hide decisions an agent would make silently
- `spec-driven-development` — Use when a team wants a spec-first workflow for coding agents, mentions GitHub Spec Kit, Kiro specs, or AWS AI-DLC, wants to move from vibe coding to repeatable delivery, or starts a feature with real ambiguity or risk
- `task-decomposition` — Use when converting a spec or plan into tasks for coding agents, preparing work for parallel sessions or worktrees, or when an agent keeps failing or drifting on tasks that are too large

## Commands (3)

- `/clarify-spec` — Hunt for ambiguities, contradictions, and silent decisions in a spec before an agent builds it
- `/spec-feature` — Run the full spec-driven loop for a feature — constitution check, spec, clarify, plan, tasks — before any code is written
- `/write-agentic-prd` — Turn a feature idea or ticket into an Agentic PRD a coding agent can execute without guessing

## Evals (8 cases)

Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.

```
claude plugin eval ./adlc-intent
```

---

Part of [ADLC Skills](../README.md). MIT licensed.
