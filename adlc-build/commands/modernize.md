---
description: Plan a legacy system modernization or rebuild with behavior characterization, strategy choice, and verified migration slices
argument-hint: "<system description or repo path>"
---

# /modernize -- Legacy Modernization Plan

## Invocation

```
/modernize Rebuild the PHP merchant dashboard as a TypeScript app
```

## Workflow

Input: $ARGUMENTS

### Step 1: Audit
Apply **legacy-modernization** step 1. If a codebase map does not exist, produce a compact one first. If Anthropic's official code-modernization plugin is installed, recommend it as the execution engine for the slices.

### Step 2: Characterize
Propose characterization tests and recording strategy for the top critical paths.

### Step 3: Behavior spec
Extract the implicit spec; present keep/change/drop decisions for owner review.

### Step 4: Strategy and slices
Recommend strangler-fig or rewrite with rationale; produce the slice plan with parity checks and rollback per slice, sized with **small-batch-delivery**.

### Step 5: Output
Save `Modernization-Plan-[system]-[date].md`.
