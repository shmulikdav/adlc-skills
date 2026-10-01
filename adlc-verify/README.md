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

- `agent-code-review` — Use when reviewing a pull request or diff written by Claude Code, Cursor, Codex, Copilot, or another agent, when setting up a review process for AI-generated code, or before merging agent work into main
- `behavioral-testing` — Use when building a test strategy for AI-generated code, when tests pass but behavior is wrong, when QA is shifting from manual regression to verifying agent output, or when correctness of money, permissions, or data integrity matters
- `definition-of-done` — Use when agents claim work is done prematurely, when standardizing the quality bar for agent-authored changes across teams, or when writing the verification section of a context file or PR template
- `hallucination-checks` — Use before merging agent-generated code, when a build fails on an unknown symbol, package, or flag, when an agent adds or suggests a new dependency, or when PR text claims results without evidence
- `tests-from-specs` — Use when generating tests from PRDs, acceptance criteria, Gherkin, or test-management exports (Xray, TestRail, Zephyr), when asked which requirements have no test, or when lifting test coverage with agents

## Commands (3)

- `/derive-tests` — Build a traceability matrix from specs or test cases and generate the missing tests
- `/review-agent-pr` — Run an alignment review of an agent-authored PR or diff against its spec, with evidence-backed findings
- `/verify-change` — Verify a change meets the Definition of Done with evidence before it is called done

## Agents (1)

- `agent-output-reviewer` — Independent reviewer for agent-authored changes

## Evals (6 cases)

Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.

```
claude plugin eval ./adlc-verify
```

---

Part of [ADLC Skills](../README.md). MIT licensed.
