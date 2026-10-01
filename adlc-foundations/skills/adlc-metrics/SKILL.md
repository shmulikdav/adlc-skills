---
name: adlc-metrics
description: "Use when someone asks how to measure the ROI or productivity impact of coding agents (Claude Code, Cursor, Copilot, Codex), wants an AI engineering dashboard, needs a baseline before a rollout, or is about to report self-reported speedups as results."
---

# ADLC Metrics & ROI Measurement

## Purpose

Developers' sense of speed is a poor measurement instrument. In METR's 2025 randomized trial, experienced open-source developers expected AI to make them faster, felt faster afterwards, and were measured as slower. Measure outcomes, not impressions.

## Metric layers

**1. Outcome (does the business get more value?)**
- Lead time for changes, deploy frequency, change-failure rate, time to restore (DORA four keys)
- Cycle time from spec approved → in production

**2. Agent effectiveness (is the agent doing useful work?)**
- PR acceptance rate for agent-authored PRs
- Rework rate: % of agent changes modified or reverted within 14 days
- Review time per agent PR vs human PR
- Escaped defects attributed to agent-authored code
- Share of tasks completed at each autonomy level

**2b. Review flow (where the 2026 bottleneck sits)**
- Pickup time and review time by PR type (human / AI-assisted / agentic)
- PR size, acceptance rate within 30 days, re-review rounds
- Open agent PRs per reviewer (queue depth)

**3. Economics**
- Token/licence cost per merged change and per active engineer
- Cost per resolved ticket for agent-handled task types

**4. Adoption & experience (leading indicators only)**
- Weekly active users, sessions per engineer
- Developer-reported friction (short pulse survey)

## Reference frameworks

- **DORA** delivery metrics, including rework rate
- **DX AI Measurement Framework** (utilization, impact, cost) alongside DX Core 4 (speed, effectiveness, quality, impact). DX's Q2 2026 data is the cautionary tale: median AI spend grew roughly 28× in a year while the share of time on new capabilities stayed flat around 57–58%
- Expect gains to show up as **more output** (including work that would not have been done at all) more than as faster tasks, so measure throughput and what it was spent on, not only cycle time

## Instructions

1. Establish a **baseline** for 4–6 weeks before or alongside the rollout. No baseline, no ROI claim.
2. Choose a **comparison design**: pilot vs control team, or within-team task randomization for the same task types.
3. Define **attribution**: label agent-authored commits/PRs (trailer, label, or branch prefix).
4. Specify data sources for each metric (Git host API, CI, issue tracker, billing export).
5. Set **guardrail metrics** that must not degrade (change-failure rate, escaped defects, security findings).

## Output

```
## ADLC Metrics Plan: [Team]
### Baseline period & comparison design
### Metric table
| Layer | Metric | Definition | Source | Baseline | Target | Guardrail? |
### Attribution method
### Review cadence & owner
### Known biases and how we control them
```

## Notes

- Lines of code and number of prompts are vanity metrics. Do not report them as productivity.
- Report rework alongside throughput. Throughput without stability is borrowing from the future.
- Re-baseline when models or tools change materially.

---

### Further Reading

- [METR: Measuring the impact of early-2025 AI on experienced open-source developer productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- [DORA research publications](https://dora.dev/research/publications/)
