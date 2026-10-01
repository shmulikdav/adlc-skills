# adlc-verify — Behavioral validation & review

**ADLC phase:** 4 · Verify

## Overview

Verification of agent-built software: review capacity design for the agent-PR bottleneck, behavioral testing, tests derived from specs, alignment review of agent PRs, hallucination checks, and a Definition of Done for agent work.

## Install

```
claude plugin marketplace add shmulikdav/adlc-skills
claude plugin install adlc-verify@adlc-skills
```

## Skills (6)

- `agent-code-review` — Use when asked to review, check, or approve a pull request, diff, or patch written by Claude Code, Cursor, Codex, Copilot, or another agent, whether pasted inline or in the repository, when setting up a review process for AI-generated code, or before merging agent work into main
- `behavioral-testing` — Use when building a test strategy for AI-generated code, when tests pass but behavior is wrong, when QA is shifting from manual regression to verifying agent output, or when correctness of money, permissions, or data integrity matters
- `definition-of-done` — Use when agents claim work is done prematurely, when standardizing the quality bar for agent-authored changes across teams, or when writing the verification section of a context file or PR template
- `hallucination-checks` — Use before merging agent-generated code, when a build fails on an unknown symbol, package, or flag, when an agent adds or suggests a new dependency, or when PR text claims results without evidence
- `review-capacity` — Use when agent-authored pull requests pile up in a review backlog, PR pickup or review time is growing, reviewers rubber-stamp large AI-generated diffs, adding reviewers did not help, merge or acceptance rates of agent PRs are low, or a team asks how to redesign code review for agent-scale output
- `tests-from-specs` — Use when asked where test coverage stands, which requirements or test cases have no automated test, or how to close a coverage gap, when mapping test cases from Xray, TestRail, Zephyr, Gherkin, PRDs, or acceptance criteria (pasted inline or exported) to automated tests, or when lifting coverage with agents

## Commands (4)

- `/derive-tests` — Build a traceability matrix from specs or test cases and generate the missing tests
- `/fix-review-queue` — Diagnose and redesign code review when agent PRs pile up — risk tiers, machine first pass, ownership, WIP limits
- `/review-agent-pr` — Run an alignment review of an agent-authored PR or diff against its spec, with evidence-backed findings
- `/verify-change` — Verify a change meets the Definition of Done with evidence before it is called done

## Agents (1)

- `agent-output-reviewer` — Independent reviewer for agent-authored changes

## Evals (8 cases)

Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.

```
claude plugin eval ./adlc-verify
```

---

Part of [ADLC Skills](../README.md). MIT licensed.
