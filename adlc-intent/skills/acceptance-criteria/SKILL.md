---
name: acceptance-criteria
description: "Use when writing or fixing acceptance criteria for a feature an agent will build or test, when criteria are vague or untestable, or before generating tests from a spec or user story."
---

# Acceptance Criteria for Agents

**Grounded in:** EARS: Easy Approach to Requirements Syntax; Cucumber: Gherkin reference.





## Purpose

Acceptance criteria are the contract between intent and verification. For agents, an untestable criterion is an invitation to guess.

## Formats

**Given/When/Then** for behavior scenarios:
```
AC-3: Given a logged-in user with an expired card
      When they start checkout
      Then they see the "update payment method" step before order review
      And no charge attempt is made
```

**EARS** (Easy Approach to Requirements Syntax) for system rules:
- Ubiquitous: *The system shall* log every failed login attempt.
- Event-driven: *When* a file over 10 MB is uploaded, *the system shall* reject it with error code FILE_TOO_LARGE.
- State-driven: *While* the account is suspended, *the system shall* block API writes.
- Unwanted behavior: *If* the payment provider times out, *then the system shall* retry once and show a pending state.
- Optional feature: *Where* SSO is enabled, *the system shall* hide the password field.

## Instructions

1. Extract each behavior from the input (story, PRD, ticket).
2. Write at least: one happy path, one boundary case, one negative/error path, and any security or permission rule.
3. Replace adjectives with numbers ("fast" → "p95 < 300 ms at 50 rps").
4. For each AC, specify **verification**: unit test, integration test, E2E, manual check, or metric. Prefer automated.
5. Add an ID (AC-n) and trace it to the requirement it covers.
6. Run the quality check below and fix failures.

## Quality checklist

- [ ] Each AC has exactly one expected outcome
- [ ] No implementation details unless they are true constraints
- [ ] No vague words without thresholds
- [ ] Negative and permission paths covered
- [ ] Every requirement has ≥ 1 AC; every AC has a verification method

## Output

A table: `ID | Requirement | Criterion | Type (happy/edge/negative/NFR) | Verification`.

---

### Further Reading

- [GitHub Spec Kit: Specification-Driven Development](https://github.com/github/spec-kit/blob/main/spec-driven.md)
- [EARS: Easy Approach to Requirements Syntax](https://alistairmavin.com/ears/)
- [Cucumber: Gherkin reference](https://cucumber.io/docs/gherkin/reference/)
