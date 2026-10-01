---
name: autonomy-levels
description: "Use when someone asks whether an agent can do a task on its own, when setting agent permissions or approval requirements per repo or task type, when writing an agent delegation policy, or after an agent did more than it should have."
---

# Agent Autonomy Levels

## Purpose

Autonomy should be granted per task type, not per tool or per person. This skill assigns a level to each task class and states what verification earns the next level.

## The ladder

| Level | Name | Agent does | Human does | Typical permission mode |
|-------|------|-----------|------------|-------------------------|
| L0 | Suggest | Answers, explains, proposes | Writes all code | Read-only / plan mode |
| L1 | Draft | Writes code in a branch | Reviews every line before commit | Ask before edits |
| L2 | Execute + review | Implements, runs tests, opens PR | Reviews the PR for alignment | Auto-accept edits, ask for shell |
| L3 | Execute + gate | Implements end to end, including fixes from CI | Approves at defined gates only | Allow-listed commands, sandbox |
| L4 | Autonomous | Runs the loop including merge/deploy | Audits samples and metrics | Headless, scoped credentials |

## Scoring a task type

Score 1–3 on each axis:

- **Blast radius:** 1 = local/isolated, 3 = customer data, money, security, prod infra
- **Reversibility:** 1 = one-click revert, 3 = irreversible (data deletion, external messages, payments)
- **Verifiability:** 1 = deterministic tests prove correctness, 3 = only expert judgment can tell
- **Spec clarity:** 1 = precise acceptance criteria, 3 = vague intent

Total 4–6 → up to L3–L4. 7–9 → L2. 10–12 → L0–L1.

## Instructions

1. List the team's recurring task types (e.g., dependency bumps, CRUD endpoint, UI copy change, schema migration, auth change, incident hotfix).
2. Score each on the four axes; show the math.
3. Assign the level and the matching permission configuration.
4. For each task type, state the **promotion criteria**: what evidence (e.g., 20 consecutive PRs merged without rework, eval pass rate ≥ X) moves it up one level, and the **demotion trigger** (e.g., one production incident).

## Output

```
| Task type | Blast | Revers. | Verif. | Clarity | Total | Level | Permissions | Promote when | Demote when |
```

## Red flags

| Thought | Reality |
|---------|---------|
| "It's worked fine for a week, let's go autonomous" | Promotion needs a defined evidence threshold, not a good week |
| "Senior engineers can give their agents L4" | Autonomy attaches to task types, not to people |
| "We'll add the gate after the pilot" | Gates removed without replacement verification rarely come back |

## Notes

- Irreversible actions stay at L1 or below regardless of score.
- Autonomy is earned with data. Track rework rate per task type.
- Security-sensitive paths (auth, crypto, billing) get a mandatory human gate at any level.

---

### Further Reading

- [Claude Code permission modes and best practices](https://code.claude.com/docs/en/best-practices)
- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
