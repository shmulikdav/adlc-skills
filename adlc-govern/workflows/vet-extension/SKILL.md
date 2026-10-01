---
name: vet-extension
description: "Use when the user invokes $vet-extension, or asks to run the Extension Vetting workflow from the adlc-govern plugin end to end."
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
If no extension was given, apply the checklist and the install / restrict / reject rule as general guidance, then ask for the link. Otherwise read the user's request, list every component and file, and do not install or execute anything.

### Step 2: Review
Apply the **extension-vetting** skill checklist. Delegate code-heavy components to the **security-reviewer** agent when available.

### Step 3: Verdict
Install / install with restrictions / reject, with evidence and approval conditions.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$audit-skills` (in `adlc-context`; install it if needed): review the rest of the installed library
- `$governance-pack`: make the allowlist policy
