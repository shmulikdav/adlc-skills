---
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
tags: [smoke, trigger, agentic-threat-model]
description: Should invoke agentic-threat-model and apply its method
---

We're about to run Claude Code in CI with access to our GitHub and Jira through MCP so it can pick up tickets and open PRs. What could go wrong?
