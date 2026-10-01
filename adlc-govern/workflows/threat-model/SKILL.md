---
name: threat-model
description: "Use when the user invokes $threat-model, or asks to run the Agentic Threat Model workflow from the adlc-govern plugin end to end."
---

> Generated from the Claude Code command `/threat-model` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $threat-model -- Agentic Threat Model

## Invocation

```
$threat-model Claude Code in CI with GitHub + Jira MCP, opens PRs, deploys to staging
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-govern:agentic-threat-model`, `adlc-govern:agent-permissions`, `adlc-govern:guardrail-hooks`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Scope
From the user's request, define agents, tools, credentials, data sources (flag untrusted content), outputs, and human gates. Ask for gaps.

### Step 2: Model
Apply the **agentic-threat-model** skill across ASI01–ASI10.

### Step 3: Controls
Translate gaps into concrete configuration using **agent-permissions** and **guardrail-hooks**.

### Step 4: Output
Risk register, top 5 actions, validation tests. Save as markdown.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$governance-pack`: turn the controls into policy, permissions and hooks
- `$vet-extension`: vet the plugins and MCP servers in use
- `$red-team-agent` (in `adlc-agent-engineering`; install it if needed): if you are shipping an agent product
