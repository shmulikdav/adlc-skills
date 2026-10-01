---
description: Run a go/no-go release check for agent-built changes with gate evidence and rollback readiness
argument-hint: "<release, PR list, or change description>"
---

# /release-check -- Go/No-Go for Agentic Changes

## Invocation

```
/release-check v2.14 — includes agent-built audit export and a billing migration
```

## Workflow

### Step 0: Load the method
Before anything else, load each skill this command uses with the Skill tool: `adlc-operate:release-gates`, `adlc-operate:agentops-observability`, `adlc-operate:ai-cost-management`. The answer must follow those skills' rubrics, templates and defaults, not general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Classify
List changes in $ARGUMENTS and assign change classes per the **release-gates** skill.

### Step 2: Gate evidence
For each change, check G1–G3 evidence; list what is missing.

### Step 3: Observability and cost
Confirm monitors and alerts per **agentops-observability**; for AI features, confirm cost alerts per **ai-cost-management**.

### Step 4: Decision
Go / Go with conditions / No-go, with rollout plan and rollback triggers.
