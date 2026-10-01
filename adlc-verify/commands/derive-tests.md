---
name: derive-tests
description: Build a traceability matrix from specs or test cases and generate the missing tests
argument-hint: "<spec, acceptance criteria, or exported test cases>"
---

# /derive-tests -- Tests from Specs

## Invocation

```
/derive-tests specs/012-audit-export/spec.md
/derive-tests [attach Xray / TestRail export]
```

## Workflow

### Step 0: Load the method
Your first action must be a Skill tool call for each of these skills: `adlc-verify:tests-from-specs`, `adlc-verify:behavioral-testing`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Parse sources
Read $ARGUMENTS and extract criteria or test cases with IDs.

### Step 2: Traceability
Apply **tests-from-specs** to inventory existing tests and build the matrix.

### Step 3: Strengthen
Apply **behavioral-testing** to add invariants, contracts, and permission-matrix tests for high-risk areas.

### Step 4: Generate and run
Write missing tests in the project's style, run them, and report results.

### Step 5: Output
Matrix, new tests, results, and criteria to rewrite.
