---
name: ai-stance-policy
description: "Use when an engineering organization needs an AI usage or acceptable-use policy for developers and coding agents, when teams are unsure which tools or data are allowed, or before announcing an AI rollout."
---

# AI Stance & Usage Policy (Engineering)

**Grounded in:** DORA research (State of AI-assisted Software Development, AI Capabilities Model); ISO/IEC 42001 AI management system; NIST AI Risk Management Framework.





## Purpose

Ambiguity creates risk and slows adoption. DORA's 2025 research names a clear, communicated AI stance as one of seven capabilities that amplify AI's benefits. This skill drafts a short, enforceable policy people will actually read.

## Instructions

1. Gather: industry and regulatory context, data types handled (PII, PHI, payment, source code of customers), approved vendors and contracts (zero data retention? enterprise tier?), existing security policies.
2. Draft the policy with these sections, in plain language. The policy must fit on one page (about 400 words): cut before you add, and link to existing security standards instead of restating them.

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

3. Mark every item that needs legal or compliance review with **[LEGAL]**.
4. Offer, don't add: after the policy, offer in one line each the gray-area **decision table** (e.g., "Can I paste a customer log into the agent?") and a one-paragraph **announcement message** for leadership. Write them only if asked, so the policy itself stays short.

## Output

The one-page policy in the template above, with **[LEGAL]** markers, followed by a single line offering the decision table and the announcement.

## Notes

- Short beats complete. Link to detailed security standards instead of copying them.
- State expectations, not just restrictions: e.g., "we expect every engineer to use agents for test generation".
- An organizational AI policy is also a core requirement of ISO/IEC 42001 (AI management systems), so this document doubles as a starting point for certification.
- Align with any external framework the company follows (ISO/IEC 42001, EU AI Act obligations, SOC 2 controls) in the appendix, not the core.
- This is not legal advice; flag sections that need legal review.

---

### Further Reading

- [DORA AI Capabilities Model](https://dora.dev/research/publications/)
- [ISO/IEC 42001 AI management system](https://www.iso.org/standard/81230.html)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
