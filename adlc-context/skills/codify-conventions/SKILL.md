---
name: codify-conventions
description: "Use when someone says the agent keeps doing something wrong, describes a team convention ('we always do it this way'), asks to make something a skill, rule, or hook, or wants to package team know-how for agents."
---

# Codify Conventions

**Grounded in:** Thoughtworks Technology Radar (Vol. 34, April 2026); Claude Code: skills; Claude Code hooks reference.





## Purpose

Every repeated correction to an agent is a convention that has not been written down in the right place. This skill picks the right enforcement mechanism and writes it.

## Choose the mechanism

| If the convention is… | Put it in… | Why |
|------------------------|-----------|-----|
| Short and always relevant | Context file | Loaded every session |
| A multi-step procedure or domain knowledge used sometimes | Skill (`skills/<name>/SKILL.md`) | Loaded only when relevant |
| Scoped to a folder or file type | Nested context file / path-scoped rule | Applies only where needed |
| Must happen every time, no exceptions | Hook, linter rule, or CI check | Deterministic; doesn't rely on the model remembering |
| A correctness property | Test | Verifiable forever |

In Thoughtworks' Radar terms, context files and skills are **feedforward** controls (guiding the agent before it acts) and hooks, linters, and tests are **feedback** controls (catching it after). Strong harnesses use both.

Rule of thumb: if breaking it is costly, do not rely on instructions alone. Enforce it with a hook, linter, or test.

## Writing a skill

```markdown
---
name: kebab-case-name            # must match the folder name
description: "What it does + when to use it, including the phrases people actually say. Be specific and a little pushy so it triggers."
---
# Title
## Purpose
## Instructions (imperative steps)
## Output format
## Notes / pitfalls
```

Keep SKILL.md focused (well under 500 lines). Move long references into `references/` files and scripts into `scripts/`, and point to them from the body.

## Instructions

1. Collect 2–3 concrete examples of the mistake or the desired behavior.
2. Classify using the table and explain the choice in one sentence.
3. Write the artifact (context-file lines, skill, hook config, or test).
4. Provide a quick test: a prompt that should now produce the correct behavior.

---

### Further Reading

- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [Agent Skills open standard](https://agentskills.io)
- [Thoughtworks Technology Radar (Vol. 34, April 2026)](https://www.thoughtworks.com/radar)
- [Claude Code hooks reference](https://code.claude.com/docs/en/hooks)
