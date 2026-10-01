---
name: release-gates
description: "Define human approval gates and automated checks for releasing agent-built changes: what must be true before merge, before staging, before production, and who signs off, with progressive delivery (flags, canaries) and rollback triggers. Use when agents produce changes faster than the release process can absorb, when designing a CI/CD gate policy for AI-generated code, or before a go/no-go decision."
---

# Release Gates for Agentic Delivery

## Purpose

Agents compress the build phase; risk concentrates at release. Gates put human judgment where it matters and automation everywhere else.

## Gate model

| Gate | Automated checks | Human decision | Owner |
|------|------------------|----------------|-------|
| G1 Merge | Tests, types, lint, secret scan, dependency verification, DoD evidence | Alignment review approved | Code owner |
| G2 Staging | Integration/E2E, contract tests, migration dry run | — (auto) unless risky change class | CI |
| G3 Production | Canary metrics, error budget, performance budgets | Go/no-go for high-risk change classes | Release owner |
| G4 Post-release | Monitors, alerts, rollback triggers armed | Confirm or roll back within window | On-call |

## Instructions

1. Define **change classes** (e.g., docs, UI copy, standard feature, data migration, auth/billing, infra). High-risk classes require explicit human approval at G3 regardless of autonomy level.
2. For each gate, list checks and the evidence format.
3. Define **progressive delivery**: feature flag default off, percentage rollout, canary duration, success metrics.
4. Define **rollback triggers** (error rate, latency, business KPI) and who can pull them without a meeting.
5. Produce a go/no-go checklist for a specific release when one is provided.

## Output

Gate table, change-class matrix, rollout and rollback policy, and (if requested) a filled go/no-go checklist for the release.
