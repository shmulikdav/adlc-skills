# Contributing to ADLC Skills

Contributions are welcome: new skills, sharper methods, better sources, fixes.

## What makes a good skill

Read docs/REVIEW.md first: benchmarks show generic skills often add nothing and can make agents do unnecessary work. Contributions must earn their place with a positive Δ in `claude plugin eval`.

- It encodes an **org- or domain-specific method** with a clear output, not something a strong model already does.
- Its description states **only when to use it** ("Use when…"), with the phrases and symptoms practitioners actually say. No workflow summary.
- It is **grounded in recognized market practice**: add its standards to `scripts/grounding.py` (at least two primary sources). If you introduce a number or model of your own, label it in the skill as a calibratable default.
- It keeps humans at the gates where judgment matters and says so explicitly.
- It is tool-agnostic where possible (Claude Code, Cursor, Codex, Copilot), and names tool-specific details only when necessary.

## Adding a skill

1. Pick the plugin by lifecycle phase.
2. Create `adlc-<plugin>/skills/<skill-name>/SKILL.md` (kebab-case; `name` must equal the folder).
3. Follow the structure: Purpose → Instructions → Output → Notes → Further Reading.
4. If a command should use it, reference it as `**skill-name**` in a command of the **same** plugin.
5. Add at least one eval case in `scripts/eval_cases.py` (natural phrasing, never naming the skill, with a rubric that rewards the skill's method).
6. Run:

```bash
python3 scripts/eval_cases.py
python3 scripts/sync_manifests.py
python3 validate_plugins.py
python3 -m unittest discover -s tests
```

7. Run `claude plugin eval ./adlc-<plugin>` and include the WITH / W/OUT / Δ table in the PR.
8. Update the counts in `README.md` and add a CHANGELOG bullet under `## Unreleased`.

## Pull requests

- One concern per PR.
- Describe the method, the source, and one example prompt with the expected output shape.
- No promotional links, no tracking parameters, no executable content in skills without discussion.

## Releases

Maintainers bump the version in `scripts/plugins_meta.json`, add a `## vX.Y.Z — YYYY-MM-DD` heading in `CHANGELOG.md`, run the sync script, and tag.
