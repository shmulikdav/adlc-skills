---
name: spec-clarification
description: "Stress-test a spec before an agent builds it: find ambiguities, contradictions, missing edge cases, unstated assumptions, and decisions an agent would otherwise make silently; return a prioritized question list with suggested defaults. Use when reviewing a PRD or spec for agent-readiness, before planning implementation, or when the user says 'what's missing from this spec' or 'interview me about this feature'."
---

# Spec Clarification (Ambiguity Hunt)

## Purpose

Every ambiguity left in a spec becomes a silent decision made by the agent. This skill surfaces those decisions so a human makes them deliberately.

## Instructions

1. Read the spec end to end. Build a quick model: actors, entities, states, transitions, external systems.
2. Hunt across these categories:
   - **Scope:** what is explicitly out? what neighboring behavior might be touched?
   - **Data:** required vs optional fields, validation, limits, retention, migration of existing data
   - **States & errors:** empty, loading, partial failure, timeouts, retries, idempotency
   - **Permissions:** who can do what; multi-tenant boundaries
   - **Concurrency:** two users, two tabs, duplicate submissions
   - **Non-functional:** performance, accessibility, localization (including RTL), observability
   - **Compatibility:** API versioning, backward compatibility, feature flags
   - **Contradictions:** requirements that conflict with each other or with existing behavior in the repo
3. For each finding, write a question **with a recommended default** and the impact if the default is wrong.
4. Prioritize: **Blocking** (changes architecture or data model) → **Important** (changes user-visible behavior) → **Minor** (cosmetic, can default).
5. Ask the user the blocking questions first, max 5 at a time. Apply answers to the spec and record decisions in a "Clarifications" section with dates.

## Output

```
## Clarifications: [Feature]
| # | Priority | Question | Recommended default | Impact if wrong |
```
Then the updated spec section(s).

## Notes

- If the spec is in a repo, check existing code for the answer before asking the human.
- "Interview me" mode: ask one question at a time and wait.
