# adlc-agent-engineering — Building agents as products

**ADLC phase:** ★ Agent engineering

## Overview

Agent engineering for teams building AI agents and LLM features: architecture patterns, tool design, eval suites, prompts as versioned code, and runtime guardrails.

## Install

```
claude plugin marketplace add shmulikdav/adlc-skills
claude plugin install adlc-agent-engineering@adlc-skills
```

## Skills (5)

- `agent-architecture` — Use when designing a new AI agent or LLM feature, when someone asks whether something should be an agent, or when an existing agent is too unreliable, slow, or expensive
- `agent-runtime-guardrails` — Use when shipping an agent to users or connecting it to real systems, after a red-team or prompt-injection finding, or when mapping an agent's controls to the OWASP Agentic Top 10
- `eval-suite-design` — Use when building evals for an agent or LLM feature, before changing models or prompts, when moving an agent from demo to production, or when asked how to know the agent got better or worse
- `prompt-versioning` — Use when prompts or model settings live in dashboards or chats without history, when a prompt or model change broke production behavior, or when setting up a change process for LLM features
- `tool-design` — Use when building function-calling tools or an MCP server for agents, when an agent misuses, ignores, or loops on a tool, or when reviewing an agent's tool set

## Commands (3)

- `/build-evals` — Create an eval suite for an agent or LLM feature with tasks, graders, thresholds, and CI wiring
- `/design-agent` — Design an AI agent or LLM feature — pick the simplest working pattern, tools, guardrails, and eval plan
- `/red-team-agent` — Red-team an agent design or running agent against the OWASP Agentic Top 10 and turn findings into guardrails and eval cases

## Evals (7 cases)

Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.

```
claude plugin eval ./adlc-agent-engineering
```

---

Part of [ADLC Skills](../README.md). MIT licensed.
