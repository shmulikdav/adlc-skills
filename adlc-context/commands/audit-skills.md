---
description: Audit an internal skills or plugin library — triggering, measured value, overlap, and what to keep, fix, or cut
argument-hint: "<path to skills/plugins, or list of installed plugins>"
---

# /audit-skills -- Skill Library Audit

## Invocation

```
/audit-skills .claude/skills
/audit-skills our internal plugin marketplace repo
```

## Workflow

Input: $ARGUMENTS

### Step 1: Inventory
List every skill with its description, size, owner if known, and any overlap with installed frameworks.

### Step 2: Review descriptions
Apply the authoring standards from the **skill-library-management** skill: trigger conditions vs workflow summaries, specificity, negative-trigger risk.

### Step 3: Evaluate
Propose 2–4 eval cases per skill. If eval results exist, read Δ per case; otherwise mark "unmeasured".

### Step 4: Decide
Keep / fix / cut per skill, with rewritten descriptions for every "fix". Note which items should become context-file lines, hooks, or tests instead (**codify-conventions**).

### Step 5: Output
Audit table, rewritten descriptions, eval cases to add.
