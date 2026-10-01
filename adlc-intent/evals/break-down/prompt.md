---
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
tags: [smoke, trigger, task-decomposition]
description: Should invoke task-decomposition and apply its method
---

Here's the plan: add CSV export for audit logs — new API endpoint, background job for large exports, email when ready, admin UI button. Break it into tasks for agents.
