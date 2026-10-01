---
name: skill-library-management
description: "Use when a team is building, curating, or pruning an internal library of agent skills or plugins, when deciding whether a skill is worth keeping, when skills are not triggering or are slowing agents down, or before publishing skills to other teams."
---

# Skill Library Management

## Overview

Skills are not free. Benchmarks now show what practitioners suspected:

- Curated, focused skills help: SkillsBench measured +16.2 pp average pass rate, with the largest gains in domains whose procedures are not in model pretraining.
- Generic skills often don't: SWE-Skills-Bench found 39 of 49 public software-engineering skills gave zero gain (+1.2% average), with token overhead in some cases above 400%.
- Skills can hurt: in a study of 307 skill-induced failures, the largest category was the skill pushing the agent into unnecessary work.
- Agent-written skills don't help on their own (−1.3 pp in SkillsBench). Human curation is the value.
- Less is more: focused sets of 2–3 skills outperformed larger bundles.

**Core rule:** a skill earns its place with a measured positive delta against no skill. Otherwise it is noise in every session.

## Keep / fix / cut test

| Signal | Action |
|--------|--------|
| Positive Δ on eval cases, triggers on natural phrasing | Keep |
| Δ ≈ 0, content restates what the model already does | Cut, or narrow it to the org-specific part |
| Doesn't trigger on realistic prompts | Fix the description (trigger conditions, not a workflow summary) |
| Triggers on unrelated prompts | Narrow the description; add a negative eval case |
| Δ negative or large token overhead | Cut or rewrite; look for "do extra work" instructions |
| Duplicates an installed framework's skill | Pick one owner |

## Authoring standards

1. **Description = when to use, not what it does.** Start with "Use when…", list situations and symptoms, third person. Summarizing the workflow in the description lets agents act on the summary and skip the body.
2. **Org-specific beats generic.** Encode what the model cannot know: your conventions, templates, thresholds, approval rules, domain procedures.
3. **Focused.** One job per skill. Move long references into `references/` files loaded on demand.
4. **Red flags for discipline rules.** Where agents tend to rationalize skipping a rule, list the rationalizations and the reality.
5. **No unnecessary work.** Every instruction should change an outcome. Delete steps that only add activity.

## Evaluation loop

1. For each skill write 2–4 eval cases: realistic prompts that should trigger it, one near-miss that should not, and a rubric for the output.
2. Run them with and without the plugin (e.g., `claude plugin eval .` reports WITH, W/OUT, and Δ per case).
3. Iterate on the description first when the skill doesn't fire; on the body when it fires but doesn't help.
4. Re-run on every model upgrade; a skill that helped an older model may be redundant now.
5. Gate publishing on a positive Δ and zero failing negative cases.

## Library hygiene

- Measure real usage, not just installs: Claude Code's OpenTelemetry export emits a skill-activation event (including whether the user or Claude triggered it). Skills nobody activates are candidates for cutting

- Per-team load budget: install by role or phase, not everything.
- Owners and review dates per skill; prune quarterly.
- Vet third-party skills before adoption (provenance, executable content, permissions).

## Output

A library audit table: `Skill | Owner | Triggers? | Δ | Tokens | Duplicates | Decision`, plus the eval cases to add.

---

### Further Reading

- [SkillsBench (arXiv 2602.12670)](https://arxiv.org/abs/2602.12670)
- [SWE-Skills-Bench (arXiv 2603.15401)](https://arxiv.org/abs/2603.15401)
- [Agent Skills Can Be Harmful (arXiv 2608.11888)](https://arxiv.org/abs/2608.11888)
- [Claude Code: Test plugins with evals](https://code.claude.com/docs/en/plugin-evals)
- [Superpowers: writing-skills](https://github.com/obra/superpowers)
