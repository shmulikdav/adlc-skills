---
name: small-batch-delivery
description: "Use when agent-generated pull requests are too large to review, review time is ballooning, a team asks how to keep AI-assisted delivery stable, or when writing PR policies for agent-authored changes."
---

# Small-Batch Delivery

## Purpose

Agents make large changes cheap to produce but not cheap to review or roll back. DORA's research highlights working in small batches as a capability that amplifies AI benefits; it counters AI's tendency to enable larger, riskier changes.

## Practices

1. **PR budget:** target ≤ ~300 changed lines of non-generated code and one concern per PR. Generated files and lockfiles are listed separately.
2. **Stacked PRs** for larger features: contract/tests → core → integration → UI, each reviewable alone.
3. **Feature flags** so incomplete work can merge dark; define the flag removal task at creation.
4. **Trunk-based integration:** short-lived branches (≤ 1–2 days), frequent merges, protected main.
5. **Rollback readiness:** every PR states how to revert; migrations are backward compatible (expand → migrate → contract).
6. **Review contract:** PR description lists spec/AC IDs, what was verified and how, and what the reviewer should focus on.

## Instructions

When given a large change or plan: propose a split into a PR stack with order, size estimate, flag strategy, and the verification for each slice. When asked for policy: produce a short PR policy for agent-authored changes, including a template.

## PR template

```
## What & why (link spec / AC IDs)
## Verification done (commands + results)
## Reviewer focus
## Risk & rollback
## Agent involvement (tool, autonomy level)
```

---

### Further Reading

- [DORA AI Capabilities Model](https://dora.dev/research/publications/)
