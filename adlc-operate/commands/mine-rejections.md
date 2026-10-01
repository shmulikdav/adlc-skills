---
description: Turn rejected agent PRs and repeated review comments into durable fixes — context, skills, hooks, tests, evals
argument-hint: "<rejected PR list, review comments, or a time window>"
---

# /mine-rejections -- Learning Loop

## Invocation

```
/mine-rejections last 30 days of closed-unmerged agent PRs in our main repo
```

## Workflow

Input: $ARGUMENTS

### Step 0: Load the method
Your first action must be a Skill tool call for each of these skills: `adlc-operate:learning-loop`, `adlc-operate:agent-incident-review`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Collect
Gather rejected or abandoned agent PRs, repeated review comments, and early reverts.

### Step 2: Cluster and convert
Apply the **learning-loop** skill: root-cause clusters, then the cheapest durable artifact per cluster.

### Step 3: Escalate incidents
For anything that reached production, run **agent-incident-review**.

### Step 4: Output
Learning report with artifacts to ship, owners, and the metric to watch.
