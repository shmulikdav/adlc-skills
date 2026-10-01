---
description: Pick and wire the agentic execution framework stack (Superpowers, Spec Kit, GSD, BMAD, built-in) with one owner per slot
argument-hint: "<team context, tools installed, main delivery problem>"
---

# /choose-rail -- Execution Stack Decision

## Invocation

```
/choose-rail 12 engineers, Claude Code + Copilot, agents build the wrong thing and PRs are huge
```

## Workflow

Input: $ARGUMENTS

### Step 0: Load the method
Before anything else, load each skill this command uses with the Skill tool: `adlc-build:execution-rail-selection`, `adlc-build:small-batch-delivery`. The answer must follow those skills' rubrics, templates and defaults, not general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Inventory
Detect installed frameworks and state directories; list slot collisions.

### Step 2: Decide
Apply the **execution-rail-selection** skill: one owner per slot, collisions resolved.

### Step 3: Delivery shape
Apply **small-batch-delivery** to set the PR budget and stacking policy the chosen rail must respect.

### Step 4: Output
One-page stack decision with artifact wiring and a 2-week trial metric.
