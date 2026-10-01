---
name: architecture-guardrails
description: "Use when agent-built code drifts from the intended architecture, modules start depending on each other in ways they shouldn't, design decisions live only in Slack or people's heads, or a team wants agents to respect architectural rules without micromanaging every implementation."
---

# Architecture Guardrails

**Grounded in:** MADR: Markdown Architectural Decision Records; ArchUnit: architecture tests; OpenAI: Harness engineering; Thoughtworks Technology Radar (Vol. 34, April 2026).





## Overview

Agents follow the architecture they can see. Decisions made in meetings and chat don't exist for them. Teams running agent-first codebases report the same lesson: encode the architecture in the repository, and **enforce invariants rather than micromanage implementations** (require that data is validated at the boundary, not which library does it).

**Core rule:** every architectural rule that matters is both written (so the agent can read it) and checked (so the build fails when it's broken).

## Layers

| Layer | Artifact | Enforced by |
|-------|----------|-------------|
| Decisions | ADRs (e.g., MADR format) in `docs/adr/`, short and linked from the context file | Review; agents read before planning |
| Structure | Allowed dependency graph between modules/layers | Architecture tests (e.g., dependency-cruiser, ArchUnit, import-linter) in CI |
| Invariants | "Parse at the boundary", "no direct DB access from UI", "all money is integer minor units" | Linters, type rules, fitness-function tests |
| Golden principles | 5–10 short rules on how this codebase is built | Context file + review checklist |

## Instructions

1. **Harvest** the real architecture: existing ADRs, the module structure, and the rules senior engineers enforce in review.
2. **Write** missing ADRs for decisions agents keep re-litigating (one page each: context, decision, consequences).
3. **Express structure as a dependency rule set** and add an architecture test to CI.
4. **Turn invariants into checks** wherever possible; keep the rest as golden principles in the context file.
5. **Wire into the agent flow:** plans must cite relevant ADRs; a change that needs to break a rule must propose a new ADR instead of silently violating it (a stop-and-ask condition).
6. **Schedule drift detection:** a periodic background agent or CI job reports violations and stale ADRs.

## Red flags

| Thought | Reality |
|---------|---------|
| "The agent will infer the architecture from the code" | It infers the most common pattern, including the mistakes |
| "We'll document the architecture later" | Every agent session before then reinforces the drift |
| "Specify the implementation so it gets it right" | Over-specification breaks; specify invariants and let the agent choose the path |

## Output

ADR backlog, dependency rule set, invariant checks added to CI, golden-principles block for the context file, and drift-detection plan.

---

### Further Reading

- [OpenAI: Harness engineering (enforce invariants, not implementations)](https://openai.com/index/harness-engineering/)
- [MADR: Markdown Architectural Decision Records](https://adr.github.io/madr/)
- [ArchUnit: architecture tests](https://www.archunit.org/)
- [Thoughtworks Technology Radar (Vol. 34, April 2026)](https://www.thoughtworks.com/radar)
