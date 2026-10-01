---
name: write-agentic-prd
description: "Use when the user invokes $write-agentic-prd, or asks to run the Agent Execution Spec workflow from the adlc-intent plugin end to end."
---

> Generated from the Claude Code command `/write-agentic-prd` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $write-agentic-prd -- Agent Execution Spec

## Invocation

```
$write-agentic-prd Let account admins export audit logs as CSV, filtered by date and user
$write-agentic-prd [attach an existing PRD or paste a Jira ticket]
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-intent:spec-clarification`, `adlc-intent:agentic-prd`, `adlc-intent:acceptance-criteria`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Understand intent
Read the user's request and attachments. If a repo is available, scan for related code, ADRs, and the context file (CLAUDE.md / AGENTS.md).

### Step 2: Clarify
Apply the **spec-clarification** skill. Ask the blocking questions (max 5). Record defaults for the rest as labeled assumptions.

### Step 3: Draft
Apply the **agentic-prd** skill to fill the full template.

### Step 4: Acceptance criteria
Apply the **acceptance-criteria** skill so every requirement has testable criteria and a verification method.

### Step 5: Self-check and save
Run the agentic-prd self-check (no orphan requirements, no unquantified adjectives, stop conditions present). Save as `AgentSpec-[feature]-[date].md`.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- Continue here: Want me to break this into agent-sized tasks?
- Continue here: Should I derive the test suite from these acceptance criteria?
- `$clarify-spec`: if open questions remain
- `$derive-tests` (in `adlc-verify`; install it if needed): turn the acceptance criteria into tests
- `$plan-long-run` (in `adlc-build`; install it if needed): if the work will run for hours
