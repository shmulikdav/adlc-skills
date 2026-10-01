---
name: plan-continuous-ai
description: "Use when the user invokes $plan-continuous-ai, or asks to run the Background Agent Workflows workflow from the adlc-operate plugin end to end."
---

> Generated from the Claude Code command `/plan-continuous-ai` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $plan-continuous-ai -- Background Agent Workflows

## Invocation

```
$plan-continuous-ai Monorepo, flaky CI, 60 new issues/week, docs always stale
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-operate:continuous-ai-workflows`, `adlc-operate:agentops-observability`, `adlc-operate:ai-cost-management`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Toil inventory
List repetitive repository work and rank it per the **continuous-ai-workflows** skill.

### Step 2: Select and specify
Pick one or two starter workflows; define trigger, output, permissions, guardrails, owner, and success metric.

### Step 3: Observe and budget
Apply **agentops-observability** for traces and alerts, and **ai-cost-management** for per-run budgets.

### Step 4: Output
Workflow catalogue and a two-week shadow-mode rollout plan.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$governance-pack` (in `adlc-govern`; install it if needed): permissions for background agents
- `$fix-review-queue` (in `adlc-verify`; install it if needed): keep agent output reviewable
- `$release-check`: gate what the workflows ship
