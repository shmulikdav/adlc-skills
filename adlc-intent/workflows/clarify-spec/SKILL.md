---
name: clarify-spec
description: "Use when the user invokes $clarify-spec, or asks to run the Spec Ambiguity Hunt workflow from the adlc-intent plugin end to end."
---

> Generated from the Claude Code command `/clarify-spec` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $clarify-spec -- Spec Ambiguity Hunt

## Invocation

```
$clarify-spec [attach spec.md]
$clarify-spec interview me — feature: bulk user import
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-intent:spec-clarification`, `adlc-intent:acceptance-criteria`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Read and model
Read the user's request. Build the actors/entities/states model. If a repo is present, check code for answers first.

### Step 2: Hunt
Apply the **spec-clarification** skill across all categories.

### Step 3: Prioritize and ask
Present the question table (Blocking → Important → Minor) with recommended defaults. In "interview me" mode, ask one question at a time.

### Step 4: Update
Apply answers to the spec, add a dated Clarifications section, and re-check acceptance criteria with the **acceptance-criteria** skill.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- Continue here: Want me to turn the clarified spec into tasks?
- `$write-agentic-prd`: write the spec from the answers
- `$spec-feature`: run the full spec-driven flow
