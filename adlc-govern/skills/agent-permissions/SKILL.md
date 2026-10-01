---
name: agent-permissions
description: "Design least-privilege permission configurations for coding agents: allow/ask/deny rules for tools and shell commands, file and directory boundaries, network access, sandboxing, secrets handling, and per-environment profiles (local, CI, headless). Use when configuring Claude Code settings or permissions, deciding what an agent may run without asking, setting up agents in CI, or after a near-miss with an agent action."
---

# Agent Permissions (Least Privilege)

## Purpose

Permission prompts that fire constantly get approved blindly. Permissions that are too broad let a single bad step do real damage. The goal is a configuration where routine safe actions flow and dangerous ones are impossible or explicitly approved.

## Design steps

1. **Inventory actions** the agent needs for the team's task types: read/edit paths, test/lint/build commands, git operations, package installs, network calls, deploys.
2. **Classify each:**
   - **Allow** — read-only or easily reversible, inside the repo (run tests, lint, git status/diff, read files)
   - **Ask** — side effects that are reversible but notable (install packages, git push to a branch, run migrations locally)
   - **Deny** — irreversible or out of scope (read secrets files, `rm -rf` outside workspace, push to main, production credentials, curl to arbitrary hosts)
3. **Bound the filesystem:** deny reads of `.env*`, key files, credential directories; restrict edits to the workspace.
4. **Profiles:** local interactive (more ask), CI/headless (no ask possible → narrow allow-list, sandboxed container, scoped token), and review-only (read-only).
5. **Secrets:** inject at runtime through environment or secret managers the agent cannot read back; never paste them into prompts or context files.
6. **Back it with enforcement:** where a rule must never be broken, add a hook or CI check in addition to the permission rule.

## Output

A permissions matrix (`Action | Local | CI | Rationale`), a draft settings snippet for the team's tool (e.g., a Claude Code `.claude/settings.json` permissions block), and a list of rules that also need hooks.

## Notes

- Check the exact rule syntax against the tool's current documentation before rollout; formats evolve.
- Review permissions after every incident or near-miss.

---

### Further Reading

- [Claude Code documentation (settings, permissions, hooks)](https://code.claude.com/docs/en/best-practices)
- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
