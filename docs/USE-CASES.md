# Use cases

Ten situations engineering organizations hit when they adopt coding agents, and the path through the kit for each. Every command suggests the next step when it finishes, so you can also start with the first command and follow the prompts.

Commands are shown in Claude Code and Cursor form (`/adlc-assess`). In Codex, use `$adlc-assess`.

| # | Situation | Who usually owns it | Plugins to install |
| --- | --- | --- | --- |
| 1 | [Rolling out coding agents across engineering](#1-rolling-out-coding-agents-across-engineering) | CTO, VP Engineering | foundations, govern, context |
| 2 | [Agent PRs are drowning the review queue](#2-agent-prs-are-drowning-the-review-queue) | Tech lead, engineering manager | verify, operate |
| 3 | [Security asks whether the agents are safe](#3-security-asks-whether-the-agents-are-safe) | Security, platform | govern, context |
| 4 | [Agents build the wrong thing from vague tickets](#4-agents-build-the-wrong-thing-from-vague-tickets) | Product manager, tech lead | intent, verify |
| 5 | [Leadership wants proof the investment pays off](#5-leadership-wants-proof-the-investment-pays-off) | CTO, engineering operations | foundations, operate |
| 6 | [Business teams are building their own apps with AI](#6-business-teams-are-building-their-own-apps-with-ai) | CIO, security, business leaders | govern |
| 7 | [Modernizing a legacy system with agents](#7-modernizing-a-legacy-system-with-agents) | Architect, tech lead | context, build, verify |
| 8 | [QA moves from manual regression to verifying agent output](#8-qa-moves-from-manual-regression-to-verifying-agent-output) | QA lead | verify |
| 9 | [Shipping an AI agent as a product](#9-shipping-an-ai-agent-as-a-product) | Product and engineering for AI features | agent-engineering, govern, operate |
| 10 | [Agent work caused an incident](#10-agent-work-caused-an-incident) | Engineering manager, SRE | operate, context |

---

## 1. Rolling out coding agents across engineering

**Situation.** Licences are bought and some teams use agents daily, but there is no shared policy, no baseline and no plan. The risk is a year of scattered usage that nobody can show results for.

| Step | Command | What you get |
| --- | --- | --- |
| 1 | `/adlc-assess` | Maturity level, a 15-dimension scorecard, the constraints that will break first, and three first moves |
| 2 | `/map-to-adlc` | Each step of your current workflow mapped to its agentic version, and where agents should enter first |
| 3 | `/adlc-roadmap` | A 90-day plan in four phases (Map, Prioritize, Build, Scale) with decision gates |
| 4 | `/governance-pack` | AI policy, agent permissions, hooks and compliance mapping before usage scales |
| 5 | `/init-agent-context` | A context file per pilot repo, so agents work with your conventions from day one |

**Try:** `/adlc-assess 120 engineers in 9 teams, Claude Code and Cursor licences for everyone, monthly releases, no AI policy, no delivery metrics`

**You end with:** a baseline to measure against, a sequenced plan, and the guardrails in place before the rollout widens.

## 2. Agent PRs are drowning the review queue

**Situation.** Agents open more pull requests than people can read. PRs wait days, then get approved in minutes. Adding reviewers didn't help.

| Step | Command | What you get |
| --- | --- | --- |
| 1 | `/fix-review-queue` | Diagnosis by PR type, risk tiers routed by path, a machine first pass, ownership rules, a PR context template and WIP limits |
| 2 | `/plan-continuous-ai` | Background workflows (CI failure investigation, triage) that take load off reviewers instead of adding to it |
| 3 | `/review-agent-pr` | The new review standard applied to a real PR, with evidence-backed findings |
| 4 | `/mine-rejections` | Recurring review comments turned into rules, hooks and tests so they stop recurring |

**Try:** `/fix-review-queue Agent PRs wait two days, then 1,500-line diffs get approved in five minutes. Adding reviewers didn't help.`

**You end with:** pickup time and review depth matched to risk, and a queue that shrinks instead of growing. In our evals, this skill lifted a small model's answer on this exact problem from 0.05 to 0.57 of the criteria a team needs (see [EVAL-RESULTS.md](EVAL-RESULTS.md)).

## 3. Security asks whether the agents are safe

**Situation.** Agents run with developers' credentials, read tickets and web pages that can carry prompt injection, and install community skills and MCP servers. Security wants an answer, not a ban.

| Step | Command | What you get |
| --- | --- | --- |
| 1 | `/threat-model` | A risk register mapped to the OWASP Top 10 for Agentic Applications, specific to your setup, with validation tests |
| 2 | `/governance-pack` | Managed settings, permission tiers, guardrail hooks and a compliance map (NIST AI RMF, ISO/IEC 42001, EU AI Act) |
| 3 | `/vet-extension` | An install, restrict or reject verdict for each plugin, skill and MCP server in use |
| 4 | `/audit-skills` | The internal skill library reviewed for overlap, triggering and measured value |

**Try:** `/threat-model Claude Code for 40 engineers with their own GitHub tokens, GitHub and Jira MCP servers, community skills allowed, no hooks`

**You end with:** controls security can sign off on, and tests that prove they work.

## 4. Agents build the wrong thing from vague tickets

**Situation.** Agents fill gaps in requirements with plausible guesses. The code works but does the wrong thing, and rework eats the speed gains.

| Step | Command | What you get |
| --- | --- | --- |
| 1 | `/clarify-spec` | The ambiguities, contradictions and silent decisions in the ticket, asked as prioritized questions |
| 2 | `/write-agentic-prd` | An agent-ready spec: intent, non-goals, guardrails, testable acceptance criteria, stop conditions |
| 3 | `/derive-tests` | Tests derived from the acceptance criteria before any code is written |
| 4 | `/verify-change` | The result checked against the Definition of Done with evidence, not claims |

**Try:** `/write-agentic-prd Let admins export audit logs as CSV`

**You end with:** specs an agent can execute without guessing, and proof the result matches them. For larger features, `/spec-feature` runs the full spec-driven loop.

## 5. Leadership wants proof the investment pays off

**Situation.** AI spend is rising and engineers report feeling faster, but nobody can show delivery improved. Research shows perceived and measured speed often diverge.

| Step | Command | What you get |
| --- | --- | --- |
| 1 | `/adlc-assess` | A measurement baseline and the gaps holding results back |
| 2 | Ask: *"How should we measure the ROI of coding agents without self-reported speedups?"* | The `adlc-metrics` skill: outcome, rework and cost-per-change metrics split by agent vs human work |
| 3 | Ask: *"Where is our AI spend going?"* | The `ai-cost-management` skill: spend by team and workflow, and where to cut |
| 4 | `/adlc-roadmap` | Targets and decision gates tied to the metrics |

**You end with:** a dashboard you can defend in a board meeting, and a plan to move its numbers.

## 6. Business teams are building their own apps with AI

**Situation.** Sales, operations and finance build internal tools with Lovable, Claude and other AI builders. Some touch customer data. Banning it would push it underground.

| Step | Command | What you get |
| --- | --- | --- |
| 1 | `/citizen-builder-policy` | A paved road: risk tiers, data rules, an app inventory, and when an app must move to engineering |
| 2 | `/governance-pack` | The citizen-builder rules aligned with the engineering AI policy |
| 3 | `/threat-model` | A focused review for any app that handles customer or financial data |

**Try:** `/citizen-builder-policy 300-person company, about 25 business users building internal apps with Lovable and Claude, two of them touch customer data`

**You end with:** a way to say yes safely, with a clear line where engineering takes over.

## 7. Modernizing a legacy system with agents

**Situation.** A large system with little documentation and few tests needs a rewrite or migration. Agents can do much of the work, but only if behavior is captured first.

| Step | Command | What you get |
| --- | --- | --- |
| 1 | `/map-codebase` | An agent-oriented map: modules, core flows, change recipes, and a risk register |
| 2 | `/modernize` | Behavior characterization, a strategy choice (strangler, rewrite, refactor) and verified migration slices |
| 3 | `/derive-tests` | Characterization tests that lock current behavior before anything changes |
| 4 | `/plan-long-run` | Checkpoints, state files, budgets and abort criteria for multi-day agent work |

**Try:** `/modernize Java 8 monolith, 400k lines, billing module has no tests, target is services on Kubernetes`

**You end with:** a migration that proves each slice behaves like the original before it goes live.

## 8. QA moves from manual regression to verifying agent output

**Situation.** Test cases live in Xray, TestRail or Zephyr, and only some are automated. Agents can write tests fast, but tests written from the implementation pass even when behavior is wrong.

| Step | Command | What you get |
| --- | --- | --- |
| 1 | `/derive-tests` | A traceability matrix from test-case IDs to automated tests, gaps marked, and the missing tests generated |
| 2 | Ask: *"Our agent-written tests pass but billing was wrong in production. How should we test differently?"* | The `behavioral-testing` skill: invariants, property-based tests and mutation testing |
| 3 | `/verify-change` | Evidence that each change meets the Definition of Done |

**Try:** `/derive-tests Here is our Xray export for checkout: 140 cases, about half automated`

**You end with:** coverage you can trace back to requirements, and tests that fail when behavior is wrong.

## 9. Shipping an AI agent as a product

**Situation.** You are building an agent or LLM feature for customers. It needs to be reliable, safe against misuse, and measurable before launch.

| Step | Command | What you get |
| --- | --- | --- |
| 1 | `/design-agent` | The simplest pattern that works, tools, guardrails and an eval plan |
| 2 | `/build-evals` | An eval suite with tasks, graders, thresholds and CI wiring |
| 3 | `/red-team-agent` | Attacks mapped to the OWASP Agentic Top 10, turned into guardrails and new eval cases |
| 4 | `/release-check` | A go/no-go decision with gate evidence and rollback readiness |

**Try:** `/design-agent Support agent that answers order questions and can issue refunds up to $200`

**You end with:** an agent you can measure, defend and roll back.

## 10. Agent work caused an incident

**Situation.** An agent-built change broke something: a dropped column, a leaked secret, a bad migration. The goal is a durable fix, not blame.

| Step | Command | What you get |
| --- | --- | --- |
| 1 | `/agent-postmortem` | A blameless timeline, the contributing factors specific to agent work, and durable fixes |
| 2 | `/codify` | Each fix turned into the right artifact: a context line, a skill, a hook or a test |
| 3 | `/release-check` | The release gates updated so the same failure is caught next time |

**Try:** `/agent-postmortem An agent migration dropped a column in staging; the PR passed CI and review`

**You end with:** the same mistake made impossible, not just less likely.

---

Have a situation that isn't covered? Open a [Discussion](https://github.com/shmulikdav/adlc-skills/discussions) or a skill proposal issue.
