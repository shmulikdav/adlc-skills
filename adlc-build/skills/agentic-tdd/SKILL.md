---
name: agentic-tdd
description: "Test-driven development with coding agents: write failing tests from acceptance criteria first, confirm they fail for the right reason, commit them, then have the agent implement until green without modifying the tests. Use when correctness matters, when an agent tends to write tests that just mirror its implementation, or when the user asks for TDD with Claude Code, Cursor, or Codex."
---

# Agentic TDD

## Purpose

Tests written after the code by the same agent tend to encode whatever the code does. Tests written first, from the spec, give the agent an external oracle to work against.

## Instructions

1. **Derive tests from acceptance criteria**, not from imagined implementation. One or more tests per AC; include negative and boundary cases.
2. **Run them and confirm they fail** for the expected reason (missing function, wrong behavior), not for setup errors.
3. **Human review of tests** (short): do they express the intended behavior? Are any asserting implementation details?
4. **Commit the tests** separately. This freezes the contract.
5. **Implement**: instruct the agent to make the tests pass *without modifying the tests*. If a test seems wrong, the agent must stop and explain rather than edit it.
6. **Iterate until green**, then run the broader suite for regressions.
7. **Refactor** with tests green; keep behavior unchanged.

## Guardrails

- Watch for test tampering: weakened assertions, skipped tests, mocks that bypass the behavior under test, special-casing test inputs in production code.
- Check that the diff to test files after step 4 is empty, or that every change was explicitly approved.

## Output

Test files, a short mapping `AC → test name`, and the final run results.

---

### Further Reading

- [Claude Code best practices](https://code.claude.com/docs/en/best-practices)
