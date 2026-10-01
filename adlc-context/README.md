# adlc-context — Context engineering

**ADLC phase:** 2 · Context

## Overview

Context engineering for coding agents: CLAUDE.md / AGENTS.md authoring and audits, codebase maps, context-window budgeting, codifying conventions as skills, hooks or tests, MCP integration planning, and evidence-based skill library management.

## Install

```
claude plugin marketplace add shmulikdav/adlc-skills
claude plugin install adlc-context@adlc-skills
```

## Skills (6)

- `agent-context-files` — Use when setting up or auditing CLAUDE.md, AGENTS.md, .cursor/rules, or Copilot instructions for a repository, when an agent keeps repeating the same project-specific mistake, or when a context file has grown long and is being ignored
- `codebase-map` — Use when onboarding an agent or a person to an unfamiliar or legacy repository, before a large refactor, rebuild, or migration, or when asked to audit or explain how a codebase is structured
- `codify-conventions` — Use when someone says the agent keeps doing something wrong, describes a team convention ('we always do it this way'), asks to make something a skill, rule, or hook, or wants to package team know-how for agents
- `context-budget` — Use when agent quality drops during long sessions, sessions run out of context, work must continue across sessions, or when deciding what belongs in CLAUDE.md vs a skill vs a subagent vs a linked document
- `mcp-integration-plan` — Use when deciding which internal systems coding agents should access through MCP servers (tickets, docs, designs, logs, databases, CI), when making internal data AI-accessible, or when agents lack context that lives outside the repository
- `skill-library-management` — Use when a team is building, curating, or pruning an internal library of agent skills or plugins, when deciding whether a skill is worth keeping, when skills are not triggering or are slowing agents down, or before publishing skills to other teams

## Commands (4)

- `/audit-skills` — Audit an internal skills or plugin library — triggering, measured value, overlap, and what to keep, fix, or cut
- `/codify` — Turn a recurring agent mistake or team convention into the right artifact — context line, skill, hook, or test
- `/init-agent-context` — Create or audit the agent context file (CLAUDE.md / AGENTS.md) for a repository
- `/map-codebase` — Generate an agent-oriented codebase map with modules, core flows, change recipes, and a risk register

## Evals (8 cases)

Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.

```
claude plugin eval ./adlc-context
```

---

Part of [ADLC Skills](../README.md). MIT licensed.
