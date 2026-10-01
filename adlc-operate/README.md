# adlc-operate — Release, observe, learn

**ADLC phase:** 6 · Operate

## Overview

Operating the ADLC: release gates, Continuous AI background workflows, AgentOps observability, AI cost management, a learning loop from rejected agent work, and blameless agent incident reviews.

## Install

```
claude plugin marketplace add shmulikdav/adlc-skills
claude plugin install adlc-operate@adlc-skills
```

## Skills (6)

- `agent-incident-review` — Use after a bug, outage, data issue, security event, or near-miss caused or amplified by a coding agent or AI feature, or when asked for a postmortem involving Claude Code, Cursor, or an agent
- `agentops-observability` — Use when running agents in CI or production, debugging what an agent did after the fact, needing an audit trail of agent actions, or building an AgentOps or LLM observability practice
- `ai-cost-management` — Use when token or AI spend is growing or unpredictable, when building an AI cost dashboard, pricing an AI feature, or checking whether an agent workflow or feature is economically viable
- `continuous-ai-workflows` — Use when a team wants agents running in the background on a schedule or on repository events (issue triage, docs upkeep, test improvement, CI failure investigation, cleanup of low-quality generated code), is evaluating GitHub Agentic Workflows or Claude Code routines, or asks what to automate with agents in CI
- `learning-loop` — Use when agents keep making the same kinds of mistakes across PRs, when review comments on agent work repeat, when many agent PRs are rejected or abandoned, or when a team asks how to make each unit of agent work improve the next one
- `release-gates` — Use when agents produce changes faster than the release process can absorb, when designing CI/CD gates for AI-generated code, before a go/no-go decision, or when deciding which changes still need human approval

## Commands (4)

- `/agent-postmortem` — Blameless post-incident review for agent-caused failures that turns findings into durable fixes
- `/mine-rejections` — Turn rejected agent PRs and repeated review comments into durable fixes — context, skills, hooks, tests, evals
- `/plan-continuous-ai` — Choose and guardrail background agent workflows (triage, CI failure investigation, docs, test gaps, cleanup) for a repository
- `/release-check` — Run a go/no-go release check for agent-built changes with gate evidence and rollback readiness

## Evals (7 cases)

Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.

```
claude plugin eval ./adlc-operate
```

---

Part of [ADLC Skills](../README.md). MIT licensed.
