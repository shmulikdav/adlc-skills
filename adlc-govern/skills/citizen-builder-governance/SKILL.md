---
name: citizen-builder-governance
description: "Use when non-engineers (operations, finance, sales, legal, HR, analysts) are building tools, automations, or apps with Claude Cowork, Claude Code, Lovable, or similar, when shadow AI apps appear on company data, or when leaders ask how to enable business teams to build without creating security and maintenance risk."
---

# Citizen-Builder Governance

**Grounded in:** Anthropic: 2026 Agentic Coding Trends Report; Thoughtworks Technology Radar (Vol. 34, April 2026); NIST AI Risk Management Framework.





## Overview

Agentic coding is spreading beyond engineering: Anthropic's 2026 trends report predicts business teams building their own tools without filing tickets. That unlocks real value and creates a new class of software no engineering team owns. The answer is a paved road, not a ban.

**Core rule:** the rules scale with what a tool touches and how many people depend on it, not with who built it.

## Tiers

| Tier | Scope | Data allowed | Requirements |
|------|-------|--------------|--------------|
| 1 · Personal | One person's productivity | Their own work data; no customer PII, no secrets | Approved tools only; nothing shared externally |
| 2 · Team | A team relies on it | Internal data per classification | Registered in the tool inventory; named owner and backup; basic access control |
| 3 · Business-critical | Customers, money, regulated data, or many teams depend on it | Per data-protection rules | Engineering review, security review, tests, monitoring, handover plan; may be rebuilt by engineering |

## Instructions

1. **Inventory** what already exists (survey + workspace scans); classify each tool into a tier.
2. **Publish the paved road:** approved builder tools, approved connectors, a data classification cheat sheet, templates for common automations.
3. **Define promotion triggers** from tier 1→2→3 (number of users, data class, external exposure, financial impact).
4. **Set guardrails** on the platform side: connector allow-lists, least-privilege service accounts, no personal API keys in shared tools, audit logs.
5. **Offer engineering office hours** and a lightweight review for tier 2→3 promotions.
6. **Plan the lifecycle:** owner leaves → tool is reassigned or retired; quarterly cleanup of unused tools.

## Red flags

| Thought | Reality |
|---------|---------|
| "Just ban it" | Usage goes underground and you lose visibility |
| "It's only a spreadsheet automation" | It may be moving customer data to a third-party service |
| "Engineering will maintain it later" | Only if the handover was planned; otherwise it breaks when the builder leaves |

## Output

Tier policy, paved-road kit (tools, connectors, templates), tool inventory format, promotion triggers, and review process.

---

### Further Reading

- [Anthropic: 2026 Agentic Coding Trends Report (Trends 5 and 7)](https://resources.anthropic.com/2026-agentic-coding-trends-report)
- [Thoughtworks Technology Radar (Vol. 34, April 2026)](https://www.thoughtworks.com/radar)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
