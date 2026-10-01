---
name: verify-change
description: "Use when the user invokes $verify-change, or asks to run the Definition of Done Check workflow from the adlc-verify plugin end to end."
---

> Generated from the Claude Code command `/verify-change` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $verify-change -- Definition of Done Check

## Invocation

```
$verify-change
$verify-change T-07
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-verify:definition-of-done`, `adlc-verify:hallucination-checks`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Load the DoD
Use the team's Definition of Done if present (context file or docs); otherwise apply the **definition-of-done** template.

### Step 2: Run checks
Execute every automatable item (tests, type check, lint, dependency verification via **hallucination-checks**) and capture output.

### Step 3: Report
Checklist with evidence per item; list human gates still required. Do not mark anything verified without output to show.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$review-agent-pr`: hand to human review with the evidence
- `$release-check` (in `adlc-operate`; install it if needed): if it is ready to ship
