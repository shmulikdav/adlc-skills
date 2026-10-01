---
description: Produce an ADLC governance pack — permissions, hooks, threat model, and compliance mapping — for a team or org
argument-hint: "<org/team context, frameworks of interest>"
---

# /governance-pack -- ADLC Governance Pack

## Invocation

```
/governance-pack Fintech, 40 engineers, Claude Code + Cursor, SOC 2 and ISO 42001 target
```

## Workflow

### Step 1: Context
Gather tools in use, data sensitivity, regulatory scope, and existing policies from $ARGUMENTS.

### Step 2: Threat model
Apply **agentic-threat-model** for the development setup.

### Step 3: Permissions profiles
Apply **agent-permissions** for local, CI, and review-only profiles.

### Step 4: Guardrails
Apply **guardrail-hooks** for the must-never-happen rules.

### Step 5: Compliance mapping
Apply **ai-compliance-mapping** for the frameworks in scope and list the evidence pack.

### Step 6: Output
A single governance document with sections for each step plus an owner/cadence table. Flag items needing legal review.
