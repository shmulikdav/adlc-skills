---
name: design-agent
description: "Run the ADLC design-agent workflow: design an AI agent or LLM feature — pick the simplest working pattern, tools, guardrails, and eval plan. Use when the user invokes $design-agent or asks for this workflow end to end."
---

> Generated from the Claude Code command `/design-agent` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $design-agent -- Agent Design

## Invocation

```
$design-agent Support agent that reads tickets, checks order status in our API, and drafts refunds under $50
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-agent-engineering:agent-architecture`, `adlc-agent-engineering:tool-design`, `adlc-agent-engineering:agent-runtime-guardrails`, `adlc-agent-engineering:eval-suite-design`, `adlc-agent-engineering:prompt-versioning`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Architecture
Apply **agent-architecture**: choose the simplest pattern on the ladder and justify it.

### Step 2: Tools
Apply **tool-design** to define the minimal tool set with specs.

### Step 3: Guardrails
Apply **agent-runtime-guardrails**, including the approval matrix for high-impact actions.

### Step 4: Evals
Apply **eval-suite-design** for a starter suite of 20–50 tasks.

### Step 5: Change process
Apply **prompt-versioning** for how prompts and models will be versioned and released.

### Step 6: Output
Single design doc with a mermaid diagram. Save as `AgentDesign-[name]-[date].md`.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$build-evals`: define how you will measure it
- `$red-team-agent`: attack it before users do
- `$threat-model` (in `adlc-govern`; install it if needed): map the agent's risks
