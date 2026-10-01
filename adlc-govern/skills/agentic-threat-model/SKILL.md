---
name: agentic-threat-model
description: "Use when assessing the security of coding agents, MCP connections, CI agents, or an AI agent being built, preparing a security review of an agentic setup, or when a team asks what could go wrong if an agent is manipulated."
---

# Agentic Threat Model

## Purpose

Agents act, not just answer. Every tool, credential, data source, and memory store an agent touches extends the attack surface. This skill produces a threat model in the shared vocabulary security teams now use.

## Scope first

Define the system: which agents, which tools/MCP servers, which credentials, which data sources (and which contain untrusted text), where outputs go (repo, CI, prod, external messages), and where humans approve.

Draw (or describe) trust boundaries: user ↔ agent, agent ↔ tools, agent ↔ untrusted content, agent ↔ agent, agent ↔ production.

## OWASP Agentic Top 10 (2026) walk-through

For each, ask the questions and record exposure and controls:

| ID | Risk | Key questions for this system |
|----|------|-------------------------------|
| ASI01 | Agent goal hijack | Can untrusted content (issues, web pages, docs, emails, code comments) redirect the agent? |
| ASI02 | Tool misuse & exploitation | Can a legitimate tool be used destructively within its permissions? |
| ASI03 | Identity & privilege abuse | Whose credentials does the agent use? Are they scoped and short-lived? |
| ASI04 | Agentic supply chain | Which MCP servers, skills, plugins, packages, and models are trusted, and how were they vetted? |
| ASI05 | Unexpected code execution | Can the agent run generated code outside a sandbox? |
| ASI06 | Memory & context poisoning | Can persisted memory, context files, or RAG sources be altered to influence future runs? |
| ASI07 | Insecure inter-agent communication | Are messages between agents authenticated and validated? |
| ASI08 | Cascading failures | Can one agent's error propagate through automated chains without a breaker? |
| ASI09 | Human-agent trust exploitation | Could a confident agent output lead a human to approve something harmful? |
| ASI10 | Rogue agents | Could an agent act outside its intended scope without detection? |

## Instructions

1. Establish scope and boundaries (ask for missing facts).
2. Walk all ten risks. For each: exposure (High/Med/Low/N/A) with a concrete attack scenario specific to this system, existing controls, gaps.
3. Prioritize by likelihood × impact.
4. Propose controls mapped to each gap: least privilege, sandboxing, allow-lists, confirmation for side effects, input provenance labeling, hooks that block dangerous actions, audit logging, kill switch, rate limits.
5. Define tests: red-team prompts and injection fixtures to validate controls.

## Output

```
## Agentic Threat Model: [System] — [date]
### Scope & trust boundaries
### Risk register
| ID | Exposure | Scenario | Existing controls | Gap | Recommended control | Owner |
### Top 5 actions
### Validation tests
```

---

### Further Reading

- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
