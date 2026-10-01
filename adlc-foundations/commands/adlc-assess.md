---
description: Assess a team's readiness for the Agentic Development Lifecycle and get a maturity level, gaps, and first moves
argument-hint: "<team or org description, current tools, delivery metrics>"
---

# /adlc-assess -- ADLC Readiness Assessment

Baseline where a team stands before scaling coding agents.

## Invocation

```
/adlc-assess Platform team, 9 engineers, Claude Code licences for all, deploy weekly, 45% test coverage
/adlc-assess [attach engineering survey results or a process doc]
```

## Workflow

### Step 1: Collect context
Read $ARGUMENTS and any attached files. Ask, in a single message, only for the missing inputs listed in the **adlc-readiness-assessment** skill.

### Step 2: Score
Apply the **adlc-readiness-assessment** skill: score the seven DORA AI capabilities and the five agent-specific dimensions, with evidence for each score.

### Step 3: Calibrate autonomy
Apply the **autonomy-levels** skill to the team's top 5 recurring task types to show what can be delegated today.

### Step 4: Measurement baseline
Apply the **adlc-metrics** skill to define the minimum baseline the team must capture before the rollout.

### Step 4b: Comprehension check
Apply the **comprehension-debt** skill's assessment to the team's critical modules.

### Step 5: Report
Produce the readiness report (maturity level, scorecard, top constraints, first three moves, what not to do yet) and the autonomy table. Save as markdown.

### Step 6: Offer next steps
- "Want me to map your current workflow to the ADLC step by step?"
- "Should I draft your AI stance policy?"
- "Want a 90-day ADLC roadmap from these findings?"
