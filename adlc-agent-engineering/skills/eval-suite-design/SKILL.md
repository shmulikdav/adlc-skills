---
name: eval-suite-design
description: "Use when building evals for an agent or LLM feature, before changing models or prompts, when moving an agent from demo to production, or when asked how to know the agent got better or worse."
---

# Eval Suite Design

**Grounded in:** Anthropic: Demystifying evals for AI agents; NIST AI Risk Management Framework.





## Purpose

Without evals, every prompt or model change is a guess and quality is judged by vibes. Evals turn agent quality into a number a team can act on, and they become the regression net for every future change.

## Building blocks

- **Task:** an input/scenario with clear success criteria
- **Trial:** one run of the agent on a task (run several; agents are non-deterministic)
- **Transcript:** the full record of steps and tool calls
- **Outcome:** the end state (files, DB records, response) — grade outcomes over paths
- **Grader:** logic that scores the outcome
- **Suite:** a set of related tasks

## Graders

| Type | Examples | Strength | Weakness |
|------|----------|----------|----------|
| Code-based | Unit tests, exact/regex match, schema validation, state checks | Fast, objective, cheap | Brittle to valid variations |
| Model-based | Rubric scoring by an LLM, pairwise comparison | Handles nuance at scale | Needs calibration against humans |
| Human | Expert review, A/B tests | Gold standard | Slow, expensive |

## Capability vs regression

- **Capability evals:** "Can it do this yet?" — hard tasks, low initial pass rate, guide improvement.
- **Regression evals:** "Does it still do this?" — near 100% pass, run on every change, gate releases.
- Graduate stable capability tasks into the regression suite.

## Instructions

1. Start small: 20–50 tasks drawn from real usage, real failures, and the spec's acceptance criteria. Include incidents and edge cases.
2. Write success criteria per task before running anything.
3. Choose graders per task; prefer outcome/state checks; calibrate model graders against a human-labeled sample.
4. Run multiple trials; report pass rate and consistency (e.g., pass@k and pass^k style reliability).
5. Read transcripts regularly to catch grader bugs and lucky passes.
6. Wire the regression suite into CI with thresholds; keep capability evals as a tracked dashboard.
7. Watch for saturation: when a suite nears 100%, add harder tasks.

## Output

Eval plan (task taxonomy, grader per task, thresholds), a task file format (YAML/JSONL) with 5–10 example tasks, and CI integration notes.

---

### Further Reading

- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
