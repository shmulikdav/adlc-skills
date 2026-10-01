---
name: red-team-agent
description: "Run the ADLC red-team-agent workflow: red-team an agent design or running agent against the OWASP Agentic Top 10 and turn findings into guardrails and eval cases. Use when the user invokes $red-team-agent or asks for this workflow end to end."
---

> Generated from the Claude Code command `/red-team-agent` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $red-team-agent -- Agent Red Team

## Invocation

```
$red-team-agent AgentDesign-support-agent.md
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-agent-engineering:agent-runtime-guardrails`, `adlc-agent-engineering:eval-suite-design`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Map the attack surface
Tools, credentials, untrusted inputs, memory, outputs, other agents.

### Step 2: Generate attack scenarios
For each relevant OWASP Agentic risk (ASI01–ASI10), write concrete scenarios (e.g., injected instructions in a ticket body asking for a refund to a new account).

### Step 3: Evaluate defenses
Check each scenario against the current design or behavior; mark blocked / partially blocked / not blocked.

### Step 4: Fix and regress
Propose controls with **agent-runtime-guardrails**; add each scenario as a regression case via **eval-suite-design**.

### Step 5: Output
Scenario table with results, control changes, and new eval cases. Only test systems you own or are authorized to test.
