---
name: write-agentic-prd
description: Turn a feature idea or ticket into an Agentic PRD a coding agent can execute without guessing
argument-hint: "<feature idea, ticket text, or existing PRD>"
---

# /write-agentic-prd -- Agent Execution Spec

## Invocation

```
/write-agentic-prd Let account admins export audit logs as CSV, filtered by date and user
/write-agentic-prd [attach an existing PRD or paste a Jira ticket]
```

## Workflow

### Step 0: Load the method
Your first action must be a Skill tool call for each of these skills: `adlc-intent:spec-clarification`, `adlc-intent:agentic-prd`, `adlc-intent:acceptance-criteria`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Understand intent
Read $ARGUMENTS and attachments. If a repo is available, scan for related code, ADRs, and the context file (CLAUDE.md / AGENTS.md).

### Step 2: Clarify
Apply the **spec-clarification** skill. Ask the blocking questions (max 5). Record defaults for the rest as labeled assumptions.

### Step 3: Draft
Apply the **agentic-prd** skill to fill the full template.

### Step 4: Acceptance criteria
Apply the **acceptance-criteria** skill so every requirement has testable criteria and a verification method.

### Step 5: Self-check and save
Run the agentic-prd self-check (no orphan requirements, no unquantified adjectives, stop conditions present). Save as `AgentSpec-[feature]-[date].md`.

### Step 6: Offer next steps
- "Want me to break this into agent-sized tasks?"
- "Should I derive the test suite from these acceptance criteria?"
