---
name: context-budget
description: "Use when agent quality drops during long sessions, sessions run out of context, work must continue across sessions, or when deciding what belongs in CLAUDE.md vs a skill vs a subagent vs a linked document."
---

# Context Budget Management

## Purpose

Agent performance degrades as the context window fills. Most agentic best practices reduce to one discipline: put the right tokens in context at the right time.

## The layering model

| Layer | Loaded | Use for |
|-------|--------|---------|
| Context file (CLAUDE.md/AGENTS.md) | Every session | Short, universal rules and commands |
| Skills | Description always; body when relevant | Procedures and domain knowledge needed sometimes |
| Referenced docs (`@file`, links) | On demand | Detailed specs, ADRs, API docs |
| Subagents | Separate window; return a summary | Exploration, search, review, research |
| State files (plan.md, progress.md, tasks.md) | Read at session start | Continuity across sessions |

## Practices

1. **One task per session.** Clear context between unrelated tasks.
2. **Explore in a subagent** when it requires reading many files; bring back only the conclusions.
3. **Externalize state.** Before a long task, write `plan.md`; update `progress.md` after each step so a fresh session can resume.
4. **Correct early.** If the agent goes off track twice, stop, clear, and restart with a better prompt rather than piling corrections into context.
5. **Prefer pointers to pastes.** Reference file paths and let the agent read what it needs.
6. **Watch for symptoms:** forgotten instructions, repeated mistakes, re-reading the same files, contradicting earlier decisions.

## Instructions

When asked to diagnose a context problem: identify what is in context (context file length, skills, pasted material, session length), find what is loaded but rarely needed, and propose moves between layers. When designing a long-running task: produce the plan/progress file structure and a session-handoff checklist.

## Output

A short diagnosis or design with a table: `Content | Current layer | Recommended layer | Reason`.

---

### Further Reading

- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Claude Code best practices](https://code.claude.com/docs/en/best-practices)
