---
description: Hunt for ambiguities, contradictions, and silent decisions in a spec before an agent builds it
argument-hint: "<spec, PRD, or ticket>"
---

# /clarify-spec -- Spec Ambiguity Hunt

## Invocation

```
/clarify-spec [attach spec.md]
/clarify-spec interview me — feature: bulk user import
```

## Workflow

### Step 0: Load the method
Before anything else, load each skill this command uses with the Skill tool: `adlc-intent:spec-clarification`, `adlc-intent:acceptance-criteria`. The answer must follow those skills' rubrics, templates and defaults, not general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Read and model
Read $ARGUMENTS. Build the actors/entities/states model. If a repo is present, check code for answers first.

### Step 2: Hunt
Apply the **spec-clarification** skill across all categories.

### Step 3: Prioritize and ask
Present the question table (Blocking → Important → Minor) with recommended defaults. In "interview me" mode, ask one question at a time.

### Step 4: Update
Apply answers to the spec, add a dated Clarifications section, and re-check acceptance criteria with the **acceptance-criteria** skill.

### Step 5: Offer next steps
- "Want me to turn the clarified spec into tasks?"
