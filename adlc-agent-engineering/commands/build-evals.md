---
description: Create an eval suite for an agent or LLM feature with tasks, graders, thresholds, and CI wiring
argument-hint: "<agent/feature description, sample transcripts, or failure cases>"
---

# /build-evals -- Eval Suite

## Invocation

```
/build-evals [attach 30 real conversations and 5 known failures]
```

## Workflow

### Step 1: Gather cases
Collect tasks from $ARGUMENTS: real usage, known failures, acceptance criteria.

### Step 2: Design
Apply **eval-suite-design**: success criteria, grader per task, capability vs regression split, trials.

### Step 3: Write
Produce the task file (YAML/JSONL) and grader code or rubrics.

### Step 4: Wire
Propose CI integration and thresholds; link to **prompt-versioning** for the change gate.
