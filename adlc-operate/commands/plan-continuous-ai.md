---
description: Choose and guardrail background agent workflows (triage, CI failure investigation, docs, test gaps, cleanup) for a repository
argument-hint: "<repo or team context, current toil>"
---

# /plan-continuous-ai -- Background Agent Workflows

## Invocation

```
/plan-continuous-ai Monorepo, flaky CI, 60 new issues/week, docs always stale
```

## Workflow

Input: $ARGUMENTS

### Step 1: Toil inventory
List repetitive repository work and rank it per the **continuous-ai-workflows** skill.

### Step 2: Select and specify
Pick one or two starter workflows; define trigger, output, permissions, guardrails, owner, and success metric.

### Step 3: Observe and budget
Apply **agentops-observability** for traces and alerts, and **ai-cost-management** for per-run budgets.

### Step 4: Output
Workflow catalogue and a two-week shadow-mode rollout plan.
