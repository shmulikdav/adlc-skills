---
name: vet-extension
description: "Run the ADLC vet-extension workflow: security-vet a third-party skill, plugin, MCP server, or hook before installing it. Use when the user invokes $vet-extension or asks for this workflow end to end."
---

> Generated from the Claude Code command `/vet-extension` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $vet-extension -- Extension Vetting

## Invocation

```
$vet-extension someorg/some-claude-plugin
$vet-extension ./downloads/cool-skill/
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-govern:extension-vetting`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Fetch and inventory
Read the user's request. List every component and file. Do not install or execute anything.

### Step 2: Review
Apply the **extension-vetting** skill checklist. Delegate code-heavy components to the **security-reviewer** agent when available.

### Step 3: Verdict
Install / install with restrictions / reject, with evidence and approval conditions.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$audit-skills` (in `adlc-context`; install it if needed): review the rest of the installed library
- `$governance-pack`: make the allowlist policy
