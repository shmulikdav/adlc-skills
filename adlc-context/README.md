# adlc-context — Context engineering

**ADLC phase:** 2 · Context

## Overview

Context engineering for coding agents: CLAUDE.md / AGENTS.md authoring and audits, codebase maps, context-window budgeting, codifying conventions as skills, hooks or tests, and MCP integration planning.

## Install

```
claude plugin marketplace add braightwave/adlc-skills
claude plugin install adlc-context@adlc-skills
```

## Skills (5)

- `agent-context-files` — Write or audit agent context files (CLAUDE.md, AGENTS.md, .cursor/rules, Copilot instructions) so coding agents get the project knowledge they cannot infer from code: commands, conventions that differ from defaults, architecture boundaries, gotchas, and where to look
- `codebase-map` — Produce an agent-oriented map of a codebase: modules and their responsibilities, entry points, data flow, dependencies, test layout, risky areas, and 'start here' paths for common change types
- `codify-conventions` — Turn tribal knowledge into reusable agent instructions: decide whether a convention belongs in a context file, a skill, a rule file, a hook, or a test, then write it
- `context-budget` — Manage an agent's context window as a scarce budget: what to load always vs on demand, when to clear or compact, when to delegate exploration to subagents, and how to hand off state between sessions with plan/progress files
- `mcp-integration-plan` — Plan which internal systems agents should reach through MCP servers (issue tracker, docs/wiki, design files, observability, databases, CI), with access scope, read vs write permissions, data sensitivity, and rollout order

## Commands (3)

- `/codify-convention` — Turn a recurring agent mistake or team convention into the right artifact — context line, skill, hook, or test
- `/init-agent-context` — Create or audit the agent context file (CLAUDE.md / AGENTS.md) for a repository
- `/map-codebase` — Generate an agent-oriented codebase map with modules, core flows, change recipes, and a risk register

---

Part of [ADLC Skills](../README.md). MIT licensed.
