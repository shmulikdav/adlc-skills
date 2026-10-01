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

- `agent-permissions` — Use when configuring what a coding agent may read, edit, or run (Claude Code settings, permissions, sandboxing), deciding what runs without approval, setting up agents in CI or headless mode, or after a near-miss with an agent action
- `agentic-threat-model` — Use when assessing the security of coding agents, MCP connections, CI agents, or an AI agent being built, preparing a security review of an agentic setup, or when a team asks what could go wrong if an agent is manipulated
- `ai-compliance-mapping` — Use when preparing for an AI audit or certification (ISO/IEC 42001, SOC 2), answering customer security questionnaires about AI use in development, or aligning agentic development practices with NIST AI RMF or the EU AI Act
- `extension-vetting` — Use when someone asks whether a skill, plugin, MCP server, hook, or agent rules file is safe to install, before adding a new plugin marketplace, or when building an approved-extensions list for a team
- `guardrail-hooks` — Use when a rule must be enforced every time rather than remembered, when CLAUDE.md instructions are not followed reliably, when protecting secrets, CI config, or migrations from agent edits, or when setting up Claude Code hooks

## Commands (3)

- `/governance-pack` — Produce an ADLC governance pack — permissions, hooks, threat model, and compliance mapping — for a team or org
- `/threat-model` — Threat-model an agentic development setup or an agent product against the OWASP Agentic Top 10
- `/vet-extension` — Security-vet a third-party skill, plugin, MCP server, or hook before installing it

## Agents (1)

- `security-reviewer` — Security-focused reviewer for agentic setups and agent-authored changes

## Evals (6 cases)

Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.

```
claude plugin eval ./adlc-govern
```

---

Part of [ADLC Skills](../README.md). MIT licensed.
