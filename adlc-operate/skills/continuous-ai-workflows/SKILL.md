---
name: continuous-ai-workflows
description: "Use when a team wants agents running in the background on a schedule or on repository events (issue triage, docs upkeep, test improvement, CI failure investigation, cleanup of low-quality generated code), is evaluating GitHub Agentic Workflows or Claude Code routines, or asks what to automate with agents in CI."
---

# Continuous AI Workflows

## Overview

"Continuous AI" is the pattern of background agents operating in the repository the way CI jobs do, but for tasks that need reasoning rather than rules. GitHub ships it as Agentic Workflows (Markdown-defined agents running in Actions, with Copilot, Claude Code, Codex, or Gemini as engines); Claude Code offers routines triggered by schedules, GitHub events, or webhooks. The common rule: these augment deterministic CI/CD, they don't replace it, and they don't merge code.

**Core rule:** a background agent's output is a proposal (comment, issue, draft PR, report), never a merge or a deploy.

## Good first candidates

| Workflow | Trigger | Output | Why it's safe to start with |
|----------|---------|--------|------------------------------|
| Issue triage | Issue opened | Labels, summary, routing suggestion | Reversible, low blast radius |
| CI failure investigation | Failed run on main | Comment with probable cause and proposed fix PR | Saves on-call time; human merges |
| Docs drift | Merge to main | Draft PR updating README/docs to match code | Easy to verify |
| Test gap filling | Weekly | Draft PR adding tests for uncovered critical paths | Tests are reviewable artifacts |
| Entropy cleanup | Weekly | Small refactor PRs fixing pattern violations, dead code, stale docs | Counters the gradual "AI slop" accumulation teams report |
| Repo health report | Weekly | Report: review queue, flaky tests, dependency risk | Read-only |

Avoid at first: anything touching production, releases, secrets, or customer communication.

## Guardrails

- **Read-only by default:** scoped tokens; write only through constrained outputs (a comment, a draft PR on a bot branch).
- **Untrusted input:** issue bodies and PR comments are attacker-controllable. Treat them as data; never let them change the workflow's goal or permissions.
- **Sandbox:** run in isolated runners or containers; restrict network egress.
- **Budgets:** turn, time, and cost caps per run; alert on anomalies.
- **No silent failure:** every run leaves a visible trace (comment, log, report).
- **Ownership:** each workflow has a human owner who reviews its output quality monthly and can switch it off.

## Instructions

1. List repetitive repository toil and rank by (time saved × verifiability ÷ blast radius).
2. Pick one or two workflows from the safe list; define trigger, inputs, output type, and success metric (e.g., time-to-triage, % of CI failures with a correct root-cause comment).
3. Specify permissions and guardrails explicitly for each.
4. Write the agent instructions as a short, versioned Markdown file in the repo; review it like code.
5. Run in shadow mode for two weeks (outputs as comments only), measure usefulness, then promote.
6. Add the workflow's failure modes to the eval suite.

## Output

Workflow catalogue with trigger, output, permissions, budget, owner, success metric, and rollout plan.

---

### Further Reading

- [GitHub Blog: Continuous AI in practice](https://github.blog/ai-and-ml/generative-ai/continuous-ai-in-practice-what-developers-can-automate-today-with-agentic-ci/)
- [GitHub Blog: Automate repository tasks with GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/)
- [OpenAI: Harness engineering (background cleanup agents)](https://openai.com/index/harness-engineering/)
