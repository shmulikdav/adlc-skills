---
name: codify
description: "Use when the user invokes $codify, or asks to run the Codify Team Knowledge workflow from the adlc-context plugin end to end."
---

> Generated from the Claude Code command `/codify` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $codify -- Codify Team Knowledge

## Invocation

```
$codify The agent keeps using axios; we use our own httpClient wrapper with retries
$codify How we write database migrations
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-context:codify-conventions`, `adlc-context:agent-context-files`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Gather examples
From the user's request and the repo, collect 2–3 concrete examples of right and wrong behavior.

### Step 2: Choose the mechanism
Apply the **codify-conventions** skill's decision table and state the choice in one sentence.

### Step 3: Write the artifact
Context-file lines (**agent-context-files**), a skill, a hook config, or a test.

### Step 4: Verify
Provide a test prompt that should now produce the correct behavior, and how to check it.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$audit-skills`: check the library still earns its context
- `$init-agent-context`: if the rule belongs in the context file
