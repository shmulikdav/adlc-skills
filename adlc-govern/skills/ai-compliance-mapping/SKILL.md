---
name: ai-compliance-mapping
description: "Map an organization's agentic development practices and AI features to governance frameworks (ISO/IEC 42001 AI management system, NIST AI RMF, EU AI Act, SOC 2) and produce a control gap list with evidence to collect. Use when preparing for an AI audit or certification, answering customer security questionnaires about AI use in development, or aligning ADLC practices with regulatory expectations."
---

# AI Compliance Mapping

## Purpose

Auditors and enterprise customers increasingly ask two questions: how do you govern AI in your products, and how do you govern AI in your development process. This skill maps existing ADLC practices to framework expectations and shows the gaps.

## Frameworks (use those relevant to the organization)

- **ISO/IEC 42001** — AI management system: policy, roles, risk assessment, impact assessment, lifecycle controls, monitoring, improvement.
- **NIST AI RMF** — Govern, Map, Measure, Manage.
- **EU AI Act** — obligations depend on role (provider/deployer) and risk classification of the AI system; development tooling itself is usually not high-risk, but AI features shipped to users may be.
- **SOC 2** — change management, access control, and vendor management controls touched by coding agents and AI vendors.

## Instructions

1. Clarify scope: AI used **in** development (coding agents), AI shipped **in** products, or both. Jurisdictions and customer requirements.
2. Inventory practices already in place (policy, permissions, reviews, logs, vendor contracts, evals).
3. Build the mapping:

```
| Framework clause / function | Expectation (plain language) | Current practice | Evidence artifact | Gap | Action |
```

4. Prioritize gaps by audit or customer impact.
5. List the evidence pack: policy doc, risk register, threat model, permission configs, review records, agent audit logs, vendor DPAs, eval results.

## Notes

- This is a structured starting point, not legal advice. Flag items for counsel or a certified auditor.
- Reuse artifacts: one threat model and one audit log can serve several frameworks.

---

### Further Reading

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC 42001](https://www.iso.org/standard/81230.html)
- [EU AI Act resource site](https://artificialintelligenceact.eu/)
