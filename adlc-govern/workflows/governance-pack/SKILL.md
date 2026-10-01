---
name: governance-pack
description: "Use when the user invokes $governance-pack, or asks to run the ADLC Governance Pack workflow from the adlc-govern plugin end to end."
---

> Generated from the Claude Code command `/governance-pack` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $governance-pack -- ADLC Governance Pack

## Invocation

```
$governance-pack Fintech, 40 engineers, Claude Code + Cursor, SOC 2 and ISO 42001 target
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-govern:agentic-threat-model`, `adlc-govern:agent-permissions`, `adlc-govern:guardrail-hooks`, `adlc-govern:ai-compliance-mapping`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Context
Gather tools in use, data sensitivity, regulatory scope, and existing policies from the user's request.

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

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$threat-model`: if you haven't mapped the threats yet
- `$vet-extension`: approve the extension allowlist
- `$citizen-builder-policy`: if non-engineers are building too
