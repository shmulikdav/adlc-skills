# ADLC Skills — v1 Review and v2 Decisions

Review date: October 2026. Scope: v1.0.0 (8 plugins, 41 skills, 23 commands, 2 agents) against the leading skill marketplaces and the published benchmarks on whether skills help agents.

## 1. What the benchmarks say about skills

| Study | Finding | Implication for this kit |
|-------|---------|--------------------------|
| **SkillsBench** (86 tasks, 11 domains, 7,308 trajectories) | Curated skills +16.2 pp average; self-generated skills −1.3 pp; focused sets of 2–3 skills beat larger bundles; gains largest where procedures are absent from pretraining (healthcare +51.9 pp) and smallest in software engineering (+4.5 pp) | Value concentrates in **domain/organizational procedure**, not in generic coding advice. Install by role, not everything |
| **SWE-Skills-Bench** (49 public SWE skills, ~565 tasks) | 39 of 49 skills gave zero pass-rate gain; average +1.2%; some cases with >400% token overhead | Generic coding-workflow skills are mostly redundant on strong models |
| **Agent Skills Can Be Harmful** (307 confirmed skill-induced failures) | Largest failure class: the skill induces unnecessary work; efficiency regressions are not explained by prompt length alone | Every instruction must change an outcome; cut "activity" steps |
| **Counterfactual Trace Auditing** (SWE-Skills-Bench, Claude Sonnet 4.5) | Pass rate moved +0.3 pp while traces showed hundreds of behavioral divergences | Measure behavior, not just pass rate; read transcripts |
| **Superpowers writing-skills testing** | Descriptions that summarize the workflow cause agents to follow the summary and skip the body | Descriptions must state trigger conditions only |

## 2. Marketplace landscape (what already exists)

| Layer | Best available | Overlap with v1 |
|-------|---------------|-----------------|
| Execution discipline (plan, TDD, debugging, worktrees, review between tasks) | **Superpowers** (in the official marketplace; most-installed skills framework) | High: v1 `explore-plan-implement`, `agentic-tdd`, `parallel-agents` |
| Feature workflow | Official **feature-dev** (explorer / architect / reviewer agents) | High |
| PR review | Official **pr-review-toolkit**, **code-review**, CodeRabbit | Medium: v1 `agent-code-review` |
| Legacy modernization execution | Official **code-modernization** (assess, map, extract rules, transform, verify; 8 agents) | Medium: v1 `legacy-modernization` |
| CLAUDE.md maintenance | Official **claude-md-management**, **claude-code-setup** | Low–medium |
| Hooks from conversation patterns | Official **hookify** | Low |
| Code security | Official **security-guidance**, **claude-security**; **Trail of Bits skills** (CodeQL, Semgrep, property-based testing, supply-chain auditor) | Low: v1 governs the *agent setup*, not code vulnerabilities |
| Spec / planning rails | **Spec Kit**, **AWS AI-DLC**, **BMAD**, **GSD**, gstack | Medium: v1 `adlc-intent` |
| Engineering specialists | **wshobson/agents** (80+ plugins) | Low |
| Operating model: readiness, autonomy policy, metrics, AI stance, roles, champions, threat model of the agent setup, compliance mapping, release gates by change class, AgentOps, cost, agent incident reviews, eval design | **No dominant kit found** | **This is v1's unique territory** |

## 3. v1 findings

1. **Descriptions summarized workflows** (all 41). Known to cause body-skipping and weaker triggering. → Rewritten as trigger conditions; validator now enforces it.
2. **Generic coding skills duplicated the best rails** and matched the profile benchmarks show adds ~0 or induces extra work. → Removed `explore-plan-implement`, `agentic-tdd`, `parallel-agents`, `/plan-feature`, `/build-feature`. Replaced with `execution-rail-selection` and `/choose-rail`, which compose the best rails instead of competing with them.
3. **No behavioral evidence.** Structural validation only. → Added 48 `claude plugin eval` cases (every skill covered, one negative per plugin) and a CI workflow that reports WITH / W/OUT / Δ.
4. **Install-everything default** conflicts with the "2–3 focused skills" finding. → README now leads with role-based install profiles.
5. **Discipline skills lacked anti-rationalization guidance.** → Red-flags tables added to definition-of-done, agent-code-review, autonomy-levels, release-gates, agent-permissions, legacy-modernization.
6. **Missing:** guidance for managing a skill library itself, now that teams install dozens. → Added `skill-library-management` + `/audit-skills`, grounded in the benchmarks.
7. **CI bug avoided:** secrets cannot gate a job-level `if` in GitHub Actions; the eval workflow gates in a step.
8. Kept: the operating-model plugins (foundations, intent, govern, operate, agent-engineering) and the verification skills that are spec- and agent-specific (`tests-from-specs`, `hallucination-checks`, `agent-code-review` repositioned as alignment review that composes with `pr-review-toolkit`).

## 4. What is still unproven

The first plugin is measured: adlc-verify results are in [EVAL-RESULTS.md](EVAL-RESULTS.md). The other seven are not yet; treat their skills as hypotheses until they are. Rule for all of them: cut or fix any skill with Δ ≤ 0, and publish the table. *(Updated 1 October 2026.)*
