---
name: task-decomposition
description: "Use when converting a spec or plan into tasks for coding agents, preparing work for parallel sessions or worktrees, or when an agent keeps failing or drifting on tasks that are too large."
---

# Task Decomposition for Agents

**Grounded in:** Bill Wake: INVEST in good stories and SMART tasks; GitHub Spec Kit.





## Purpose

Agents succeed on tasks that are small, well-bounded, and verifiable. Big tasks drift. Good decomposition is the cheapest reliability improvement available.

## Sizing rules

- One task = one verifiable outcome, typically 1–4 hours of human-equivalent work or a diff an engineer can review in under 15 minutes.
- A task touches a small, named set of files or one module.
- Every task ends with a check: a test that passes, a command output, or an observable behavior.

## Instructions

1. Read the spec and plan. List the deliverables (endpoints, components, migrations, jobs, docs).
2. Order phases: setup → contracts/tests → core implementation → integration → polish/docs.
3. For each task produce:

```
T-07 [P] Implement POST /invoices validation
  Covers: FR-2, AC-3, AC-4
  Depends on: T-03 (schema), T-05 (contract test)
  Files: src/invoices/validate.ts, src/invoices/validate.test.ts
  Done when: `npm test -- validate` passes; contract test T-05 green
  Autonomy: L2
```

4. Mark `[P]` only when tasks touch disjoint files and share no unmerged dependency.
5. Identify the **critical path** and any task that needs a human decision first.
6. Validate coverage: every requirement/AC appears in at least one task; remove tasks with no source requirement.

## Output

`tasks.md` with phases, task list, a dependency summary, parallel groups, and a coverage table (AC → tasks).

## Notes

- Write tests-first tasks before implementation tasks when the behavior is clear.
- If a task needs more than one sentence of "and also", split it.

---

### Further Reading
- [Bill Wake: INVEST in good stories and SMART tasks](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)
- [GitHub Spec Kit](https://github.com/github/spec-kit)
