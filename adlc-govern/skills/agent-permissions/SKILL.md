---
name: agent-permissions
description: "Use when configuring what a coding agent may read, edit, or run (Claude Code settings, permissions, sandboxing), deciding what runs without approval, setting up agents in CI or headless mode, or after a near-miss with an agent action."
---

# Agent Permissions (Least Privilege)

**Grounded in:** NIST SP 800-207: Zero Trust Architecture; OWASP Top 10 for Agentic Applications (2026); Claude Code best practices.





## Purpose

Permission prompts that fire constantly get approved blindly. Permissions that are too broad let a single bad step do real damage. The goal is a configuration where routine safe actions flow and dangerous ones are impossible or explicitly approved.

## The 2026 baseline: classifier-based auto mode

Static allow/ask/deny lists are no longer the whole picture. Since August 2026, Claude Code starts new Pro, Max, and Team sessions in **auto mode**, where a classifier reviews actions and blocks risky ones instead of prompting for each. That shifts the design question from "which commands need a prompt" to:

- Which **custom rules** extend the built-in classifier list (keep the defaults and add your own, rather than replacing them)
- Whether **all shell commands** go through the classifier, or only arbitrary-code-execution patterns
- Which **network hosts** each command may reach when sandboxed
- What **managed settings** the organization enforces so individuals can't loosen them

Deny rules and hooks still matter: auto mode reduces prompt fatigue, but deterministic rules remain the backstop for anything that must never happen. Check current setting names in the Claude Code permissions and auto-mode documentation before rollout; they change frequently.

## Design steps

1. **Inventory actions** the agent needs for the team's task types: read/edit paths, test/lint/build commands, git operations, package installs, network calls, deploys.
2. **Classify each:**
   - **Allow** — read-only or easily reversible, inside the repo (run tests, lint, git status/diff, read files)
   - **Ask** — side effects that are reversible but notable (install packages, git push to a branch, run migrations locally)
   - **Deny** — irreversible or out of scope (read secrets files, `rm -rf` outside workspace, push to main, production credentials, curl to arbitrary hosts)
3. **Bound the filesystem:** deny reads of `.env*`, key files, credential directories; restrict edits to the workspace.
4. **Profiles:** local interactive (auto mode with org rules, or ask for high-risk repos), CI/headless (no ask possible → narrow allow-list, sandboxed container, scoped token, network allow-list), and review-only (read-only).
5. **Secrets:** inject at runtime through environment or secret managers the agent cannot read back; never paste them into prompts or context files.
6. **Back it with enforcement:** where a rule must never be broken, add a hook or CI check in addition to the permission rule.

## Red flags

| Thought | Reality |
|---------|---------|
| "Approve-all is faster" | Blanket approval removes the only check between a bad step and real damage |
| "It's only the dev environment" | Dev machines hold credentials, SSH keys, and tokens to production systems |
| "The instruction in CLAUDE.md says not to" | Instructions are probabilistic; deny rules and hooks are not |

## Output

A permissions matrix (`Action | Local | CI | Rationale`), a draft settings snippet for the team's tool (e.g., a Claude Code `.claude/settings.json` permissions block), and a list of rules that also need hooks.

## Notes

- Check the exact rule syntax against the tool's current documentation before rollout; formats evolve.
- Review permissions after every incident or near-miss.

---

### Further Reading

- [Claude Code documentation (settings, permissions, hooks)](https://code.claude.com/docs/en/best-practices)
- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
