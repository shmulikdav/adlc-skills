# adlc-agent-engineering — Building agents as products

**ADLC phase:** ★ Agent engineering

## Overview

Agent engineering for teams building AI agents and LLM features: architecture patterns, tool design, eval suites, prompts as versioned code, and runtime guardrails.

## Install

```
claude plugin marketplace add braightwave/adlc-skills
claude plugin install adlc-agent-engineering@adlc-skills
```

## Skills (5)

- `agent-architecture` — Choose the right architecture for an AI agent product: single LLM call, workflow (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer), or autonomous agent loop, and define autonomy boundaries, tools, memory, human checkpoints, and failure handling
- `agent-runtime-guardrails` — Design runtime guardrails for an agent product: input validation and injection defenses, provenance labeling of untrusted content, tool allow-lists and argument validation, output checks, human approval for high-impact actions, rate/cost/step limits, and a kill switch
- `eval-suite-design` — Design an evaluation suite for an AI agent or LLM feature: tasks with success criteria, code-based, model-based, and human graders, capability vs regression evals, multiple trials for non-determinism, and how evals gate releases
- `prompt-versioning` — Treat prompts, system instructions, tool descriptions, and model choices as versioned code: store in the repo, review in PRs, tie every change to eval results, roll out with flags, and keep rollback paths
- `tool-design` — Design tools (functions, MCP tools) that agents use reliably: clear names and descriptions, minimal well-typed parameters, meaningful errors that suggest a fix, token-efficient responses, pagination, idempotency, and safe defaults for side effects

## Commands (3)

- `/build-evals` — Create an eval suite for an agent or LLM feature with tasks, graders, thresholds, and CI wiring
- `/design-agent` — Design an AI agent or LLM feature — pick the simplest working pattern, tools, guardrails, and eval plan
- `/red-team-agent` — Red-team an agent design or running agent against the OWASP Agentic Top 10 and turn findings into guardrails and eval cases

---

Part of [ADLC Skills](../README.md). MIT licensed.
