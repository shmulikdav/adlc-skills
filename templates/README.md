# Templates

Opt-in building blocks referenced by the skills. Nothing here is activated when you install the plugins — copy what you need into your own repo and review it first.

| Path | Used by | What it is |
|------|---------|-----------|
| `hooks/protect-paths.sh` | `adlc-govern:guardrail-hooks` | PreToolUse hook that blocks agent edits to secrets, CI config, lockfiles, applied migrations |
| `hooks/settings.example.json` | `adlc-govern:guardrail-hooks` | Example `.claude/settings.json` wiring for the hook |
| `CLAUDE.template.md` | `adlc-context:agent-context-files` | Minimal agent context file skeleton |
| `agent-spec.template.md` | `adlc-intent:agentic-prd` | Agentic PRD / Agent Execution Spec skeleton |

Copy the hook into your project:

```bash
mkdir -p .claude/hooks
cp templates/hooks/protect-paths.sh .claude/hooks/
# merge templates/hooks/settings.example.json into .claude/settings.json
```

Test it with a deliberate violation (ask the agent to edit `.env`) before relying on it.
