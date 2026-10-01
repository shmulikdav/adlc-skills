---
name: map-to-adlc
description: Map your current SDLC workflow to the Agentic Development Lifecycle and pick where agents should enter first
argument-hint: "<description of the current dev workflow>"
---

# /map-to-adlc -- SDLC → ADLC Workflow Mapping

## Invocation

```
/map-to-adlc Jira ticket → PM writes spec in Confluence → dev implements → PR review → QA manual test → weekly release
```

## Workflow

### Step 0: Load the method
Your first action must be a Skill tool call for each of these skills: `adlc-foundations:sdlc-to-adlc-mapping`, `adlc-foundations:autonomy-levels`, `adlc-foundations:role-transitions`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Capture the current flow
From $ARGUMENTS, list every step with owner, input, output artifact, tool, and pain point. Ask for missing steps (especially review, QA, and release).

### Step 2: Map
Apply the **sdlc-to-adlc-mapping** skill to produce the full mapping table (executor, new artifact, human gate kept, new failure mode, guardrail).

### Step 3: Set autonomy
Apply the **autonomy-levels** skill to each step where an agent becomes the executor.

### Step 4: Role impact
Apply the **role-transitions** skill for the roles that appear in the flow.

### Step 5: Output
Mapping table, ranked top-3 entry points, autonomy table, and role-impact summary. Save as markdown.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- Continue here: Want me to write the first feature as an agent-ready spec?
- Continue here: Should I set up the repo context files for the pilot team?
- `/adlc-roadmap`: sequence the changes
- `/spec-feature` (in `adlc-intent`; install it if needed): pilot the new intent stage on one feature
- `/choose-rail` (in `adlc-build`; install it if needed): pick the execution framework
