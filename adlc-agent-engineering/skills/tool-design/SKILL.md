---
name: tool-design
description: "Use when building function-calling tools or an MCP server for agents, when an agent misuses, ignores, or loops on a tool, or when reviewing an agent's tool set."
---

# Tool Design for Agents

## Purpose

Tools are the agent's interface to the world. A tool designed like a thin wrapper around an internal API forces the agent to do the API's job. A tool designed for the agent's task gets used correctly.

## Principles

1. **Task-shaped, not API-shaped.** One tool that "schedules a meeting" beats three that list users, list events, and create events, when that's what the task needs.
2. **Names and descriptions are prompts.** Say what it does, when to use it, when not to, and what it returns. Namespace related tools consistently.
3. **Few, typed, explicit parameters.** Use enums and formats; avoid ambiguous names (`user` → `user_email`).
4. **Responses for a reader with limited context.** Return the fields needed for the next decision, human-readable identifiers, and a concise mode by default; paginate and truncate with guidance.
5. **Errors that teach.** "Date must be ISO 8601, e.g. 2026-10-01" beats "400 Bad Request".
6. **Side effects are explicit.** Separate read and write tools; support dry-run; make writes idempotent where possible; require confirmation for irreversible actions.
7. **Least privilege.** Each tool gets only the scope it needs.

## Instructions

When designing: list the agent's tasks → derive the minimal tool set → write each spec (name, description, params schema, response shape, errors, side effects, permissions) → write 3 test prompts per tool to check selection and usage.

When reviewing: score each tool on the principles above and propose rewrites of names, descriptions, and response shapes.

## Output

`| Tool | Purpose | Params | Returns | Side effects | Errors | Permission scope |` plus full specs.

---

### Further Reading

- [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
