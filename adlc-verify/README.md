# adlc-verify — Behavioral validation & review

**ADLC phase:** 4 · Verify

## Overview

Verification of agent-built software: behavioral testing, tests derived from specs, alignment review of agent PRs, hallucination checks for APIs and dependencies, and a Definition of Done for agent work.

## Install

```
claude plugin marketplace add braightwave/adlc-skills
claude plugin install adlc-verify@adlc-skills
```

## Skills (5)

- `agent-code-review` — Review agent-authored code for alignment, not just correctness: does the diff implement the spec and only the spec, follow the repo's constraints, keep tests honest, and avoid the typical failure patterns of AI-generated code (invented APIs, silent scope creep, weakened tests, duplicated logic, swallowed errors, insecure defaults)
- `behavioral-testing` — Design behavioral validation for agent-built software: test what the system does across the input range (properties, invariants, contracts, state transitions) rather than matching the agent's own implementation
- `definition-of-done` — Define and enforce a Definition of Done for agent-authored work: the checks an agent must run and evidence it must attach before claiming completion, plus the human gates that remain
- `hallucination-checks` — Verify that what an agent referenced actually exists and behaves as claimed: packages and versions, imports, API methods, config keys, CLI flags, environment variables, file paths, and documentation links; detect typosquatted or nonexistent dependencies
- `tests-from-specs` — Derive a traceable test suite from a spec or test-management system: map every acceptance criterion to tests, classify existing vs proposed vs unverified, and generate test code or test cases (including from Xray, TestRail, or Gherkin feature files)

## Commands (3)

- `/derive-tests` — Build a traceability matrix from specs or test cases and generate the missing tests
- `/review-agent-pr` — Run an alignment review of an agent-authored PR or diff against its spec, with evidence-backed findings
- `/verify-change` — Verify a change meets the Definition of Done with evidence before it is called done

## Agents (1)

- `agent-output-reviewer` — Independent reviewer for agent-authored changes

---

Part of [ADLC Skills](../README.md). MIT licensed.
