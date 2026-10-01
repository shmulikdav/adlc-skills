---
name: ai-cost-management
description: "Use when token or AI spend is growing or unpredictable, when building an AI cost dashboard, pricing an AI feature, or checking whether an agent workflow or feature is economically viable."
---

# AI Cost Management

## Purpose

Agent costs scale with context size, steps, and retries, not with headcount. Without unit economics, spend grows silently and ROI claims are guesses.

## Unit metrics

- Development: cost per merged agent-authored PR; cost per resolved ticket by task type; licence + usage cost per active engineer
- Product: cost per agent run, per successful outcome, per customer/tenant; gross margin per AI feature

## Levers

| Lever | Effect | Watch out for |
|-------|--------|---------------|
| Model routing (small model for simple steps) | Large savings on routine steps | Quality drop on misrouted tasks — measure with evals |
| Prompt/context caching | Cuts repeated context cost | Cache invalidation when context changes |
| Context trimming | Fewer input tokens, often better quality | Removing context the task needed |
| Step limits & loop detection | Prevents runaway runs | Cutting off legitimately long tasks |
| Batch/async processing | Lower price for non-urgent work | Latency |

## Instructions

1. Establish attribution: tag usage by team, workflow, feature, and customer.
2. Compute current unit costs and trend.
3. Identify the top cost drivers (workflow × model × step).
4. Propose levers with expected savings and a quality guardrail for each.
5. Run a **stress test**: unit economics if token prices or usage per outcome rise 2× and 5×; flag features that become margin-negative.
6. Set budgets and alerts (per team, per workflow, per run anomaly).

## Output

Cost baseline table, driver analysis, lever plan with guardrails, stress-test table, budget/alert policy.
