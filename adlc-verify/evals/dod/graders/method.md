---
type: llm
weight: 2
---

PASS if the response defines a checklist requiring fresh evidence (test output, type check, lint) attached before claiming completion, separates automatable checks from human gates, and suggests enforcing it via hooks or CI. FAIL if it only suggests asking the agent to double-check its work.
