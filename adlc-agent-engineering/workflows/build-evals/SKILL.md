---
name: build-evals
description: "Run the ADLC build-evals workflow: create an eval suite for an agent or LLM feature with tasks, graders, thresholds, and CI wiring. Use when the user invokes $build-evals or asks for this workflow end to end."
---

> Generated from the Claude Code command `/build-evals` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $build-evals -- Eval Suite

## Invocation

```
$build-evals [attach 30 real conversations and 5 known failures]
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-agent-engineering:eval-suite-design`, `adlc-agent-engineering:prompt-versioning`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Gather cases
Collect tasks from the user's request: real usage, known failures, acceptance criteria.

### Step 2: Design
Apply **eval-suite-design**: success criteria, grader per task, capability vs regression split, trials.

### Step 3: Write
Produce the task file (YAML/JSONL) and grader code or rubrics.

### Step 4: Wire
Propose CI integration and thresholds; link to **prompt-versioning** for the change gate.
