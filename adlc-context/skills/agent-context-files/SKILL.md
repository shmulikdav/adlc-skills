---
name: agent-context-files
description: "Use when setting up or auditing CLAUDE.md, AGENTS.md, .cursor/rules, or Copilot instructions for a repository, when an agent keeps repeating the same project-specific mistake, or when a context file has grown long and is being ignored."
---

# Agent Context Files

## Purpose

Context files are loaded every session, so every line costs attention. Bloated files cause agents to ignore the instructions that matter. The goal is the smallest file that prevents the most expensive mistakes.

## What belongs (and what does not)

| Include | Exclude |
|---------|---------|
| Build/test/lint commands the agent can't guess | Anything obvious from reading code |
| Conventions that differ from language defaults | Standard language style rules |
| Architecture boundaries ("UI never calls DB directly") | Long tutorials or API docs (link them) |
| Repo-specific gotchas and footguns | Secrets, URLs with tokens, personal data |
| Where key things live (paths) | Rules that only apply to one folder (use a nested file) |
| How to verify a change is done | Aspirational rules nobody enforces |

## Structure

```markdown
# [Project] — agent context

## Commands
- Install: ...   Test: ...   Single test: ...   Lint/types: ...

## Architecture (5–10 lines)
## Conventions that differ from defaults
## Boundaries — never do
## Verification — before saying "done"
## Pointers
- Domain glossary: docs/glossary.md
- ADRs: docs/adr/
```

Target: under ~150 lines for the root file. Treat it as a **table of contents, not an encyclopedia**: point to a structured `docs/` knowledge base (architecture, ADRs, plans, runbooks) that is the versioned system of record. What the agent can't see in the repository doesn't exist for it, so decisions made in chat or meetings must land in `docs/`. Use nested files in subdirectories for area-specific rules, and imports (`@path/to/file`) for occasionally-needed detail.

## Instructions

**Create mode**
1. Inspect the repo: package/build files, CI config, test setup, folder structure, README, existing rule files.
2. Draft the file using only facts found in the repo; mark anything inferred with `(verify)`.
3. Ask the user for the 3–5 things that most often go wrong when someone new works in this repo; add them as boundaries.

**Audit mode**
1. Score each line: *prevents a real mistake* / *derivable from code* / *stale* / *contradictory*.
2. Propose cuts, merges, and moves to nested files. Show a before/after line count.
3. Check cross-tool consistency: AGENTS.md is the cross-tool convention (Codex, Cursor, Copilot, and recent Claude Code versions read it). Keep one source of truth and make the other a pointer or symlink, so tools never see conflicting rules.

## Notes

- Treat the context file like code: review it in PRs, prune it, test changes by observing whether agent behavior shifts.
- For capturing session learnings into CLAUDE.md over time, Anthropic's official `claude-md-management` plugin complements this skill.
- When an agent makes the same mistake twice, the fix belongs in the context file or a skill, not in the next prompt.

---

### Further Reading

- [Claude Code best practices: write an effective CLAUDE.md](https://code.claude.com/docs/en/best-practices)
- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
