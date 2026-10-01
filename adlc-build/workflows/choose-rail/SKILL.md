---
name: choose-rail
description: "Run the ADLC choose-rail workflow: pick and wire the agentic execution framework stack (Superpowers, Spec Kit, GSD, BMAD, built-in) with one owner per slot. Use when the user invokes $choose-rail or asks for this workflow end to end."
---

> Generated from the Claude Code command `/choose-rail` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $choose-rail -- Execution Stack Decision

## Invocation

```
$choose-rail 12 engineers, Claude Code + Copilot, agents build the wrong thing and PRs are huge
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-build:execution-rail-selection`, `adlc-build:small-batch-delivery`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Inventory
Detect installed frameworks and state directories; list slot collisions.

### Step 2: Decide
Apply the **execution-rail-selection** skill: one owner per slot, collisions resolved.

### Step 3: Delivery shape
Apply **small-batch-delivery** to set the PR budget and stacking policy the chosen rail must respect.

### Step 4: Output
One-page stack decision with artifact wiring and a 2-week trial metric.
