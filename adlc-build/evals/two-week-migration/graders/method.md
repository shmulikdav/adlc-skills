---
type: llm
weight: 2
---

PASS if the response decomposes the work into packages with clear ownership, externalizes plan and progress state in the repository, defines human checkpoints and abort criteria, sets cost and time budgets, starts with a pilot package, and shapes the output as small reviewable PRs. FAIL if it suggests launching many agents on the whole migration at once without checkpoints or budgets.
