---
name: agent-postmortem
description: "Use when the user invokes $agent-postmortem, or asks to run the Agent Incident Review workflow from the adlc-operate plugin end to end."
---

> Generated from the Claude Code command `/agent-postmortem` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $agent-postmortem -- Agent Incident Review

## Invocation

```
$agent-postmortem The agent dropped a DB index during a refactor; checkout latency spiked for 40 minutes
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-operate:agent-incident-review`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Collect evidence
Read the user's request and attachments (transcripts, logs, commits). Ask for missing evidence.

### Step 2: Review
Apply the **agent-incident-review** skill: timeline, impact, layer analysis, contributing factors.

### Step 3: Fixes
Turn each finding into a durable artifact with owner and due date; propose the regression test or eval case.

### Step 4: Output
Save `Postmortem-[title]-[date].md`.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$codify` (in `adlc-context`; install it if needed): make the fix permanent
- `$threat-model` (in `adlc-govern`; install it if needed): if it exposed a security gap
- `$mine-rejections`: look for the same pattern elsewhere
