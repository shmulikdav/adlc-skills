---
name: map-codebase
description: "Use when the user invokes $map-codebase, or asks to run the Codebase Map workflow from the adlc-context plugin end to end."
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

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- Continue here: Want a modernization plan for the highest-risk modules?
- Continue here: Should I set up the context file for this repo?
- `$init-agent-context`: link the map from the context file
- `$modernize` (in `adlc-build`; install it if needed): if this is a legacy system
