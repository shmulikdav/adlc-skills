---
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
tags: [smoke, trigger, agent-runtime-guardrails]
description: Should invoke agent-runtime-guardrails and apply its method
---

Our agent reads customer emails and can update orders. A red-teamer got it to change a shipping address by putting instructions in an email. How do we fix this?
