# adlc-build — Agentic construction

**ADLC phase:** 3 · Build

## Overview

Agentic construction workflows: explore-plan-implement, test-first development with agents, parallel agents and worktrees, small-batch delivery, and legacy modernization with behavior parity.

## Install

```
claude plugin marketplace add braightwave/adlc-skills
claude plugin install adlc-build@adlc-skills
```

## Skills (5)

- `agentic-tdd` — Test-driven development with coding agents: write failing tests from acceptance criteria first, confirm they fail for the right reason, commit them, then have the agent implement until green without modifying the tests
- `explore-plan-implement` — Run the core agentic coding loop: explore the relevant code read-only, write a reviewable plan, implement against the plan with verification after each step, then commit with a traceable message
- `legacy-modernization` — Modernize or rebuild a legacy system with coding agents: characterize current behavior first (golden tests, recorded I/O), extract an implicit spec from code, choose strangler-fig vs rewrite, migrate in verified slices, and keep behavior parity
- `parallel-agents` — Run multiple coding agents in parallel safely: split work into independent streams, isolate each in a git worktree or separate session, assign roles (implementer, test writer, reviewer), coordinate through files and PRs, and merge without conflicts
- `small-batch-delivery` — Keep agent-generated changes small and shippable: PR size limits, feature flags, trunk-based integration, stacked PRs, and rollback readiness

## Commands (3)

- `/build-feature` — Implement an approved plan test-first, verifying after each step and producing small, reviewable PRs
- `/modernize` — Plan a legacy system modernization or rebuild with behavior characterization, strategy choice, and verified migration slices
- `/plan-feature` — Explore the codebase read-only and produce a reviewable implementation plan before any code changes

---

Part of [ADLC Skills](../README.md). MIT licensed.
