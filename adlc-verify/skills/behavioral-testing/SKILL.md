---
name: behavioral-testing
description: "Design behavioral validation for agent-built software: test what the system does across the input range (properties, invariants, contracts, state transitions) rather than matching the agent's own implementation. Use when building a test strategy for AI-generated code, when tests pass but behavior is wrong, or when QA needs to shift from manual regression to verifying agent output."
---

# Behavioral Testing

## Purpose

In the ADLC, the main failure mode is plausible-but-wrong output. Example-based tests that mirror the implementation won't catch it. Behavioral testing checks the properties the system must always hold.

## Techniques

| Technique | Catches | Example |
|-----------|---------|---------|
| Contract tests | Interface drift between services | API response matches OpenAPI schema |
| Property-based tests | Edge cases nobody thought of | `decode(encode(x)) == x` for generated x |
| Invariant checks | Silent data corruption | Account balance never negative; totals equal sum of lines |
| State-transition tests | Illegal workflows | Cannot ship an unpaid order |
| Metamorphic tests | Logic errors without an oracle | Sorting then filtering = filtering then sorting |
| Characterization tests | Unintended behavior change | Golden outputs from current system |
| Permission matrix tests | Authorization gaps | Every role × action combination |

## Instructions

1. From the spec, extract invariants, state machines, contracts, and the permission matrix.
2. Choose techniques per risk area (money, permissions, data integrity get the strongest).
3. Write a test plan: `Area | Property/invariant | Technique | Example inputs | Priority`.
4. Generate tests, ensuring they would fail on a plausible wrong implementation. For each test, state one realistic bug it catches.
5. Integrate into CI so the agent runs them locally before claiming done.

## Notes

- A test the agent cannot run locally does not guide the agent. Keep the fast suite fast.
- Mutation testing on critical modules measures whether the suite would notice a wrong implementation.
