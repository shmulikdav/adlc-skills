---
description: Threat-model an agentic development setup or an agent product against the OWASP Agentic Top 10
argument-hint: "<system description: agents, tools/MCP servers, credentials, data sources, outputs>"
---

# /threat-model -- Agentic Threat Model

## Invocation

```
/threat-model Claude Code in CI with GitHub + Jira MCP, opens PRs, deploys to staging
```

## Workflow

### Step 1: Scope
From $ARGUMENTS, define agents, tools, credentials, data sources (flag untrusted content), outputs, and human gates. Ask for gaps.

### Step 2: Model
Apply the **agentic-threat-model** skill across ASI01–ASI10.

### Step 3: Controls
Translate gaps into concrete configuration using **agent-permissions** and **guardrail-hooks**.

### Step 4: Output
Risk register, top 5 actions, validation tests. Save as markdown.
