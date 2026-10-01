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

### Step 1: Fetch and inventory
Read $ARGUMENTS. List every component and file. Do not install or execute anything.

### Step 2: Review
Apply the **extension-vetting** skill checklist. Delegate code-heavy components to the **security-reviewer** agent when available.

### Step 3: Verdict
Install / install with restrictions / reject, with evidence and approval conditions.
