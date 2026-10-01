---
name: agent-code-review
description: "Review agent-authored code for alignment, not just correctness: does the diff implement the spec and only the spec, follow the repo's constraints, keep tests honest, and avoid the typical failure patterns of AI-generated code (invented APIs, silent scope creep, weakened tests, duplicated logic, swallowed errors, insecure defaults). Use when reviewing a PR written by Claude Code, Cursor, Codex, or Copilot, or setting up an AI-assisted review process."
---

# Agent Code Review (Alignment Review)

## Purpose

Reviewing agent output is a different job from reviewing a colleague's code. The code usually compiles and reads well. The risks hide in what it assumes, what it quietly changed, and what it quietly didn't do.

## Review passes

**Pass 1 — Intent alignment**
- Map each change to a requirement/AC. Flag changes with no source (scope creep) and requirements with no change (silent omission).

**Pass 2 — Test integrity**
- Were tests modified? Weakened assertions, new skips, mocks replacing the code under test, special cases for test inputs?

**Pass 3 — AI failure patterns**
- Invented or wrong-version APIs, packages, config keys, CLI flags
- Duplicated helpers instead of reusing existing ones
- Swallowed exceptions, broad catches, silent fallbacks, default values hiding failures
- Over-engineering: abstractions, options, or files nobody asked for
- Stale comments or docs describing intended rather than actual behavior
- Inconsistent naming/patterns versus the rest of the repo

**Pass 4 — Security & data**
- Input validation, authz checks on new paths, secrets in code or logs, injection, unsafe deserialization, dependency additions

**Pass 5 — Operability**
- Logging, metrics, error messages, migrations reversible, feature flag present

## Output

```
## Alignment Review: [PR]
Verdict: Approve / Approve with changes / Request changes
### Requirement coverage (AC → change → status)
### Findings
| # | Severity (blocker/major/minor) | Pass | File:line | Evidence | Fix |
### Questions for the author
```

## Notes

- Self-refute each finding before reporting it: look for evidence it's not a problem. Report only what survives.
- Prefer an independent reviewer context (a fresh session or a reviewer subagent) over the author agent reviewing itself.
