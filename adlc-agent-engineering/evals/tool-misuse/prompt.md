---
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
tags: [smoke, trigger, tool-design]
description: Should invoke tool-design and apply its method
---

Our agent has tools called get_data, update_record, and query. It keeps calling the wrong one and passing bad parameters. How should we redesign them?
