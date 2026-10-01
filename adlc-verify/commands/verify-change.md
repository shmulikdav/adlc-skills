---
description: Verify a change meets the Definition of Done with evidence before it is called done
argument-hint: "[branch or task ID]"
---

# /verify-change -- Definition of Done Check

## Invocation

```
/verify-change
/verify-change T-07
```

## Workflow

Input: $ARGUMENTS

### Step 0: Load the method
Before anything else, load each skill this command uses with the Skill tool: `adlc-verify:definition-of-done`, `adlc-verify:hallucination-checks`. The answer must follow those skills' rubrics, templates and defaults, not general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Load the DoD
Use the team's Definition of Done if present (context file or docs); otherwise apply the **definition-of-done** template.

### Step 2: Run checks
Execute every automatable item (tests, type check, lint, dependency verification via **hallucination-checks**) and capture output.

### Step 3: Report
Checklist with evidence per item; list human gates still required. Do not mark anything verified without output to show.
