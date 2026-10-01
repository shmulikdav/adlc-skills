---
name: review-agent-pr
description: "Run the ADLC review-agent-pr workflow: run an alignment review of an agent-authored PR or diff against its spec, with evidence-backed findings. Use when the user invokes $review-agent-pr or asks for this workflow end to end."
---

> Generated from the Claude Code command `/review-agent-pr` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $review-agent-pr -- Alignment Review

## Invocation

```
$review-agent-pr feat/audit-export specs/012-audit-export/spec.md
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-verify:agent-code-review`, `adlc-verify:hallucination-checks`, `adlc-verify:definition-of-done`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Gather
Read the user's request: the diff and the spec/ACs. Ask for the spec if missing; without it, review only passes 2–5 and say so.

### Step 2: Independent context
Delegate to the **agent-output-reviewer** agent when available, so the review runs in a fresh context.

### Step 3: Review
Apply the **agent-code-review** skill's five passes.

### Step 4: Verify references
Apply **hallucination-checks** to new dependencies, APIs, config keys, and claims in the PR description.

### Step 5: DoD check
Compare against the **definition-of-done** checklist and list missing evidence.

### Step 6: Report
Verdict, coverage table, findings, missing evidence.
