---
name: plan-long-run
description: "Run the ADLC plan-long-run workflow: plan multi-hour or multi-day agent work — decomposition, state files, checkpoints, budgets, abort criteria, review shape. Use when the user invokes $plan-long-run or asks for this workflow end to end."
---

> Generated from the Claude Code command `/plan-long-run` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $plan-long-run -- Long-Running Agent Work

## Invocation

```
$plan-long-run Migrate 340 API endpoints from Express to Fastify with agents over two weeks
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-build:long-running-agent-work`, `adlc-build:execution-rail-selection`, `adlc-build:small-batch-delivery`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

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

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$verify-change` (in `adlc-verify`; install it if needed): verify each checkpoint
- `$release-check` (in `adlc-operate`; install it if needed): before the result ships
