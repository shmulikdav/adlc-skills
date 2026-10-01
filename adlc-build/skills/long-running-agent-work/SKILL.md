---
name: long-running-agent-work
description: "Use when planning agent work that spans many hours, days, or dozens of sessions, coordinating multiple agents or agent teams on one project, running large migrations or backlog burn-downs with agents, or when long agent runs lose coherence, stall, or blow their budget."
---

# Long-Running & Multi-Agent Work

**Grounded in:** Anthropic: Harness design for long-running application development; Anthropic: 2026 Agentic Coding Trends Report.





## Overview

Agents now run for hours or days and coordinate as teams: Anthropic's 2026 trends report expects task horizons to extend from minutes to days, with humans providing oversight at key decision points rather than on every step. The failure modes change accordingly: lost state, drift from intent, duplicated or conflicting work, silent budget burn, and a mountain of output nobody can review.

**Core rule:** design the checkpoints, state, and budget before starting, the way you would for a human project team.

## Design elements

| Element | Decision to make |
|---------|-----------------|
| Decomposition | Work packages with clear interfaces; which run in parallel, which serialize (shared schema, lockfiles, migrations) |
| State | Externalized plan, progress log, and decision log in the repo, so any fresh session or agent can resume |
| Coordination | One orchestrator or lead; workers own disjoint files; communication through artifacts, not chat history |
| Checkpoints | Human decision points at phase boundaries and on predefined triggers (scope change, failed verification twice, budget at 50%) |
| Verification | Each package ends with its own done check; integration tests run after every merge |
| Budget | Token/cost and wall-clock caps per package and overall; alerts at thresholds |
| Review shape | Output lands as small, stacked PRs sized for review capacity, not one giant branch |
| Abort criteria | When to stop and re-plan rather than let agents grind |

## Instructions

1. Confirm the work is worth a long run: high volume, well-specified, verifiable (migrations, test backfills, framework upgrades, backlog of similar fixes).
2. Write the plan and decomposition; mark parallel packages and shared-resource conflicts.
3. Create the state files and the checkpoint schedule; name the human who owns each checkpoint.
4. Set budgets and abort criteria.
5. Run a pilot package end to end; measure cost, quality, and review effort; adjust before scaling out.
6. At each checkpoint: review progress against intent, rework rate, and spend; continue, re-plan, or stop.

## Red flags

| Thought | Reality |
|---------|---------|
| "Let it run over the weekend and see" | Without checkpoints and budgets you get a large bill and an unreviewable diff |
| "More agents, faster finish" | Parallelism beyond review capacity just moves the queue |
| "The agent will remember the plan" | Only what's written in the repo survives a new session |

## Output

Run plan: decomposition, state files, coordination model, checkpoint schedule with owners, budgets, abort criteria, and review shape.

---

### Further Reading

- [Anthropic: Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [Anthropic: 2026 Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report)
