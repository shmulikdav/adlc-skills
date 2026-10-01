# CLAUDE.md

Guidance for agents working in this repository. Single source of truth for structure and maintenance.

## Project

**ADLC Skills** (`shmulikdav/adlc-skills`) — a Claude Code / Cowork plugin marketplace of 8 plugins encoding the Agentic Development Lifecycle's operating model: readiness, intent, context, execution stack, verification, governance, operations, and agent engineering. Owner: Shmulik Davar, BrAIght Wave.

Positioning: this kit is the **operating-model layer**. It composes with execution rails (Superpowers, official `feature-dev`, `pr-review-toolkit`, `code-modernization`, security plugins) instead of duplicating them. Do not add generic coding-workflow skills; see docs/REVIEW.md for the evidence.

## Structure

```
.claude-plugin/marketplace.json   <- generated
scripts/plugins_meta.json         <- SOURCE: plugin names, descriptions, keywords, version, owner
scripts/sync_manifests.py         <- regenerates plugin.json files, plugin READMEs, marketplace.json
scripts/eval_cases.py             <- SOURCE: eval cases; regenerates every plugin's evals/
validate_plugins.py               <- structural + style validator
tests/                            <- consistency tests
templates/                        <- opt-in hooks and file templates (never auto-activated)
docs/                             <- research, review, recommended stack
adlc-<name>/
  .claude-plugin/plugin.json      <- generated
  skills/<skill>/SKILL.md
  commands/<command>.md
  agents/<agent>.md               <- optional
  evals/<case>/prompt.md + graders/*.md   <- generated; claude plugin eval format
  README.md                       <- generated
```

## Skill authoring rules

- **Description = trigger conditions only.** Start with "Use when / before / after…", third person, list situations and symptoms, ≤500 chars. Never summarize the workflow in the description (agents act on the summary and skip the body). Enforced by the validator.
- **Org-specific over generic.** Encode procedures, templates, thresholds and decision rules a model can't know. If a skill restates what a strong model already does, it doesn't belong (SWE-Skills-Bench: 39/49 generic SWE skills had zero gain).
- **No unnecessary work.** Every instruction must change an outcome.
- **Red flags table** for discipline rules agents tend to rationalize away.
- **Every skill has ≥1 eval case** with natural phrasing (never naming the skill) and a rubric rewarding the skill's method; every plugin has ≥1 negative case.
- Commands reference only skills in their own plugin (`**skill-name**`). Validator enforces.
- **Grounded in market practice.** Every skill has a `**Grounded in:**` line under its title and at least two primary sources in `### Further Reading`, both managed in `scripts/grounding.py` (validator-enforced). Where no standard exists, say in the skill that a number or model is the kit's own calibratable default.
- `### Further Reading` links primary sources only.

## After any change

1. Edit `scripts/plugins_meta.json` and/or `scripts/eval_cases.py` as needed.
2. `python3 scripts/sync_manifests.py && python3 scripts/eval_cases.py && python3 scripts/grounding.py`
3. Update counts in `README.md` if skills/commands changed.
4. `python3 validate_plugins.py && python3 -m unittest discover -s tests`
5. Behavior check (costs model usage): `claude plugin eval ./adlc-<plugin>`. A skill change must not make Δ negative.
6. CHANGELOG bullet under `## Unreleased`.

## Releases

Version lives in `scripts/plugins_meta.json` and must equal the newest `## vX.Y.Z` heading in `CHANGELOG.md` (tested). New skills = minor; fixes/docs = patch; removals/renames = major.
