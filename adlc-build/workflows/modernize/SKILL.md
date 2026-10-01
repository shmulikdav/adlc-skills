---
name: modernize
description: "Use when the user invokes $modernize, or asks to run the Legacy Modernization Plan workflow from the adlc-build plugin end to end."
---

> Generated from the Claude Code command `/modernize` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $modernize -- Legacy Modernization Plan

## Invocation

```
$modernize Rebuild the PHP merchant dashboard as a TypeScript app
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-build:legacy-modernization`, `adlc-build:small-batch-delivery`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

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

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$map-codebase` (in `adlc-context`; install it if needed): map the system first if you haven't
- `$derive-tests` (in `adlc-verify`; install it if needed): lock behavior with characterization tests
- `$plan-long-run`: run the migration in checkpoints
