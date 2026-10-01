# Try ADLC Skills in 10 Minutes

Six prompts, one per role. Each works in an empty folder; no codebase needed. Paste them as-is, then swap in your own context.

## Setup (1 minute)

```bash
claude plugin marketplace add shmulikdav/adlc-skills
claude plugin install adlc-foundations@adlc-skills
claude plugin install adlc-intent@adlc-skills
claude plugin install adlc-govern@adlc-skills
```

Start `claude` in any folder. In Cowork: Customize → Browse plugins → Personal → + → Add marketplace from GitHub → `shmulikdav/adlc-skills`.

## 1. Engineering leader: where do we stand?

```
/adlc-assess 40 engineers, Claude Code licences for everyone for two months, weekly deploys, ~35% test coverage, no written AI policy, PRs wait 3 days for review
```

**You should get:** a maturity level justified by your weakest critical dimensions, a scorecard against the DORA AI capabilities plus agent-specific readiness, the top constraints, and three first moves.

## 2. Leader: how much can the agent do alone?

```
Can we let the coding agent handle dependency bumps, CRUD endpoints, and database schema migrations without a human reviewing every PR?
```

**You should get:** a different autonomy level per task type, scored on blast radius, reversibility, verifiability, and spec clarity, with promotion and demotion criteria. The skill triggers on its own; no slash command needed.

## 3. Product manager: make a ticket agent-ready

```
/write-agentic-prd Let account admins export audit logs as CSV, filtered by date and user
```

**You should get:** clarifying questions first, then a spec with non-goals, guardrails, testable acceptance criteria, and conditions under which the agent must stop and ask.

## 4. Security: is our agent setup safe?

```
/threat-model Claude Code running in CI with GitHub and Jira MCP access; it picks up tickets and opens PRs
```

**You should get:** a risk register across the OWASP Top 10 for Agentic Applications (ASI01–ASI10), with scenarios specific to your setup and concrete controls.

## 5. Tech lead: unblock the review queue

```
/fix-review-queue 14 engineers, ~120 PRs/week, half agent-authored, median pickup 2 days, big diffs get rubber-stamped
```

**You should get:** a diagnosis by PR type, risk tiers with routing rules, a machine first-pass layer, a PR context-packet template, and WIP limits. (Install `adlc-verify` first.)

## 6. Anyone: vet a plugin before installing

```
/vet-extension https://github.com/<some-org>/<some-claude-plugin>
```

**You should get:** an inventory of instruction-only vs executable components, findings with file references, and an install / restrict / reject verdict.

## Next

- Install the profile for your role: see [Install by role](../README.md#install-by-role)
- Pair with an execution framework: [RECOMMENDED-STACK.md](RECOMMENDED-STACK.md)
- Measure whether it helps you: `claude plugin eval ./adlc-<plugin>` from a clone of this repo
