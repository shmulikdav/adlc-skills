---
name: prompt-versioning
description: "Use when prompts or model settings live in dashboards or chats without history, when a prompt or model change broke production behavior, or when setting up a change process for LLM features."
---

# Prompt Versioning (Prompts as Code)

## Purpose

In an LLM feature, the prompt is part of the program. Changing it without version control, review, and tests is deploying untested code to production.

## Practices

1. **Store** prompts, tool descriptions, and model/parameter configs as files in the repo, next to the code that uses them.
2. **Template** with explicit variables; never build prompts by ad-hoc string concatenation spread across files.
3. **Review** prompt changes in PRs like code; the PR includes eval results before vs after.
4. **Pin** model versions explicitly; treat a model upgrade as a change requiring the regression eval suite.
5. **Roll out** risky changes behind a flag or to a percentage of traffic; compare live metrics.
6. **Log** the prompt version and model version with every production run so behavior can be traced.
7. **Rollback** is a config change, not an emergency rewrite.

## Instructions

Audit the current state (where prompts live, how they change, how changes are tested), then propose the target structure, the PR template for prompt changes, and the minimum eval gate.

## Output

Current-state findings, target folder structure, PR template, eval gate thresholds, rollout procedure.
