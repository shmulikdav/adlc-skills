# Changelog

## Unreleased

- **Atomic criteria for every remaining eval case** (intent, context, build, operate, agent-engineering): 27 compound rubrics split one-for-one into 131 single-requirement graders, with no requirements added or removed. Every positive case in the kit is now scored as the fraction of criteria met.

- **extension-vetting re-measured:** loading rose from 0/5 to 2/5 and the harm disappeared (Δ −0.23 to −0.03); when it loads it helps, but it loads too rarely to show a net gain. `/vet-extension` now says to answer general questions directly, and the skill must say that stars are not evidence of safety. Recommended use: run `/vet-extension <link>` explicitly.

- **Govern re-measured:** `ai-compliance-mapping` rose to +0.40 after its fix; `guardrail-hooks` shows no gain with a fair prompt; `extension-vetting` is still harmful (−0.23) because it never loaded.
- **extension-vetting** trigger covers general questions asked before a specific extension is shared.
- New eval case **vet-plugin-files**: a plugin's files inline with four planted problems, so the vetting skill is measured on real vetting (64 cases).

- **adlc-govern measured:** four skills with clear gains (+0.30 to +0.57); results in `docs/EVAL-RESULTS.md` and the README.
- **extension-vetting** and **/vet-extension** give the full checklist and install / restrict / reject rule before asking for a link. Found by the govern eval: with the kit installed, the model deferred instead of answering (Δ −0.20).
- **guardrail-hooks** triggers on "must never happen, no matter what"; **agent-permissions** now says why must-never rules need hooks. Found by the govern eval: the two skills collided and the answer missed the key point.
- **ai-compliance-mapping** has an Output section that ends with the counsel-or-auditor confirmation.
- **protect-secrets eval** prompt says "don't change any files", so neither arm burns its turns trying to write a settings file.

- **adlc-govern evals:** compound rubrics split into atomic criteria (same requirements, one per grader), ready to measure.
- **ai-stance-policy:** the policy must fit on one page (about 400 words); items needing legal review are marked [LEGAL]; the decision table and announcement are offered instead of written unasked; an Output section was added. Found by the foundations eval: no run produced a policy short enough.
- **comprehension-debt:** the ownership map (a named owner for each critical module) is now the baseline practice, not one option among several. Found by the foundations eval: no run proposed named owners.

- **adlc-foundations evals:** compound all-or-nothing rubrics split into atomic criteria, so a partly right baseline scores partial credit instead of 0. A first run with the old rubrics showed large gains (Δ +0.20 to +1.00 on seven of eight skills) but overstated their size; re-measured with atomic criteria, all eight skills show gains of +0.24 to +0.77; published in `docs/EVAL-RESULTS.md` and the README.
- **adlc-readiness-assessment** now gives a provisional assessment from what the user already provided, marking gaps as unknown, instead of asking questions first. The first eval run caught this: with the skill loaded, Haiku asked for more inputs and never assessed, even when told to.

Hardening after an external review.

- **Supply chain:** GitHub Actions pinned to full commit SHAs (Dependabot keeps them current), Claude Code version pinned in the eval workflow, CODEOWNERS added, release split into a read-only verify job and a write-only publish job, and a warning when a release changes skills without an `Evals:` line in its notes.
- **Evals:** one near-miss negative case per plugin, checking that requests right next to a plugin's territory don't trigger it (63 cases total).
- **Codex:** workflow skill descriptions are now trigger-only, like every authored skill; a test enforces it.
- **Docs:** `docs/COMPATIBILITY.md` (what is verified on each platform and how), `docs/TROUBLESHOOTING.md`, `SECURITY.md` now covers the Cursor installer, stale "not yet measured" statements removed, social preview no longer shows a count that goes stale.
- Plugins show proper display names in Claude apps ("ADLC Verify" instead of "Adlc verify").
- README: Cowork install steps match the current Settings → Plugins screen.

## v2.4.0 — 2026-10-01

Easier to start, and the commands now flow into each other.

- **Use cases** (`docs/USE-CASES.md`): ten situations engineering organizations hit with coding agents, each with a step-by-step path through the commands, what each step produces, and a prompt to try.
- **Start here** table at the top of the README: pick your situation, get the first command.
- **Chained commands:** every command ends by suggesting at most two next steps, chosen by what it found, including commands in other plugins. Codex workflow skills get the same chaining as `$command`.
- Examples (prompts and command invocations) for all eight plugins.
- New test: every command mentioned in the README and docs must exist.

## v2.3.0 — 2026-10-01

Now installable in OpenAI Codex and Cursor, alongside Claude Code and Cowork, plus the first published eval results.

- **Codex:** native Codex manifests and marketplace (`.codex-plugin/`, `.agents/plugins/marketplace.json`). Each of the 28 commands also ships as a Codex workflow skill (`$adlc-assess`), because Codex plugins have no slash commands. Verified with Codex CLI 0.159.3: all 8 plugins install and all 47 skills and 28 workflows load.
- **Cursor:** native Cursor manifests and marketplace (`.cursor-plugin/`), `name` added to command and agent frontmatter, and `scripts/install-cursor.sh` for local installs. Validated against Cursor's official schema and validator.
- Codex and Cursor packaging is generated from the Claude Code plugins by `scripts/sync_cross_platform.py`; CI fails if any generated file is out of date, and new tests check all three platforms stay consistent.
- Renamed `/codify-convention` to `/codify`: the old name was one letter from its skill (`codify-conventions`), and the model skipped loading the skill.
- Every command now loads its skills first (Step 0); the smoke test (`scripts/smoke_commands.sh`) verifies this per command.
- First published eval results for adlc-verify (`docs/EVAL-RESULTS.md`, README).
- Evals v2/v3: atomic-criteria graders, inline fixtures with planted defects, Sonnet judge recommended.
- Eval-driven fixes: `hallucination-checks` never asserts unverified facts and adds necessity and approval steps; broader triggers for `review-capacity`, `agent-code-review`, `tests-from-specs`.

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
