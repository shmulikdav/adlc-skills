---
type: llm
weight: 2
---

PASS if the response classifies actions into allow, ask, and deny, defines separate local and CI profiles with CI being narrower and sandboxed with scoped tokens, denies reading secrets files and pushing to main, and recommends backing critical rules with hooks. FAIL if it recommends one permissive setting everywhere.
