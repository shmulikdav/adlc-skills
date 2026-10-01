# adlc-operate — Release, observe, learn

**ADLC phase:** 6 · Operate

## Overview

Operating the ADLC: release gates for agent-built changes, AgentOps observability, AI cost management and unit economics, and blameless agent incident reviews that feed durable fixes back into the lifecycle.

## Install

```
claude plugin marketplace add braightwave/adlc-skills
claude plugin install adlc-operate@adlc-skills
```

## Skills (4)

- `agent-incident-review` — Use after a bug, outage, data issue, security event, or near-miss caused or amplified by a coding agent or AI feature, or when asked for a postmortem involving Claude Code, Cursor, or an agent
- `agentops-observability` — Use when running agents in CI or production, debugging what an agent did after the fact, needing an audit trail of agent actions, or building an AgentOps or LLM observability practice
- `ai-cost-management` — Use when token or AI spend is growing or unpredictable, when building an AI cost dashboard, pricing an AI feature, or checking whether an agent workflow or feature is economically viable
- `release-gates` — Use when agents produce changes faster than the release process can absorb, when designing CI/CD gates for AI-generated code, before a go/no-go decision, or when deciding which changes still need human approval

## Commands (2)

- `/agent-postmortem` — Blameless post-incident review for agent-caused failures that turns findings into durable fixes
- `/release-check` — Run a go/no-go release check for agent-built changes with gate evidence and rollback readiness

## Evals (5 cases)

Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.

```
claude plugin eval ./adlc-operate
```

---

Part of [ADLC Skills](../README.md). MIT licensed.
