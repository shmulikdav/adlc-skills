---
name: guardrail-hooks
description: "Design deterministic guardrails for coding agents with lifecycle hooks: block edits to protected files, block dangerous commands, auto-format and lint after edits, run tests before stop, log every tool call for audit. Use when a rule must be enforced every time rather than remembered, when setting up Claude Code hooks, or when instructions in CLAUDE.md are not being followed reliably."
---

# Guardrail Hooks

## Purpose

Instructions are probabilistic; hooks are deterministic. Anything whose violation is costly should be enforced by a hook, a linter, or CI, not only by a sentence in a context file.

## Common guardrails

| Guardrail | Event | Behavior |
|-----------|-------|----------|
| Protected paths | Before file edit/write | Block edits to `.env*`, secrets, lockfiles, migrations already applied, CI config |
| Dangerous commands | Before shell command | Block `rm -rf` outside workspace, force-push, `curl | sh`, production CLIs |
| Format & lint | After file edit | Run the formatter/linter on changed files |
| Test gate | Before the agent stops | Run fast tests; if failing, report back so the agent keeps working |
| Audit log | After any tool call | Append tool name, inputs (redacted), and timestamp to a log |
| Secret scan | Before commit | Run a secret scanner on the staged diff |

## Instructions

1. List the rules that must never be broken and the routine actions that should always happen.
2. Map each to a hook event and a script. Keep scripts small, fast, and readable; output a clear reason when blocking so the agent can adjust.
3. Decide scope: project hooks checked into the repo (reviewed in PRs) vs user-level hooks.
4. Test each hook with a deliberate violation.
5. Document the hooks in the context file in one line each so humans know they exist.

## Example (Claude Code hooks config, block edits to protected files)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-paths.sh" }
        ]
      }
    ]
  }
}
```

A ready-to-adapt script lives in this repo under `templates/hooks/`. Verify event names and the blocking exit-code contract against the current hooks documentation before deploying.

## Notes

- Hooks run with the user's permissions. Review hook scripts like production code; never install hooks from untrusted sources.
- Hooks should fail closed for security rules and fail open (warn) for convenience rules.

---

### Further Reading

- [Claude Code best practices](https://code.claude.com/docs/en/best-practices)
- [Claude Code plugins reference (hooks)](https://code.claude.com/docs/en/plugins-reference)
