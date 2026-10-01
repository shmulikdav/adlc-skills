---
description: Explore the codebase read-only and produce a reviewable implementation plan before any code changes
argument-hint: "<feature, ticket, or spec path>"
---

# /plan-feature -- Explore and Plan

## Invocation

```
/plan-feature specs/012-audit-export/spec.md
/plan-feature Add rate limiting to the public API
```

## Workflow

Input: $ARGUMENTS

### Step 1: Explore
Apply the **explore-plan-implement** skill's explore stage. Read-only. Summarize current behavior, files, constraints, risks.

### Step 2: Plan
Write `plan.md` per the skill's template, linking spec/AC IDs.

### Step 3: Size the delivery
Apply **small-batch-delivery** to split the plan into a PR stack if it exceeds one reviewable PR.

### Step 4: Parallelism check
Apply **parallel-agents** to mark which slices can run in separate worktrees.

### Step 5: Stop for approval
Present the plan and ask for approval or edits. Do not implement in this command.

### Step 6: Offer next steps
- "Approved? Run the build with tests first."
