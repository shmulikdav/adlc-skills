---
name: init-agent-context
description: "Use when the user invokes $init-agent-context, or asks to run the Agent Context Setup workflow from the adlc-context plugin end to end."
---

> Generated from the Claude Code command `/init-agent-context` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $init-agent-context -- Agent Context Setup

## Invocation

```
$init-agent-context create
$init-agent-context audit — our CLAUDE.md is 600 lines and Claude ignores half of it
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-context:agent-context-files`, `adlc-context:context-budget`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Determine mode
`create` if no context file exists, otherwise `audit` (or as stated in the user's request).

### Step 2: Survey the repo
Read build files, CI config, test setup, folder structure, README, and existing rule files (CLAUDE.md, AGENTS.md, .cursor/rules, .github/copilot-instructions.md).

### Step 3: Write or audit
Apply the **agent-context-files** skill in the chosen mode.

### Step 4: Budget check
Apply the **context-budget** skill: move anything rarely needed into skills, nested files, or linked docs.

### Step 5: Output
The new or revised file (with a diff summary in audit mode) and a list of conventions that should become hooks, tests, or skills instead.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- Continue here: Want me to turn the top recurring mistake into a skill or hook?
- Continue here: Should I generate a codebase map and link it?
- `$map-codebase`: add an architecture map the agent can use
- `$codify`: turn recurring corrections into rules or hooks
- `$audit-skills`: review the skills already installed
