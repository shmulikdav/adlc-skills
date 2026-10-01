---
name: legacy-modernization
description: "Modernize or rebuild a legacy system with coding agents: characterize current behavior first (golden tests, recorded I/O), extract an implicit spec from code, choose strangler-fig vs rewrite, migrate in verified slices, and keep behavior parity. Use when rebuilding an old system from scratch, migrating frameworks or languages, or auditing a legacy codebase before a rewrite."
---

# Legacy Modernization with Agents

## Purpose

Agents are good at reading and translating code, and that is exactly the trap: they will faithfully reproduce behavior nobody wants, or "improve" behavior somebody depends on. Modernization succeeds when current behavior is captured before anything changes.

## Instructions

1. **Audit** (read-only): build a codebase map; inventory features, integrations, data stores, scheduled jobs, and undocumented behaviors (magic constants, implicit retries, timezone handling).
2. **Characterize behavior:** create characterization (golden) tests around critical paths; record real request/response or input/output pairs from a non-production environment; snapshot DB schemas.
3. **Extract the implicit spec:** generate a behavior spec from code + tests. Mark each behavior *keep*, *change*, or *drop* with a human owner decision.
4. **Choose the strategy:**
   - *Strangler fig* (route traffic slice by slice to the new system) when the system is live and risk-sensitive.
   - *Rewrite* only when the system is small, well characterized, or the platform is end-of-life.
5. **Slice the migration:** by capability or route; each slice has parity tests, a cutover plan, and a rollback.
6. **Run parity checks** continuously: same inputs into old and new, diff outputs; investigate every diff as keep/change/bug.
7. **Decommission** only after a defined period with zero unexplained diffs.

## Output

Audit summary, behavior spec with keep/change/drop decisions, strategy rationale, slice plan, and parity-testing approach.

## Notes

- Never let the agent infer intent from code alone for money, permissions, or data retention logic. Confirm with an owner.
- Keep secrets and production data out of the agent's context during the audit; use sanitized samples.
