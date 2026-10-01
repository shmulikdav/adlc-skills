# Changelog

## Unreleased

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
