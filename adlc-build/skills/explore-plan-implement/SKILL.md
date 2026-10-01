---
name: explore-plan-implement
description: "Run the core agentic coding loop: explore the relevant code read-only, write a reviewable plan, implement against the plan with verification after each step, then commit with a traceable message. Use for any non-trivial code change with a coding agent, when the user says 'plan first', 'don't start coding yet', or when previous attempts solved the wrong problem."
---

# Explore → Plan → Implement → Commit

## Purpose

Letting an agent code immediately often produces a correct solution to the wrong problem. Separating exploration and planning from execution puts a cheap human checkpoint before the expensive part.

## Instructions

### 1. Explore (read-only)
- Read the spec/ticket and the context file.
- Find the relevant entry points, similar existing implementations, and tests. Use subagents for broad searches.
- Summarize: current behavior, files involved, constraints, risks. Do not edit anything.

### 2. Plan
Write `plan.md` (or present it in plan mode):
```
Goal (one sentence, linked to spec/AC IDs)
Approach and why (alternatives considered in one line each)
Steps: numbered, each with files touched and a verification command
Tests to add or change
Risks / things that could break
Out of scope
```
Stop for human approval when the change touches more than a couple of files, public interfaces, data, or security-sensitive code.

### 3. Implement
- Execute step by step. After each step, run its verification (tests, type check, lint, or a run command).
- If reality diverges from the plan, update the plan first, then continue. Do not silently change approach.
- Keep diffs minimal; no drive-by refactors unless planned.

### 4. Verify & commit
- Run the full relevant test suite and checks.
- Self-review the diff against the plan and acceptance criteria; list anything not done.
- Commit with a message that references the spec/AC IDs and explains why, not only what.

## Notes

- For a typo or one-line fix, skip the formal plan; the overhead isn't worth it.
- Provide verification criteria up front. An agent with a test to pass outperforms an agent asked to "make it work".

---

### Further Reading

- [Claude Code best practices: explore first, then plan, then code](https://code.claude.com/docs/en/best-practices)
