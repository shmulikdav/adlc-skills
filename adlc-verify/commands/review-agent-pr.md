---
description: Run an alignment review of an agent-authored PR or diff against its spec, with evidence-backed findings
argument-hint: "<PR link, branch, or diff> [spec path]"
---

# /review-agent-pr -- Alignment Review

## Invocation

```
/review-agent-pr feat/audit-export specs/012-audit-export/spec.md
```

## Workflow

### Step 1: Gather
Read $ARGUMENTS: the diff and the spec/ACs. Ask for the spec if missing; without it, review only passes 2–5 and say so.

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
