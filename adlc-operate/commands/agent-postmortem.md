---
name: agent-postmortem
description: Blameless post-incident review for agent-caused failures that turns findings into durable fixes
argument-hint: "<incident description, transcripts, logs>"
---

# /agent-postmortem -- Agent Incident Review

## Invocation

```
/agent-postmortem The agent dropped a DB index during a refactor; checkout latency spiked for 40 minutes
```

## Workflow

### Step 0: Load the method
Your first action must be a Skill tool call for each of these skills: `adlc-operate:agent-incident-review`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Collect evidence
Read $ARGUMENTS and attachments (transcripts, logs, commits). Ask for missing evidence.

### Step 2: Review
Apply the **agent-incident-review** skill: timeline, impact, layer analysis, contributing factors.

### Step 3: Fixes
Turn each finding into a durable artifact with owner and due date; propose the regression test or eval case.

### Step 4: Output
Save `Postmortem-[title]-[date].md`.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `/codify` (in `adlc-context`; install it if needed): make the fix permanent
- `/threat-model` (in `adlc-govern`; install it if needed): if it exposed a security gap
- `/mine-rejections`: look for the same pattern elsewhere
