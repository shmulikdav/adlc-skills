---
name: init-agent-context
description: Create or audit the agent context file (CLAUDE.md / AGENTS.md) for a repository
argument-hint: "<create | audit> [repo path or notes]"
---

# /init-agent-context -- Agent Context Setup

## Invocation

```
/init-agent-context create
/init-agent-context audit — our CLAUDE.md is 600 lines and Claude ignores half of it
```

## Workflow

### Step 0: Load the method
Your first action must be a Skill tool call for each of these skills: `adlc-context:agent-context-files`, `adlc-context:context-budget`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Determine mode
`create` if no context file exists, otherwise `audit` (or as stated in $ARGUMENTS).

### Step 2: Survey the repo
Read build files, CI config, test setup, folder structure, README, and existing rule files (CLAUDE.md, AGENTS.md, .cursor/rules, .github/copilot-instructions.md).

### Step 3: Write or audit
Apply the **agent-context-files** skill in the chosen mode.

### Step 4: Budget check
Apply the **context-budget** skill: move anything rarely needed into skills, nested files, or linked docs.

### Step 5: Output
The new or revised file (with a diff summary in audit mode) and a list of conventions that should become hooks, tests, or skills instead.

### Step 6: Offer next steps
- "Want me to turn the top recurring mistake into a skill or hook?"
- "Should I generate a codebase map and link it?"
