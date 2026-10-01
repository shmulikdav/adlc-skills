---
name: spec-feature
description: Run the full spec-driven loop for a feature — constitution check, spec, clarify, plan, tasks — before any code is written
argument-hint: "<feature description>"
---

# /spec-feature -- Spec-Driven Feature Kickoff

## Invocation

```
/spec-feature Real-time notifications for order status changes
```

## Workflow

Input: $ARGUMENTS

### Step 0: Load the method
Your first action must be a Skill tool call for each of these skills: `adlc-intent:spec-driven-development`, `adlc-intent:agentic-prd`, `adlc-intent:spec-clarification`, `adlc-intent:acceptance-criteria`, `adlc-intent:architecture-guardrails`, `adlc-intent:task-decomposition`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Detect conventions
Apply the **spec-driven-development** skill's toolchain detection (Spec Kit, Kiro, AI-DLC, or plain `specs/`). Load or draft the constitution.

### Step 2: Specify
Write `spec.md` (what and why, no tech) using the **agentic-prd** skill's intent, scope, scenarios, and requirements sections.

### Step 3: Clarify — GATE
Apply **spec-clarification**. Stop and wait for the user's answers to blocking questions.

### Step 4: Acceptance criteria
Apply **acceptance-criteria** to every requirement.

### Step 5: Plan — GATE
Draft `plan.md` with a constitution compliance check and the relevant architecture decisions and invariants (**architecture-guardrails**). Stop for approval.

### Step 6: Tasks
Apply **task-decomposition** to produce `tasks.md` with parallel markers and an AC coverage table.

### Step 7: Summary
List artifacts created, gates approved, and gates pending.

### Step 8: Offer next steps
- "Ready to implement task by task?"
- "Want me to identify which tasks can run in parallel agents?"
