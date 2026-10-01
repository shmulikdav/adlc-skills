---
name: vet-extension
description: Security-vet a specific third-party skill, plugin, MCP server, or hook from its link or files. For a general safety question with no link, answer with the checklist directly instead of waiting for one.
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
Your first action must be a Skill tool call for each of these skills: `adlc-govern:extension-vetting`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Fetch and inventory
If no extension was given, apply the checklist and the install / restrict / reject rule as general guidance, then ask for the link. Otherwise read $ARGUMENTS, list every component and file, and do not install or execute anything.

### Step 2: Review
Apply the **extension-vetting** skill checklist. Delegate code-heavy components to the **security-reviewer** agent when available.

### Step 3: Verdict
Install / install with restrictions / reject, with evidence and approval conditions.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `/audit-skills` (in `adlc-context`; install it if needed): review the rest of the installed library
- `/governance-pack`: make the allowlist policy
