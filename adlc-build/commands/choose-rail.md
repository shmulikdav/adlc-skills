---
name: choose-rail
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
Your first action must be a Skill tool call for each of these skills: `adlc-build:execution-rail-selection`, `adlc-build:small-batch-delivery`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Inventory
Detect installed frameworks and state directories; list slot collisions.

### Step 2: Decide
Apply the **execution-rail-selection** skill: one owner per slot, collisions resolved.

### Step 3: Delivery shape
Apply **small-batch-delivery** to set the PR budget and stacking policy the chosen rail must respect.

### Step 4: Output
One-page stack decision with artifact wiring and a 2-week trial metric.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `/init-agent-context` (in `adlc-context`; install it if needed): prepare context for the chosen rail
- `/spec-feature` (in `adlc-intent`; install it if needed): run the first feature through it
- `/plan-long-run`: if tasks run for hours
