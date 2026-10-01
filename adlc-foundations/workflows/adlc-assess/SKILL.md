---
name: adlc-assess
description: "Run the ADLC adlc-assess workflow: assess a team's readiness for the Agentic Development Lifecycle and get a maturity level, gaps, and first moves. Use when the user invokes $adlc-assess or asks for this workflow end to end."
---

> Generated from the Claude Code command `/adlc-assess` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $adlc-assess -- ADLC Readiness Assessment

Baseline where a team stands before scaling coding agents.

## Invocation

```
$adlc-assess Platform team, 9 engineers, Claude Code licences for all, deploy weekly, 45% test coverage
$adlc-assess [attach engineering survey results or a process doc]
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-foundations:adlc-readiness-assessment`, `adlc-foundations:autonomy-levels`, `adlc-foundations:adlc-metrics`, `adlc-foundations:comprehension-debt`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Collect context
Read the user's request and any attached files. Ask, in a single message, only for the missing inputs listed in the **adlc-readiness-assessment** skill.

### Step 2: Score
Apply the **adlc-readiness-assessment** skill: score all 15 dimensions (the seven DORA AI capabilities and the eight agent-specific dimensions), with evidence for each score; mark anything unknown as unknown rather than guessing.

### Step 3: Calibrate autonomy
Apply the **autonomy-levels** skill to the team's top 5 recurring task types to show what can be delegated today.

### Step 4: Measurement baseline
Apply the **adlc-metrics** skill to define the minimum baseline the team must capture before the rollout.

### Step 4b: Comprehension check
Apply the **comprehension-debt** skill's assessment to the team's critical modules.

### Step 5: Report
Produce the readiness report (maturity level, scorecard, top constraints, first three moves, what not to do yet) and the autonomy table. Save as markdown.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- Continue here: Want me to map your current workflow to the ADLC step by step?
- Continue here: Should I draft your AI stance policy?
- Continue here: Want a 90-day ADLC roadmap from these findings?
- `$adlc-roadmap`: turn the gaps into a 90-day plan
- `$fix-review-queue` (in `adlc-verify`; install it if needed): if review capacity is the top constraint
- `$governance-pack` (in `adlc-govern`; install it if needed): if there is no written AI policy
