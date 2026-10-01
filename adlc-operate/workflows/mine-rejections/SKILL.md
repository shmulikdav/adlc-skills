---
name: mine-rejections
description: "Run the ADLC mine-rejections workflow: turn rejected agent PRs and repeated review comments into durable fixes — context, skills, hooks, tests, evals. Use when the user invokes $mine-rejections or asks for this workflow end to end."
---

> Generated from the Claude Code command `/mine-rejections` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $mine-rejections -- Learning Loop

## Invocation

```
$mine-rejections last 30 days of closed-unmerged agent PRs in our main repo
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-operate:learning-loop`, `adlc-operate:agent-incident-review`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Collect
Gather rejected or abandoned agent PRs, repeated review comments, and early reverts.

### Step 2: Cluster and convert
Apply the **learning-loop** skill: root-cause clusters, then the cheapest durable artifact per cluster.

### Step 3: Escalate incidents
For anything that reached production, run **agent-incident-review**.

### Step 4: Output
Learning report with artifacts to ship, owners, and the metric to watch.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$codify` (in `adlc-context`; install it if needed): turn the top patterns into rules, hooks or tests
- `$init-agent-context` (in `adlc-context`; install it if needed): update the context file
