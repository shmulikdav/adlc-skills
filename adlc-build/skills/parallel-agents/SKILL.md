---
name: parallel-agents
description: "Run multiple coding agents in parallel safely: split work into independent streams, isolate each in a git worktree or separate session, assign roles (implementer, test writer, reviewer), coordinate through files and PRs, and merge without conflicts. Use when someone wants to speed up delivery with several Claude Code sessions, subagents, or agent teams, or asks how to orchestrate agents in parallel."
---

# Parallel Agents

## Purpose

Parallelism multiplies throughput only when streams are independent and verification keeps up. Otherwise it multiplies conflicts and review load.

## Patterns

| Pattern | When | How |
|---------|------|-----|
| Independent tasks | Tasks marked [P] touch disjoint files | One worktree/branch per task, merge in dependency order |
| Writer + reviewer | Quality-sensitive changes | Session A implements; session B (fresh context) reviews the diff against the spec |
| Writer + tester | Behavior-heavy features | One agent writes tests from ACs, another implements |
| Competing hypotheses | Hard bug, unclear cause | Several agents investigate different hypotheses; compare evidence |
| Fan-out research | Large codebase questions | Subagents explore modules and return summaries |

## Instructions

1. Start from a task list (see task decomposition). Confirm independence: disjoint files, no shared unmerged dependency, no shared migrations.
2. Create isolation: `git worktree add ../wt-T07 -b feat/T07` per stream (or separate clones/containers).
3. Give each agent: its task, the spec section, the done check, and the files it owns. Tell it which files it must not touch.
4. Coordinate through artifacts (tasks.md status, PR descriptions), not through long chat histories.
5. Cap concurrency at what humans can review. Review capacity is the real limit.
6. Merge in dependency order; rerun the full test suite after each merge.

## Notes

- Shared resources (DB schema, lockfiles, generated code) are the usual conflict source. Serialize tasks that touch them.
- A fresh-context reviewer catches more than the author agent reviewing itself.
