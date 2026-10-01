## What & why

<!-- Which skill/command/agent, and the problem it solves -->

## Checklist

- [ ] Description is trigger conditions only ("Use when…"), no workflow summary
- [ ] Encodes org- or domain-specific procedure, not something a strong model already does
- [ ] Eval case added in `scripts/eval_cases.py` (natural phrasing, never names the skill)
- [ ] `python3 scripts/eval_cases.py && python3 scripts/sync_manifests.py`
- [ ] `python3 validate_plugins.py && python3 -m unittest discover -s tests`
- [ ] README counts updated (if skills/commands changed)
- [ ] CHANGELOG bullet under `## Unreleased`

## Eval results

<!-- Paste the WITH / W/OUT / Δ table from `claude plugin eval ./adlc-<plugin>` for affected cases -->
