# Changelog

## Unreleased

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
