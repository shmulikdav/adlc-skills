---
name: autonomy-levels
description: "Use when someone asks whether an agent can do a task on its own, when setting agent permissions or approval requirements per repo or task type, when writing an agent delegation policy, or after an agent did more than it should have."
---

# Agent Autonomy Levels

**Grounded in:** Feng, McDonald, Zhang: Levels of Autonomy for AI Agents (Knight First Amendment Institute); OWASP Top 10 for Agentic Applications (2026); Anthropic: 2026 Agentic Coding Trends Report.





## Purpose

Autonomy should be a deliberate design decision per task type, separate from what the agent is capable of. This skill uses the five levels of agent autonomy published by Feng, McDonald and Zhang (Knight First Amendment Institute / University of Washington), defined by the role the human plays, and maps each level to concrete coding-agent configurations.

## The five levels (by the human's role)

| Level | Human role | In agentic development this looks like | Typical configuration |
|-------|-----------|----------------------------------------|-----------------------|
| L1 | **Operator** | Human drives; agent answers, explains, suggests on request | Read-only or plan mode |
| L2 | **Collaborator** | Human and agent share planning and execution, handing control back and forth | Interactive session, edits reviewed as they happen |
| L3 | **Consultant** | Agent leads the task; consults the human for intent, preferences, and expertise | Agent implements and opens a PR; human reviews for alignment |
| L4 | **Approver** | Agent works independently; human approves at defined gates or for risky actions | Sandboxed, allow-listed or auto-mode execution; approval required for merges, migrations, deploys |
| L5 | **Observer** | Agent runs fully autonomously; human monitors and can stop it | Background/CI agents with scoped credentials, budgets, audit logs, and a kill switch |

Most production coding work today sits at L3–L4. Anthropic's 2026 research found developers use AI in roughly 60% of their work but fully delegate only 0–20% of tasks, which is consistent with this.

## Scoring a task type

Score 1–3 on each axis:

- **Blast radius:** 1 = local/isolated, 3 = customer data, money, security, prod infra
- **Reversibility:** 1 = one-click revert, 3 = irreversible (data deletion, external messages, payments)
- **Verifiability:** 1 = deterministic tests prove correctness, 3 = only expert judgment can tell
- **Spec clarity:** 1 = precise acceptance criteria, 3 = vague intent

Total 4–6 → up to L4–L5 (Approver/Observer). 7–9 → L3 (Consultant). 10–12 → L1–L2 (Operator/Collaborator).

These thresholds are a **starting heuristic**, not a standard. Calibrate them with your own rework and incident data.

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
| "Senior engineers can give their agents L5" | Autonomy attaches to task types, not to people |
| "We'll add the gate after the pilot" | Gates removed without replacement verification rarely come back |

## Notes

- Irreversible actions (data deletion, payments, external messages) never run above L4: a human approves them, regardless of score.
- Autonomy is earned with data. Track rework rate per task type.
- Security-sensitive paths (auth, crypto, billing) get a mandatory human gate at any level.

---

### Further Reading

- [Claude Code permission modes and best practices](https://code.claude.com/docs/en/best-practices)
- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Feng, McDonald, Zhang: Levels of Autonomy for AI Agents (Knight First Amendment Institute)](https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1)
- [Anthropic: 2026 Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report)
