---
name: agentic-prd
description: "Write an Agentic PRD (Agent Execution Specification): a product spec a coding agent can execute without guessing. Covers business intent, scope and non-goals, constraints and guardrails, repo context pointers, interfaces, acceptance tests, and stop conditions. Use when a PM or engineer wants a PRD for Claude Code / Cursor / Codex, says 'make this spec agent-ready', or hands an agent a vague ticket."
---

# Agentic PRD (Agent Execution Specification)

## Purpose

A classic PRD is written for humans who fill gaps with judgment and hallway conversations. An agent fills gaps with plausible guesses. An Agentic PRD removes the gaps that matter: intent, boundaries, and how "done" is verified.

## Principles

- **Intent over instructions.** State the outcome and why; let the agent choose the path within constraints.
- **Boundaries are explicit.** Non-goals and forbidden actions are as important as goals.
- **Done is testable.** Every requirement maps to an acceptance check an agent can run or a human can verify in minutes.
- **Point, don't paste.** Reference files, ADRs, and docs by path instead of copying them in.
- **Short enough to fit.** Aim for 1–3 pages. Long specs dilute attention.

## Template

```markdown
# [Feature] — Agent Execution Spec
Version: | Owner: | Status: Draft / Approved

## 1. Business intent
Problem, who has it, why now, expected outcome (metric).

## 2. Scope
In scope: ...
Non-goals (do NOT do): ...

## 3. Users & scenarios
Primary scenarios as Given/When/Then.

## 4. Functional requirements
FR-1 ... (each with an ID; each traceable to acceptance criteria)

## 5. Constraints & guardrails
- Tech: languages, libraries allowed/forbidden, patterns to follow (link ADRs)
- Security & data: PII handling, secrets, auth rules
- Performance: budgets
- Files/areas the agent must not modify

## 6. Repo context
- Entry points: path/to/...
- Similar existing implementation to mirror: path/to/...
- Conventions: see CLAUDE.md / AGENTS.md sections ...
- How to run tests: command

## 7. Interfaces & data
API contracts, schemas, events (or links to them).

## 8. Acceptance criteria
AC-1 (covers FR-1): Given ... When ... Then ...
Verification: automated test / manual check / both

## 9. Definition of done
Tests pass, lint/type checks pass, docs updated, no new warnings, PR description links ACs.

## 10. Stop & escalate conditions
The agent must stop and ask when: a requirement conflicts with existing behavior; a migration is needed; a forbidden file must change; acceptance criteria cannot be met.

## 11. Open questions
```

## Instructions

1. Read whatever the user provides (ticket, notes, existing PRD). Identify missing intent, missing boundaries, and untestable requirements.
2. Ask at most 5 high-leverage clarifying questions; for the rest, write explicit, labeled assumptions.
3. Fill the template. Give every requirement an ID and map it to at least one acceptance criterion.
4. Run a self-check: any requirement without an AC? any vague words ("fast", "user-friendly", "robust") without a number? any action with side effects without a stop condition?
5. Save as `AgentSpec-[feature]-[date].md`.

## Notes

- If the user's org has a canonical spec format (e.g., Spec Kit's spec.md), adapt the sections rather than forcing this template.
- Keep implementation detail out of intent sections; put hard technical constraints in section 5.

---

### Further Reading

- [GitHub Spec Kit: Specification-Driven Development](https://github.com/github/spec-kit/blob/main/spec-driven.md)
- [Claude Code best practices: give verification criteria](https://code.claude.com/docs/en/best-practices)
