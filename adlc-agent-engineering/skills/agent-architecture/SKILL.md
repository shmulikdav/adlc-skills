---
name: agent-architecture
description: "Use when designing a new AI agent or LLM feature, when someone asks whether something should be an agent, or when an existing agent is too unreliable, slow, or expensive."
---

# Agent Architecture

## Purpose

Most problems that look like they need an agent are better served by a workflow. Start with the simplest design that meets the goal; add autonomy only when the task genuinely requires open-ended decisions.

## Decision ladder

1. **Single call + retrieval/tools** — the task is one step with good context.
2. **Workflow** — steps are known in advance:
   - *Prompt chaining:* fixed sequence with checks between steps
   - *Routing:* classify input, send to a specialized path
   - *Parallelization:* split into independent subtasks or vote on one
   - *Orchestrator-workers:* a planner delegates subtasks that can't be predefined
   - *Evaluator-optimizer:* generate, critique, refine against clear criteria
3. **Agent loop** — the path can't be predicted; the model decides next steps using tools and environment feedback.

Move down the ladder only with evidence that the simpler level fails.

## Design checklist

- Goal and success criteria (measurable, outcome-based)
- Autonomy boundary: what the agent may decide vs what requires a human
- Tools: minimal set, clear contracts (see tool design)
- State & memory: what persists, where, for how long, and who can write it
- Stop conditions: step/time/cost limits, success detection, escalation path
- Failure handling: retries, fallbacks, safe defaults, partial results
- Observability and evals from day one

## Output

```
## Agent Design: [name]
Problem & success criteria
Chosen pattern & why simpler patterns are insufficient
Architecture diagram (mermaid)
Tools | Memory | Human checkpoints | Stop conditions | Failure modes & handling
Eval plan (link) | Cost envelope
```

---

### Further Reading

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
