---
name: ai-compliance-mapping
description: "Use when preparing for an AI audit or certification (ISO/IEC 42001, SOC 2), answering customer security questionnaires about AI use in development, or aligning agentic development practices with NIST AI RMF or the EU AI Act."
---

# AI Compliance Mapping

## Purpose

Auditors and enterprise customers increasingly ask two questions: how do you govern AI in your products, and how do you govern AI in your development process. This skill maps existing ADLC practices to framework expectations and shows the gaps.

## Frameworks (use those relevant to the organization)

- **ISO/IEC 42001** — AI management system: policy, roles, risk assessment, impact assessment, lifecycle controls, monitoring, improvement.
- **NIST AI RMF** — Govern, Map, Measure, Manage.
- **EU AI Act** — obligations depend on role (provider/deployer) and risk classification of the AI system; development tooling itself is usually not high-risk, but AI features shipped to users may be. Timeline after the Digital Omnibus (Regulation (EU) 2026/1744, in force 27 July 2026): prohibited practices and AI literacy since February 2025; GPAI provider obligations since August 2025; Article 50 transparency obligations from 2 August 2026 (with a grace period to 2 December 2026 for some generative systems already on the market); Annex III high-risk obligations moved to 2 December 2027; Annex I (product-embedded) to 2 August 2028. Verify current dates before advising; this area keeps moving.
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
