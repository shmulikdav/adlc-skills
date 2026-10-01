---
name: codebase-map
description: "Produce an agent-oriented map of a codebase: modules and their responsibilities, entry points, data flow, dependencies, test layout, risky areas, and 'start here' paths for common change types. Use when onboarding an agent or a person to an unfamiliar or legacy repo, before a large refactor or rebuild, or when the user asks to audit or understand a codebase."
---

# Codebase Map

## Purpose

Agents explore efficiently when they know where to look. A codebase map is a compact, navigable index that saves repeated exploration in every session and exposes risk before changes start.

## Instructions

1. **Survey** (read-only): top-level tree (2–3 levels), build and dependency files, CI configuration, entry points (main, routes, handlers, jobs), test directories, config and environment handling.
2. **Identify modules**: for each, its responsibility in one line, key files, inbound/outbound dependencies, and owner if known.
3. **Trace 2–3 core flows** end to end (e.g., request → handler → service → DB → response), listing files in order.
4. **Assess risk** per module: test coverage signal, complexity hot spots, dead code, duplicated logic, hard-coded secrets or URLs (report locations only, never values), outdated dependencies.
5. **Write change recipes**: "To add an API endpoint, start at…, mirror…, register in…, test in…".
6. Keep the map factual. Mark uncertain statements `(unverified)`.

## Output

```markdown
# Codebase Map: [repo] — [date]
## Summary (stack, size, architecture style)
## Module index
| Module | Responsibility | Key files | Depends on | Tests | Risk |
## Core flows
## Change recipes
## Risk register (top 10)
## Questions for the team
```

Save as `docs/codebase-map.md` and link it from the context file rather than inlining it.

## Notes

- For large repos, run exploration in subagents per top-level module to keep the main context clean.
- A map ages fast; date it and regenerate after major refactors.
