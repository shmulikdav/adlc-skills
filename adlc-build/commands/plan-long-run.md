---
description: Plan multi-hour or multi-day agent work — decomposition, state files, checkpoints, budgets, abort criteria, review shape
argument-hint: "<the large task, e.g., migration or backlog burn-down>"
---

# /plan-long-run -- Long-Running Agent Work

## Invocation

```
/plan-long-run Migrate 340 API endpoints from Express to Fastify with agents over two weeks
```

## Workflow

Input: $ARGUMENTS

### Step 1: Fit check
Apply the **long-running-agent-work** skill's fit criteria; recommend a smaller approach if the task isn't verifiable at scale.

### Step 2: Run design
Decomposition, state files, coordination model, checkpoints with owners, budgets, abort criteria.

### Step 3: Execution stack
Apply **execution-rail-selection** to choose the rail and orchestration features to use.

### Step 4: Review shape
Apply **small-batch-delivery** so output lands as reviewable stacked PRs.

### Step 5: Output
Run plan plus a pilot package to execute first.
