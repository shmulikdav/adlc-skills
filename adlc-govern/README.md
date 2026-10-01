# adlc-govern — Security, permissions & compliance

**ADLC phase:** 5 · Govern

## Overview

Governance and security for agentic development: OWASP Agentic Top 10 threat modeling, least-privilege agent permissions, guardrail hooks, compliance mapping (ISO 42001, NIST AI RMF, EU AI Act, SOC 2), and extension vetting.

## Install

```
claude plugin marketplace add braightwave/adlc-skills
claude plugin install adlc-govern@adlc-skills
```

## Skills (5)

- `agent-permissions` — Design least-privilege permission configurations for coding agents: allow/ask/deny rules for tools and shell commands, file and directory boundaries, network access, sandboxing, secrets handling, and per-environment profiles (local, CI, headless)
- `agentic-threat-model` — Threat-model an agentic development setup or an AI agent product using the OWASP Top 10 for Agentic Applications (ASI01–ASI10): goal hijack, tool misuse, identity and privilege abuse, supply chain, unexpected code execution, memory and context poisoning, inter-agent communication, cascading failures, human-agent trust exploitation, rogue agents
- `ai-compliance-mapping` — Map an organization's agentic development practices and AI features to governance frameworks (ISO/IEC 42001 AI management system, NIST AI RMF, EU AI Act, SOC 2) and produce a control gap list with evidence to collect
- `extension-vetting` — Vet third-party agent extensions before installing them: skills, plugins, MCP servers, hooks, and agent rule files
- `guardrail-hooks` — Design deterministic guardrails for coding agents with lifecycle hooks: block edits to protected files, block dangerous commands, auto-format and lint after edits, run tests before stop, log every tool call for audit

## Commands (3)

- `/governance-pack` — Produce an ADLC governance pack — permissions, hooks, threat model, and compliance mapping — for a team or org
- `/threat-model` — Threat-model an agentic development setup or an agent product against the OWASP Agentic Top 10
- `/vet-extension` — Security-vet a third-party skill, plugin, MCP server, or hook before installing it

## Agents (1)

- `security-reviewer` — Security-focused reviewer for agentic setups and agent-authored changes

---

Part of [ADLC Skills](../README.md). MIT licensed.
