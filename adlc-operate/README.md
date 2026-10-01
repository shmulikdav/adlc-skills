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

- `agent-incident-review` — Run a blameless post-incident review for failures caused or amplified by AI agents: reconstruct the agent's trajectory from transcripts and logs, identify which control failed (spec, context, permissions, verification, gate), and turn findings into durable fixes in context files, skills, hooks, tests, or evals
- `agentops-observability` — Instrument agents and agentic workflows for observability: traces of steps and tool calls, inputs/outputs with redaction, latency, token usage, error and retry rates, human intervention points, and dashboards and alerts
- `ai-cost-management` — Measure and control the cost of agentic development and AI features: cost per merged change, per ticket, per run, and per customer; budgets and alerts; model routing; caching; context trimming; and unit-economics stress tests
- `release-gates` — Define human approval gates and automated checks for releasing agent-built changes: what must be true before merge, before staging, before production, and who signs off, with progressive delivery (flags, canaries) and rollback triggers

## Commands (2)

- `/agent-postmortem` — Blameless post-incident review for agent-caused failures that turns findings into durable fixes
- `/release-check` — Run a go/no-go release check for agent-built changes with gate evidence and rollback readiness

---

Part of [ADLC Skills](../README.md). MIT licensed.
