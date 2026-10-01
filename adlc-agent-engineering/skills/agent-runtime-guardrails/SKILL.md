---
name: agent-runtime-guardrails
description: "Use when shipping an agent to users or connecting it to real systems, after a red-team or prompt-injection finding, or when mapping an agent's controls to the OWASP Agentic Top 10."
---

# Agent Runtime Guardrails

**Grounded in:** OWASP Top 10 for Agentic Applications (2026); Feng, McDonald, Zhang: Levels of Autonomy for AI Agents (Knight First Amendment Institute); NIST AI 600-1: Generative AI Profile.





## Purpose

Evals measure quality before release; guardrails constrain behavior at runtime. An agent that reads untrusted content and holds real permissions needs both.

## Layers

| Layer | Controls |
|-------|----------|
| Input | Schema validation, size limits, mark untrusted content with provenance so the agent treats it as data, not instructions |
| Planning | Explicit, versioned goals; refuse goal changes originating from tool results or retrieved content |
| Tools | Allow-list per task; argument validation; scoped credentials; dry-run for writes |
| Actions | Human approval for irreversible or high-impact actions (payments, deletions, external messages, permission changes) |
| Output | Policy checks, PII/secret redaction, format validation, grounding checks for factual claims |
| Limits | Max steps, time, tokens, cost per run; loop detection |
| Control | Kill switch per agent/tenant; audit log; anomaly alerts |

## Instructions

1. List the agent's tools and data sources; mark untrusted inputs and high-impact actions.
2. For each OWASP Agentic risk relevant to the design, select controls from the layers above.
3. Specify each guardrail: trigger, check, action on failure (block, ask human, degrade), logging.
4. Define red-team tests that should be blocked, and add them to the eval suite.

## Output

Guardrail spec table, approval matrix (action × who approves), limits configuration, red-team test list.

---

### Further Reading

- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Feng, McDonald, Zhang: Levels of Autonomy for AI Agents (Knight First Amendment Institute)](https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1)
- [NIST AI 600-1: Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
