---
description: Blameless post-incident review for agent-caused failures that turns findings into durable fixes
argument-hint: "<incident description, transcripts, logs>"
---

# /agent-postmortem -- Agent Incident Review

## Invocation

```
/agent-postmortem The agent dropped a DB index during a refactor; checkout latency spiked for 40 minutes
```

## Workflow

### Step 1: Collect evidence
Read $ARGUMENTS and attachments (transcripts, logs, commits). Ask for missing evidence.

### Step 2: Review
Apply the **agent-incident-review** skill: timeline, impact, layer analysis, contributing factors.

### Step 3: Fixes
Turn each finding into a durable artifact with owner and due date; propose the regression test or eval case.

### Step 4: Output
Save `Postmortem-[title]-[date].md`.
