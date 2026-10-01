---
name: agent-incident-review
description: "Use after a bug, outage, data issue, security event, or near-miss caused or amplified by a coding agent or AI feature, or when asked for a postmortem involving Claude Code, Cursor, or an agent."
---

# Agent Incident Review

## Purpose

"The AI did it" is not a root cause. Agents act inside a system of specs, context, permissions, and gates. The review finds which layer let the failure through and fixes that layer so the next agent run is safer.

## Instructions

1. **Timeline:** reconstruct what happened from transcripts, tool-call logs, commits, CI runs, and deploy logs. Note each decision point the agent took and what information it had.
2. **Impact:** users, data, money, time; detection time and how it was detected.
3. **Layer analysis** — for each layer, did it fail, and how?

| Layer | Question |
|-------|----------|
| Intent/spec | Was the requirement ambiguous or missing? |
| Context | Did the agent lack or misread project knowledge? Was the context stale or poisoned? |
| Permissions | Could the agent do more than it should have? |
| Verification | Why didn't tests/evals/review catch it? |
| Gates | Was a human gate skipped, rubber-stamped, or absent? |
| Human factors | Did confident output reduce scrutiny? Review fatigue? |

4. **Contributing factors**, not a single cause.
5. **Durable fixes:** each finding becomes an artifact: context-file line, skill, hook, test, eval case, permission change, or gate change. Each with owner and date.
6. **Regression asset:** add the incident scenario to the eval or test suite so it can never silently recur.

## Output

```
## Agent Incident Review: [title] — [date]
Summary | Impact | Timeline | Layer analysis | Contributing factors
### Actions
| # | Fix | Artifact type | Owner | Due |
### Regression test / eval added
```

Keep it blameless toward people and precise about systems.
