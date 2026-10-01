---
name: tests-from-specs
description: "Use when generating tests from PRDs, acceptance criteria, Gherkin, or test-management exports (Xray, TestRail, Zephyr), when asked which requirements have no test, or when lifting test coverage with agents."
---

# Tests from Specs

## Purpose

Coverage percentages say which lines ran. Traceability says which promises are verified. This skill builds the second.

## Instructions

1. **Collect sources:** spec/PRD acceptance criteria, user stories, Gherkin features, or exported test cases from a test-management tool (Xray, TestRail, Zephyr). Parse steps, expected results, and preconditions.
2. **Inventory existing tests:** search the repo; map tests to criteria by name, docstring, or behavior.
3. **Build the traceability matrix:**

```
| AC / Test case ID | Requirement | Existing test(s) | Status: Verified / Proposed / Gap | Level: unit / integration / e2e |
```

4. **Generate missing tests** at the lowest level that can verify the behavior. Use the project's framework and conventions; mirror an existing test file's style.
5. **Flag untestable criteria** and propose a rewrite of the criterion.
6. **Run** the new tests; report pass/fail. Failing tests on existing code are findings, not test bugs, until investigated.

## Output

Traceability matrix, new test files, run results, and a list of criteria that need rewriting.

## Notes

- When test cases come from a test-management system, keep their IDs in test names or annotations so results can be pushed back.
- Never mark a criterion Verified on the basis of a test you didn't run.
