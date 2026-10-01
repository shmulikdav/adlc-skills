---
name: audit-skills
description: "Use when the user invokes $audit-skills, or asks to run the Skill Library Audit workflow from the adlc-context plugin end to end."
---

> Generated from the Claude Code command `/audit-skills` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $audit-skills -- Skill Library Audit

## Invocation

```
$audit-skills .claude/skills
$audit-skills our internal plugin marketplace repo
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-context:skill-library-management`, `adlc-context:codify-conventions`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

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

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$vet-extension` (in `adlc-govern`; install it if needed): vet any third-party skill or plugin you keep
- `$codify`: replace a weak skill with a hook or test
