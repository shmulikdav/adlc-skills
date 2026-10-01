---
name: derive-tests
description: "Run the ADLC derive-tests workflow: build a traceability matrix from specs or test cases and generate the missing tests. Use when the user invokes $derive-tests or asks for this workflow end to end."
---

> Generated from the Claude Code command `/derive-tests` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $derive-tests -- Tests from Specs

## Invocation

```
$derive-tests specs/012-audit-export/spec.md
$derive-tests [attach Xray / TestRail export]
```

## Workflow

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-verify:tests-from-specs`, `adlc-verify:behavioral-testing`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Parse sources
Read the user's request and extract criteria or test cases with IDs.

### Step 2: Traceability
Apply **tests-from-specs** to inventory existing tests and build the matrix.

### Step 3: Strengthen
Apply **behavioral-testing** to add invariants, contracts, and permission-matrix tests for high-risk areas.

### Step 4: Generate and run
Write missing tests in the project's style, run them, and report results.

### Step 5: Output
Matrix, new tests, results, and criteria to rewrite.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$verify-change`: run the new tests against the change
- `$review-agent-pr`: review with the coverage map attached
