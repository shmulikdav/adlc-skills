---
description: Turn a recurring agent mistake or team convention into the right artifact — context line, skill, hook, or test
argument-hint: "<the convention or the mistake the agent keeps making>"
---

# /codify-convention -- Codify Team Knowledge

## Invocation

```
/codify-convention The agent keeps using axios; we use our own httpClient wrapper with retries
/codify-convention How we write database migrations
```

## Workflow

### Step 1: Gather examples
From $ARGUMENTS and the repo, collect 2–3 concrete examples of right and wrong behavior.

### Step 2: Choose the mechanism
Apply the **codify-conventions** skill's decision table and state the choice in one sentence.

### Step 3: Write the artifact
Context-file lines (**agent-context-files**), a skill, a hook config, or a test.

### Step 4: Verify
Provide a test prompt that should now produce the correct behavior, and how to check it.
