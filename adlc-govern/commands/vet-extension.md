---
description: Security-vet a third-party skill, plugin, MCP server, or hook before installing it
argument-hint: "<repo URL, local path, or package name>"
---

# /vet-extension -- Extension Vetting

## Invocation

```
/vet-extension someorg/some-claude-plugin
/vet-extension ./downloads/cool-skill/
```

## Workflow

### Step 0: Load the method
Before anything else, load each skill this command uses with the Skill tool: `adlc-govern:extension-vetting`. The answer must follow those skills' rubrics, templates and defaults, not general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Fetch and inventory
Read $ARGUMENTS. List every component and file. Do not install or execute anything.

### Step 2: Review
Apply the **extension-vetting** skill checklist. Delegate code-heavy components to the **security-reviewer** agent when available.

### Step 3: Verdict
Install / install with restrictions / reject, with evidence and approval conditions.
