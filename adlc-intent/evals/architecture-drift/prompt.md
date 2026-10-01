---
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
tags: [smoke, trigger, architecture-guardrails]
description: Should invoke architecture-guardrails and apply its method
---

Our agents keep calling the database directly from API handlers even though we use a service layer, and they re-debate decisions we made months ago. How do we make them stick to the architecture?
