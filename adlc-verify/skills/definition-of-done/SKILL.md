---
name: definition-of-done
description: "Use when agents claim work is done prematurely, when standardizing the quality bar for agent-authored changes across teams, or when writing the verification section of a context file or PR template."
---

# Definition of Done for Agent Work

## Purpose

"Done" must mean verified, with evidence, not "the agent stopped". A written DoD gives agents a checklist they can execute and reviewers a standard they can enforce.

## Red flags

| Claim or thought | Reality |
|------------------|---------|
| "Tests should pass now" | Run them. A claim without fresh output is not evidence |
| "The agent reported success" | Check the diff and run the checks independently |
| "Linter is clean, so it builds" | Linting is not compiling, and compiling is not behavior |
| "It's a small change, skip the checklist" | Small changes to auth, money, or data are where incidents start |

## Template

```markdown
## Definition of Done (agent-authored changes)

### Agent must verify (and paste evidence)
- [ ] All acceptance criteria mapped to tests; tests pass (command + summary output)
- [ ] Full relevant test suite passes; no new skipped tests
- [ ] Type check and lint clean
- [ ] No new dependencies without approval; existing ones verified (hallucination checks)
- [ ] No secrets, keys, or personal data in code, logs, or fixtures
- [ ] Docs/changelog updated if behavior changed
- [ ] Diff limited to the planned scope; deviations listed

### Human gates
- [ ] Alignment review completed
- [ ] Security review for auth, payments, data export, infra changes
- [ ] Product owner sign-off for user-visible behavior changes
```

## Instructions

1. Start from the template; adapt to the stack (commands, tools) and the team's risk profile.
2. Split items into *automatable* (hooks/CI) and *judgment* (human gates). Automate everything automatable.
3. Produce a short version for the context file's "Verification" section and the full version for the team handbook.

---

### Further Reading

- [Claude Code best practices: provide verification](https://code.claude.com/docs/en/best-practices)
