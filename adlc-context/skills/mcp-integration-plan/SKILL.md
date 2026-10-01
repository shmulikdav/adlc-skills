---
name: mcp-integration-plan
description: "Use when deciding which internal systems coding agents should access through MCP servers (tickets, docs, designs, logs, databases, CI), when making internal data AI-accessible, or when agents lack context that lives outside the repository."
---

# MCP Integration Plan

**Grounded in:** Model Context Protocol: Security best practices; OWASP Top 10 for Agentic Applications (2026); DORA research (State of AI-assisted Software Development, AI Capabilities Model).





## Purpose

DORA's 2025 research lists AI-accessible internal data as an amplifying capability. MCP (Model Context Protocol) is the standard way to give agents that access, and every connection is also an attack surface. Plan both together.

## Instructions

1. **Inventory context needs.** For the team's common tasks, list what knowledge the agent lacks and where it lives (tickets, specs, ADRs, designs, logs, metrics, DB schema, runbooks).
2. **Map to sources and servers.** For each source: official MCP server available? self-hosted? read-only possible?
3. **Classify each integration:**

```
| Source | Value (H/M/L) | Data sensitivity | Access: read / write | Scope (which projects/spaces) | Auth model | Owner |
```

4. **Apply least privilege:** start read-only; scope to specific projects; use per-user auth over shared service tokens; never expose production write access to an agent without a human gate.
5. **Assess injection exposure:** any source containing third-party or user-generated text (tickets from customers, emails, web pages) can carry prompt-injection payloads. Mark these and require confirmation before agents act on instructions found in them.
6. **Sequence rollout:** highest value × lowest risk first; define success signal per integration.

## Output

Integration table, rollout order, approval/vetting process for new servers, and a short "do not connect" list with reasons.

## Notes

- Vet third-party MCP servers like any dependency (source, maintainer, permissions requested, update policy).
- Prefer project-level configuration checked into the repo so the whole team gets the same, reviewed setup.

---

### Further Reading

- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [DORA AI Capabilities Model](https://dora.dev/research/publications/)
- [Model Context Protocol: Security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
