---
name: release-gates
description: "Use when agents produce changes faster than the release process can absorb, when designing CI/CD gates for AI-generated code, before a go/no-go decision, or when deciding which changes still need human approval."
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

## Red flags

| Thought | Reality |
|---------|---------|
| "CI is green, ship it" | CI proves what the tests check; the gate exists for what they don't |
| "The agent already reviewed it" | Self-review by the author agent is not a gate |
| "Rollback is easy, skip the canary" | Data migrations and external side effects don't roll back |

## Output

Gate table, change-class matrix, rollout and rollback policy, and (if requested) a filled go/no-go checklist for the release.
