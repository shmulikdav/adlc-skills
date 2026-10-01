---
name: map-to-adlc
description: "Run the ADLC map-to-adlc workflow: map your current SDLC workflow to the Agentic Development Lifecycle and pick where agents should enter first. Use when the user invokes $map-to-adlc or asks for this workflow end to end."
---

> Generated from the Claude Code command `/map-to-adlc` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $map-to-adlc -- SDLC → ADLC Workflow Mapping

## Invocation

```
$map-to-adlc Jira ticket → PM writes spec in Confluence → dev implements → PR review → QA manual test → weekly release
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-foundations:sdlc-to-adlc-mapping`, `adlc-foundations:autonomy-levels`, `adlc-foundations:role-transitions`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Capture the current flow
From the user's request, list every step with owner, input, output artifact, tool, and pain point. Ask for missing steps (especially review, QA, and release).

### Step 2: Map
Apply the **sdlc-to-adlc-mapping** skill to produce the full mapping table (executor, new artifact, human gate kept, new failure mode, guardrail).

### Step 3: Set autonomy
Apply the **autonomy-levels** skill to each step where an agent becomes the executor.

### Step 4: Role impact
Apply the **role-transitions** skill for the roles that appear in the flow.

### Step 5: Output
Mapping table, ranked top-3 entry points, autonomy table, and role-impact summary. Save as markdown.

### Step 6: Offer next steps
- "Want me to write the first feature as an agent-ready spec?"
- "Should I set up the repo context files for the pilot team?"
