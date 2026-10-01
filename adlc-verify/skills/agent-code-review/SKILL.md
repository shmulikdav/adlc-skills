---
name: agent-code-review
description: "Use when reviewing a pull request or diff written by Claude Code, Cursor, Codex, Copilot, or another agent, when setting up a review process for AI-generated code, or before merging agent work into main."
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

## Red flags

| Thought | Reality |
|---------|---------|
| "It reads well, so it's probably right" | Fluent code is the agent's default output; it says nothing about alignment |
| "Tests pass" | Check whether the tests were changed in the same PR |
| "The agent explained its reasoning" | Explanations are generated too; verify against code and spec |
| "Too big to review properly, approve and watch prod" | Send it back to be split; size is a defect |

## Composition

Run machine review first: Claude Code's built-in `/code-review` (multi-agent) and `/ultrareview` (cloud fleet with adversarial critique, for auth, payments, migrations) and `/security-review`. Start the human pass with test integrity: weakened tests, disabled lint, and gated CI steps are where agent-PR risk concentrates.

For general code-quality passes (comments, types, silent failures, simplification), Anthropic's official `pr-review-toolkit` provides specialist reviewers. Use this skill for what those don't check: alignment with the spec and the agent-specific failure patterns.

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
