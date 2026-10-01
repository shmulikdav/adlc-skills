---
name: ai-stance-policy
description: "Draft a clear, communicated AI stance for an engineering organization: approved tools, data classification rules for prompts, what agents may and may not do, code ownership and review expectations, IP and licensing, and how the policy evolves. Use when a company needs an AI usage policy for developers, an acceptable-use policy for coding agents, or when teams are unsure what is allowed."
---

# AI Stance & Usage Policy (Engineering)

## Purpose

Ambiguity creates risk and slows adoption. DORA's 2025 research names a clear, communicated AI stance as one of seven capabilities that amplify AI's benefits. This skill drafts a short, enforceable policy people will actually read.

## Instructions

1. Gather: industry and regulatory context, data types handled (PII, PHI, payment, source code of customers), approved vendors and contracts (zero data retention? enterprise tier?), existing security policies.
2. Draft the policy with these sections, each in plain language, max one page total for the core:

```
# AI Stance — [Company] Engineering

## Our position (3 sentences)
Why we use AI agents, what we expect, what we will not compromise.

## Approved tools
Tool | Approved use | Account type | Owner

## Data rules
Allowed in prompts / context: ...
Never in prompts / context: secrets, credentials, customer PII unless [approved path], ...

## What agents may do
- Read code in [scope]; run tests; open PRs ...

## What requires a human
- Merging to main, production changes, schema migrations, auth/billing code, external communications ...

## Ownership
The human who merges owns the code. "The agent wrote it" is not an explanation.

## Disclosure
How AI-generated changes are labeled in PRs/commits.

## Extensions (MCP servers, skills, plugins)
Only from the approved list; request process: ...

## How this policy changes
Owner, review cadence, feedback channel.
```

3. Add an appendix with a **decision table** for gray areas (e.g., "Can I paste a customer log into the agent?").
4. Add a one-paragraph **announcement message** leadership can send.

## Notes

- Short beats complete. Link to detailed security standards instead of copying them.
- State expectations, not just restrictions: e.g., "we expect every engineer to use agents for test generation".
- Align with any external framework the company follows (ISO/IEC 42001, EU AI Act obligations, SOC 2 controls) in the appendix, not the core.
- This is not legal advice; flag sections that need legal review.

---

### Further Reading

- [DORA AI Capabilities Model](https://dora.dev/research/publications/)
