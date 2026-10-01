# Pre-Launch Audit — October 2026

A critical review of ADLC Skills against where agentic development actually is in late 2026, done before public announcement. Goal: find what's missing, stale, or overclaimed.

## Method

Checked the kit against: Anthropic's *2026 Agentic Coding Trends Report* (eight trends), 2026 delivery data (LinearB benchmarks on 8.1M PRs, Faros, DX Q2 2026), GitHub's Continuous AI / Agentic Workflows, OpenAI's *Harness engineering* write-up, Anthropic's 2026 skill-formation RCT, the 2026 agent-skill supply-chain incidents and studies (ClawHavoc, Snyk ToxicSkills), the EU AI Act Digital Omnibus, the OpenTelemetry GenAI conventions, current Claude Code capabilities, and competing "ADLC" repositories.

## Coverage against Anthropic's eight 2026 trends

| Trend | v2.0 coverage | v2.1 |
|-------|---------------|------|
| 1. SDLC changes dramatically | Strong (foundations, mapping, roles) | Unchanged |
| 2. Single agents → coordinated teams | **Weak** (removed generic parallel-agents skill) | `long-running-agent-work` |
| 3. Long-running agents build complete systems | **Missing** | `long-running-agent-work` |
| 4. Human oversight scales (agentic QC, review what matters) | **Partial** (review skills, no capacity design) | `review-capacity`, built-in review composition |
| 5. New surfaces and users | **Missing** | `citizen-builder-governance` |
| 6. Economics shift | Partial (metrics, cost) | Metrics updated: output volume, DX framework |
| 7. Non-technical use cases expand | **Missing** | `citizen-builder-governance` |
| 8. Dual-use security | Strong | Extension vetting updated with 2026 attack patterns |

## Gaps found and closed

1. **The review bottleneck is the defining 2026 problem, and v2.0 had no skill for it.** Agentic PRs wait ~5× longer for pickup and are accepted far less often than manual PRs. → `review-capacity` + `/fix-review-queue`; review-flow metrics in `adlc-metrics`; readiness dimension 13.
2. **Continuous AI / background agents** (GitHub Agentic Workflows, Claude Code routines) were absent. → `continuous-ai-workflows` + `/plan-continuous-ai`.
3. **No learning loop.** Rejected agent PRs and repeated review comments are the richest improvement signal; competing kits ("rejection mining") and AWS's background-agent sample capture it. → `learning-loop` + `/mine-rejections`.
4. **Comprehension debt** was one line in `role-transitions`. Anthropic's RCT shows a 17% comprehension drop with delegation-style AI use, largest on debugging. → `comprehension-debt`; readiness dimension 15.
5. **Architecture as agent constraint** was missing; every phase model includes it, and harness-engineering practice says enforce invariants in the repo. → `architecture-guardrails`; wired into `/spec-feature`.
6. **Non-engineers building software** with Cowork, Claude Code, Lovable. Directly relevant to consulting clients outside R&D. → `citizen-builder-governance` + `/citizen-builder-policy`.

## Stale content corrected

- **Permissions:** auto mode is the default for new Pro/Max/Team sessions since August 2026; the skill only described allow/ask/deny.
- **Review tooling:** Claude Code now has built-in multi-agent `/code-review`, `/ultrareview`, and `/security-review`; skills now compose with them.
- **Context files:** AGENTS.md is read by recent Claude Code versions; best practice moved to "AGENTS.md as table of contents, `docs/` as system of record".
- **Supply chain:** ClawHavoc (1,184 malicious skills, fake popularity, typosquatting), Snyk ToxicSkills (prompt injection in 36% of scanned skills), hidden-Unicode payloads, rug pulls. Now explicit in `extension-vetting`, and this repo's CI scans itself for hidden characters.
- **EU AI Act:** high-risk deadlines moved by the Digital Omnibus (Annex III to Dec 2027); Article 50 transparency still applied from Aug 2026.
- **Observability:** OTel GenAI conventions are still *Development* status and moved repositories in June 2026; Claude Code and Codex export OTel data.
- **Measurement:** DX AI Measurement Framework added; DX Q2 2026 shows spend up ~28× with flat innovation ratio.

## Competitive check

Other public "ADLC" repos exist: gate CLIs (voodootikigod/adlc), ADR and use-case skills (wuersch/adlc), a GitHub-automation pipeline (juanjtov/adlc-pipeline), and Salesforce's Agentforce agent lifecycle. None targets the organizational operating model for engineering leaders; this kit's positioning holds. Plugin names (`adlc-*` under the `adlc-skills` marketplace) don't collide.

## Grounding pass (v2.2)

Every skill was checked for whether it applies recognized market practice or something invented. 12 skills cited no sources; the autonomy ladder, PR-size thresholds, review tiers, and maturity scale were home-grown. Fixed: all skills now cite standards (see STANDARDS-MAP.md), the autonomy skill uses the published Levels of Autonomy for AI Agents, and the remaining kit-specific heuristics are labeled as calibratable defaults.

## What is still not good enough (honest list)

1. **Measured Δ for some plugins, not all.** Results and the current status by plugin are in [EVAL-RESULTS.md](EVAL-RESULTS.md). Plugins not yet measured remain well-sourced hypotheses.
2. **Kit size.** 47 skills risks the "more is worse" effect the benchmarks warn about. Mitigation: role profiles and per-plugin installs. Watch skill-activation telemetry and cut what isn't used.
3. **No real-world case studies.** Claims of value rest on research, not on teams using this kit. Collect two or three pilot stories.
4. **Model-graded rubrics.** Eval rubrics are judged by a model; calibrate a sample against human judgment before quoting numbers publicly.
5. **Fast-moving facts.** Permissions, review commands, regulatory dates, and OTel status will change within months. Plan a quarterly refresh.
6. **English only.**
7. **Commands use the older `commands/` format** for Cowork and pm-skills parity; migrate if Claude Code deprecates it.
