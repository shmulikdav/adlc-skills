---
type: llm
weight: 2
---

PASS if the response checks alignment against the spec (scope creep and omissions), whether tests were modified or weakened in the same PR, and AI-specific failure patterns (invented APIs or config, swallowed errors, duplicated helpers), plus security on the new paths. FAIL if it only lists generic code review tips.
