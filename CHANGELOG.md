# Changelog

## Unreleased

## v2.2.0 — 2026-10-01

Grounded every skill in recognized market practice. See docs/STANDARDS-MAP.md.

- Every skill now opens with a **Grounded in** line naming the standards it applies (DORA, DX, Google Engineering Practices, Google SRE, NIST AI RMF / AI 600-1 / SSDF 800-218A / SP 800-207, ISO/IEC 42001, OWASP Agentic Top 10, OpenSSF, FinOps Foundation, Thoughtworks Technology Radar, OpenTelemetry, MCP security guidance, Spec Kit, AWS AI-DLC, and others) and cites at least two primary sources. 12 skills previously cited none.
- `autonomy-levels` now uses the published five-level framework (Operator, Collaborator, Consultant, Approver, Observer; Feng, McDonald & Zhang) instead of a home-grown ladder.
- Replaced or labeled kit-specific numbers: PR-size and review-tier defaults now operationalize Google's small-CL and review guidance and are marked as calibratable; the maturity scale is labeled as this kit's synthesis around DORA capabilities.
- Added standards-backed practice to skills: OpenSSF security baseline for agent context files, Google SRE postmortem format, FinOps for AI allocation and showback, error budgets in release gates, mutation testing as a feedback control, Scrum Definition of Done, ISO 42001 AI policy.
- Validator fails any skill without a Grounded-in line and two sources; new `docs/STANDARDS-MAP.md` (generated); new link-check CI workflow.

## v2.1.0 — 2026-10-01

Pre-launch audit against the 2026 state of agentic development. See docs/LAUNCH-AUDIT.md.

- New skills: `review-capacity` (agent-PR review bottleneck), `continuous-ai-workflows` (background agents in CI), `learning-loop` (compounding fixes from rejected agent work), `comprehension-debt` (keeping humans able to verify agent output), `architecture-guardrails` (ADRs, invariants, dependency rules), `long-running-agent-work` (multi-hour and multi-agent runs), `citizen-builder-governance` (non-engineers building with AI).
- New commands: `/fix-review-queue`, `/plan-continuous-ai`, `/mine-rejections`, `/plan-long-run`, `/citizen-builder-policy`.
- Updated for 2026 reality: auto-mode-era permissions; built-in `/code-review`, `/ultrareview`, `/security-review` composition; AGENTS.md as table of contents with `docs/` as system of record; 2026 skill-supply-chain attack patterns in extension vetting; EU AI Act timeline after the Digital Omnibus; OpenTelemetry GenAI conventions status; DX AI Measurement Framework and review-flow metrics; three new readiness dimensions.
- 55 eval cases (every skill covered).
- Validator now fails the build on hidden zero-width or bidirectional Unicode characters anywhere in the repo.

## v2.0.0 — 2026-10-01

First public release: 8 plugins, 40 skills, 23 commands, 2 agents, 48 eval cases. Start with docs/TRY-IT.md.

Changes since the private v1 (breaking: removed skills and commands that duplicated execution frameworks; see docs/REVIEW.md):

- Repositioned as the ADLC operating-model layer that composes with Superpowers and Anthropic's official plugins.
- Removed `explore-plan-implement`, `agentic-tdd`, `parallel-agents`, `/plan-feature`, `/build-feature` (generic coding workflow; covered better by Superpowers and `feature-dev`; benchmarks show such skills add ~0).
- Added `execution-rail-selection` + `/choose-rail` (adlc-build) and `skill-library-management` + `/audit-skills` (adlc-context).
- Rewrote all 40 skill descriptions as trigger conditions ("Use when…"); validator enforces it.
- Added red-flags tables to discipline skills.
- Added 48 `claude plugin eval` cases covering every skill plus negative cases per plugin, and a CI workflow reporting WITH / W/OUT / Δ.
- New docs: REVIEW.md (benchmarks + marketplace landscape), RECOMMENDED-STACK.md, TRY-IT.md; research notes updated.
- Public launch: SECURITY.md, CODE_OF_CONDUCT.md, issue and PR templates, social preview image, automated releases from CHANGELOG, README quick start and FAQ.

## v1.0.0 — 2026-10-01

- Initial release: 8 plugins, 41 skills, 23 commands, 2 agents.
- Plugins: adlc-foundations, adlc-intent, adlc-context, adlc-build, adlc-verify, adlc-govern, adlc-operate, adlc-agent-engineering.
- Opt-in templates: protect-paths guardrail hook, CLAUDE.md skeleton, Agent Execution Spec skeleton.
- Tooling: manifest sync script, validator, consistency tests, CI workflow.
- Research notes with sources in `docs/ADLC-RESEARCH.md`.
