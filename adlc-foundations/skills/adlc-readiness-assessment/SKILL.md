---
name: adlc-readiness-assessment
description: "Use when an organization asks whether it is ready for agentic development or coding agents at scale, wants an AI-readiness or maturity baseline for R&D, is starting an AI transformation of engineering, or reports that AI coding tools are not delivering the expected productivity."
---

# ADLC Readiness Assessment

## Purpose

Produce an evidence-based readiness baseline before an organization scales coding agents. The core finding behind this skill: AI is an amplifier. It magnifies strong engineering foundations and magnifies dysfunction. So the question is not "which tool" but "which foundations".

## Inputs to gather

Ask for whatever is missing, in one batch, before scoring:

- Team size, number of teams, main stack, monorepo vs polyrepo
- Current AI tooling (Claude Code, Cursor, Copilot, Codex, other) and license coverage
- How work flows today: ticket → spec → code → review → test → release
- Deploy frequency, lead time, change-failure rate, MTTR (rough numbers are fine)
- Test coverage and CI duration
- Existing AI policy (written? communicated? enforced?)
- Internal docs: where architecture, conventions, and decisions live

## Scoring model

Score each dimension 1–5 with a one-line evidence note. Never score without evidence; mark "unknown" instead.

### A. DORA AI Capabilities (2025)

| # | Capability | 1 = | 5 = |
|---|------------|-----|-----|
| 1 | Clear, communicated AI stance | No policy; people guess | Written, known, updated stance on tools, data, and expectations |
| 2 | Healthy data ecosystem | Data siloed, low quality | Trusted, governed, discoverable data |
| 3 | AI-accessible internal data | Agents see only the open file | Agents reach docs, tickets, ADRs, runbooks via MCP/context files |
| 4 | Strong version control practices | Long-lived branches, rare commits | Small commits, easy rollback, protected main |
| 5 | Working in small batches | Big-bang PRs | Small PRs, feature flags, trunk-based |
| 6 | User-centric focus | Output-driven roadmap | Outcomes tied to user needs |
| 7 | Quality internal platform | Every team builds its own path | Paved roads: CI, environments, templates, guardrails |

### B. Agent-specific readiness

| # | Dimension | What good looks like |
|---|-----------|----------------------|
| 8 | Agent context | CLAUDE.md / AGENTS.md per repo, kept short and current |
| 9 | Verification harness | Fast tests an agent can run locally; deterministic CI |
| 10 | Spec discipline | Features start from a written spec with acceptance criteria |
| 11 | Governance & security | Agent permissions, secrets handling, audit trail defined |
| 12 | Measurement | Baseline of delivery metrics exists before rollout |

## Maturity levels

- **Level 0 – Ad hoc:** individuals use chat assistants; no shared practice
- **Level 1 – Assisted:** licensed tools, autocomplete and chat; SDLC unchanged
- **Level 2 – Delegated:** agents implement scoped tasks; humans review every diff
- **Level 3 – Orchestrated:** spec-driven work, parallel agents, verification gates, shared context files
- **Level 4 – Agentic:** agents run large parts of the lifecycle end to end; humans own intent, gates, and governance

Assign the level from the weakest critical dimensions (4, 8, 9, 11), not the average. A team with great tools and no tests is Level 1.

## Output

```
## ADLC Readiness: [Org / Team]
Maturity: Level [n] — [one-sentence justification]

### Scorecard
| Dimension | Score | Evidence | Gap |

### Top 3 constraints (what will break first if you scale agents now)
### First 3 moves (next 30 days, each with owner and success signal)
### What NOT to do yet
```

Save as `ADLC-Readiness-[team]-[date].md`.

## Notes

- Be blunt about foundations. Weak tests plus fast agents equals fast defects.
- Separate perceived from measured productivity. Self-reported speedups are unreliable.
- Recommend one pilot team with good foundations, not a company-wide rollout.

---

### Further Reading

- [DORA research publications (State of AI-assisted Software Development 2025, AI Capabilities Model)](https://dora.dev/research/publications/)
- [Claude Code best practices](https://code.claude.com/docs/en/best-practices)
