---
description: Implement an approved plan test-first, verifying after each step and producing small, reviewable PRs
argument-hint: "<plan path or approved plan>"
---

# /build-feature -- Test-First Implementation

## Invocation

```
/build-feature plan.md
```

## Workflow

### Step 1: Load the plan
Read $ARGUMENTS. If no approved plan exists, stop and suggest planning first.

### Step 2: Tests first
Apply the **agentic-tdd** skill: write failing tests from the acceptance criteria, confirm they fail correctly, and pause for a quick test review before committing them.

### Step 3: Implement
Apply the implement stage of **explore-plan-implement**: step by step, verifying after each step, without editing committed tests.

### Step 4: Slice into PRs
Apply **small-batch-delivery** and fill the PR template for each slice.

### Step 5: Report
Summary of tests added, verification results, deviations from the plan, and open items.

### Step 6: Offer next steps
- "Want an independent alignment review of these PRs?"
