---
description: Design an AI agent or LLM feature — pick the simplest working pattern, tools, guardrails, and eval plan
argument-hint: "<what the agent should accomplish, users, systems it touches>"
---

# /design-agent -- Agent Design

## Invocation

```
/design-agent Support agent that reads tickets, checks order status in our API, and drafts refunds under $50
```

## Workflow

Input: $ARGUMENTS

### Step 0: Load the method
Before anything else, load each skill this command uses with the Skill tool: `adlc-agent-engineering:agent-architecture`, `adlc-agent-engineering:tool-design`, `adlc-agent-engineering:agent-runtime-guardrails`, `adlc-agent-engineering:eval-suite-design`, `adlc-agent-engineering:prompt-versioning`. The answer must follow those skills' rubrics, templates and defaults, not general knowledge. If a skill fails to load, say so in the first line of the answer.

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
