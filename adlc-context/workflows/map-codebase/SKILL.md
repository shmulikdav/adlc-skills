---
name: map-codebase
description: "Run the ADLC map-codebase workflow: generate an agent-oriented codebase map with modules, core flows, change recipes, and a risk register. Use when the user invokes $map-codebase or asks for this workflow end to end."
---

> Generated from the Claude Code command `/map-codebase` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $map-codebase -- Codebase Map

## Invocation

```
$map-codebase
$map-codebase focus on the billing service
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-context:context-budget`, `adlc-context:codebase-map`, `adlc-context:agent-context-files`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Scope
Use the user's request to set focus; default is the whole repo.

### Step 2: Explore efficiently
Following the **context-budget** skill, delegate per-module exploration to subagents when the repo is large.

### Step 3: Map
Apply the **codebase-map** skill: module index, core flows, change recipes, risk register, questions.

### Step 4: Save and link
Save `docs/codebase-map.md` and propose a one-line pointer for the context file (**agent-context-files**).

### Step 5: Offer next steps
- "Want a modernization plan for the highest-risk modules?"
- "Should I set up the context file for this repo?"
