---
name: learning-loop
description: "Use when agents keep making the same kinds of mistakes across PRs, when review comments on agent work repeat, when many agent PRs are rejected or abandoned, or when a team asks how to make each unit of agent work improve the next one."
---

# Learning Loop (Compounding Agent Work)

## Overview

Every rejected agent PR and every repeated review comment is free training data for your harness. Teams that capture it make the next run better; teams that don't pay for the same mistake indefinitely. With roughly two of three AI PRs not accepted within 30 days in 2026 benchmark data, rejections are the richest signal most teams ignore.

**Core rule:** a mistake that happens twice becomes an artifact: a context-file line, a skill, a hook, a test, or an eval case.

## Signals to mine

| Signal | Where | What it usually reveals |
|--------|-------|-------------------------|
| Rejected / abandoned agent PRs | Git host | Wrong problem solved, missing context, scope creep |
| Repeated review comments | PR review threads | Unwritten conventions |
| Reverts within 14 days | Git history | Verification gaps |
| Human edits on agent branches before merge | Commit diffs | Systematic quality gaps |
| Blocked actions | Hook/permission logs | Agent confusion about boundaries |
| Incidents | Postmortems | Missing gates |

## Instructions

1. **Collect** a month of signals (start with rejected PRs and review comments on agent PRs).
2. **Cluster** by root cause: missing context, unclear spec, convention, verification gap, permission/boundary, model limitation.
3. **Convert** each recurring cluster into the cheapest durable fix:
   - Missing context → context file or linked doc
   - Convention → skill or linter rule
   - Must-never-happen → hook or permission rule
   - Behavior that broke → test
   - Agent-quality regression → eval case
   - Unclear spec → template change in the spec format
4. **Verify** the fix: re-run a representative past task or eval; confirm the mistake no longer occurs.
5. **Prune** quarterly: remove instructions nobody needs anymore (context bloat is also a failure).
6. **Report** the loop: top recurring causes, fixes shipped, measured change in rejection or rework rate.

## Red flags

| Thought | Reality |
|---------|---------|
| "I'll just fix it in my prompt next time" | Prompts don't persist across people or sessions; artifacts do |
| "Add it to CLAUDE.md" (for everything) | Bloated context files get ignored; pick the right mechanism |
| "The model will get better anyway" | Org-specific knowledge never arrives with a model upgrade |

## Output

Monthly learning report: signal volume, root-cause clusters, artifacts shipped (with links), and trend in rejection/rework rate.

---

### Further Reading

- [OpenAI: Harness engineering (encode golden principles in the repo)](https://openai.com/index/harness-engineering/)
- [Claude Code best practices: treat CLAUDE.md like code](https://code.claude.com/docs/en/best-practices)
