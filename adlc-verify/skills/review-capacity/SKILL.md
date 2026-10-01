---
name: review-capacity
description: "Use when agent-authored pull requests pile up waiting for review, reviewers rubber-stamp large AI diffs, merge rates of agent PRs are low, or a team asks how to scale code review now that agents produce more changes than humans can read."
---

# Review Capacity Design

## Overview

The bottleneck has moved from writing code to deciding whether code is safe to merge. LinearB's 2026 benchmarks (8.1M PRs) found agentic PRs wait about 5× longer for a reviewer to pick them up than unassisted PRs, AI-assisted PRs are about 2.6× larger at P75, and only about a third of AI PRs are accepted within 30 days versus most manual PRs. Asking reviewers to "go faster" doesn't fix this. Redesigning the review system does.

**Core rule:** human attention goes to intent, architecture fit, and risk. Everything checkable by a machine is checked before a human sees the PR.

## The review system

| Layer | Who/what | Checks |
|-------|----------|--------|
| 0 · Authoring contract | The agent, before opening the PR | Definition of Done evidence attached; PR within size budget; spec/AC IDs linked |
| 1 · Deterministic gates | CI | Tests, types, lint, secret scan, dependency verification, test-file diff flagged |
| 2 · AI first pass | Review agents (e.g., Claude Code `/code-review`, `/ultrareview` for critical changes, `pr-review-toolkit`, `/security-review`) | Bugs, silent failures, security patterns, spec alignment |
| 3 · Human review, tiered by risk | Owner of the affected area | Intent, architecture fit, product judgment |

## Risk tiers (route, don't queue)

| Tier | Examples | Human review |
|------|----------|--------------|
| Low | Docs, copy, test-only, dependency patch with green suite | Optional sampling (e.g., 1 in 5) after layers 1–2 pass |
| Standard | Feature work behind a flag | One owner, focused on intent and design |
| High | Auth, payments, data migrations, permissions, infra, public APIs | Owner + specialist; AI deep review mandatory first |

Tier by the files touched and the change class, computed automatically (CODEOWNERS, path rules, labels), not by the author's self-assessment.

## Instructions

1. **Measure the queue:** PR pickup time, review time, size, acceptance rate, and re-review rounds, split by human / AI-assisted / agentic. Find where time goes: waiting, reading, or rework.
2. **Fix ownership:** every agent PR gets an accountable human requester and an auto-assigned reviewer. Unowned agent PRs are the main cause of long pickup times.
3. **Shrink the unit:** enforce the PR size budget and stacking (small-batch delivery).
4. **Ship a context packet with every agent PR:** the spec link, plan, what was verified and how, deviations, and where the reviewer should look. Reviewers can't reconstruct the agent's reasoning from a diff.
5. **Install layers 1–2** so humans never review what a machine can reject.
6. **Define tiers** and routing rules; publish review SLAs per tier.
7. **Cap WIP:** limit open agent PRs per requester so generation can't outrun review.
8. **Review the review system monthly:** escaped defects by tier tell you whether low-tier sampling is safe.

## Red flags

| Thought | Reality |
|---------|---------|
| "Add more reviewers" | Throughput rises again and the backlog returns; change how review time is spent |
| "The AI reviewer approved it" | AI review is a filter, not an approval for high-tier changes |
| "Big PRs are fine if the agent wrote tests" | Check whether those tests were weakened in the same PR first |

## Output

Queue diagnosis (table by PR type), tier definitions with routing rules, layer configuration, PR context-packet template, WIP limits, and the metrics to watch.

---

### Further Reading

- [LinearB: AI in software development, 2026 benchmark data](https://linearb.io/library/ai-in-software-development)
- [Anthropic: 2026 Agentic Coding Trends Report (Trend 4: oversight scales through collaboration)](https://resources.anthropic.com/2026-agentic-coding-trends-report)
