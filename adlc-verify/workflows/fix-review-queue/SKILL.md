---
name: fix-review-queue
description: "Run the ADLC fix-review-queue workflow: diagnose and redesign code review when agent PRs pile up — risk tiers, machine first pass, ownership, WIP limits. Use when the user invokes $fix-review-queue or asks for this workflow end to end."
---

> Generated from the Claude Code command `/fix-review-queue` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $fix-review-queue -- Review Capacity Redesign

## Invocation

```
$fix-review-queue 14 engineers, ~120 PRs/week (half agent-authored), median pickup 2 days, reviewers rubber-stamp big diffs
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-verify:review-capacity`, `adlc-verify:definition-of-done`, `adlc-verify:agent-code-review`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Diagnose
Apply the **review-capacity** skill's queue measurement: pickup, review time, size, acceptance and re-review rounds by PR type. Ask for data or estimates if missing.

### Step 2: Redesign
Apply **review-capacity**: ownership, risk tiers and routing, layers 0–3, context packet, WIP limits.

### Step 3: Raise the floor
Apply **definition-of-done** for the authoring contract and **agent-code-review** for what the human pass focuses on.

### Step 4: Output
Diagnosis table, tier and routing rules, layer configuration, PR context-packet template, metrics to track for 30 days.
