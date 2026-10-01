---
type: llm
weight: 2
---

PASS if the response proposes low-risk starter workflows such as issue triage, CI failure investigation, documentation updates, or test gap filling, insists that outputs are proposals like comments or draft PRs rather than merges, treats issue and comment text as untrusted input, and sets permissions, budgets, an owner, and a shadow-mode trial. FAIL if it suggests letting background agents merge or deploy.
