---
name: release-check
description: "Run the ADLC release-check workflow: run a go/no-go release check for agent-built changes with gate evidence and rollback readiness. Use when the user invokes $release-check or asks for this workflow end to end."
---

> Generated from the Claude Code command `/release-check` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $release-check -- Go/No-Go for Agentic Changes

## Invocation

```
$release-check v2.14 — includes agent-built audit export and a billing migration
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-operate:release-gates`, `adlc-operate:agentops-observability`, `adlc-operate:ai-cost-management`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Classify
List changes in the user's request and assign change classes per the **release-gates** skill.

### Step 2: Gate evidence
For each change, check G1–G3 evidence; list what is missing.

### Step 3: Observability and cost
Confirm monitors and alerts per **agentops-observability**; for AI features, confirm cost alerts per **ai-cost-management**.

### Step 4: Decision
Go / Go with conditions / No-go, with rollout plan and rollback triggers.
