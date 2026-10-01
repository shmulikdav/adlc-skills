---
type: llm
---

PASS only if the response defines risk tiers that route PRs automatically by files touched or change type, with a lighter path for low-risk changes and a deeper path (for example a specialist reviewer) for high-risk areas such as auth, payments, or migrations. FAIL otherwise.
