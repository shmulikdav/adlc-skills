# Contributing to ADLC Skills

Contributions are welcome: new skills, sharper methods, better sources, fixes.

## What makes a good skill

- It encodes a **method** with a clear output, not a generic prompt.
- Its description says **what it does and when to use it**, including phrases practitioners actually say.
- It is grounded in a **primary source** or real practice, cited under `### Further Reading`.
- It keeps humans at the gates where judgment matters and says so explicitly.
- It is tool-agnostic where possible (Claude Code, Cursor, Codex, Copilot), and names tool-specific details only when necessary.

## Adding a skill

1. Pick the plugin by lifecycle phase.
2. Create `adlc-<plugin>/skills/<skill-name>/SKILL.md` (kebab-case; `name` must equal the folder).
3. Follow the structure: Purpose → Instructions → Output → Notes → Further Reading.
4. If a command should use it, reference it as `**skill-name**` in a command of the **same** plugin.
5. Run:

```bash
python3 scripts/sync_manifests.py
python3 validate_plugins.py
python3 -m unittest discover -s tests
```

6. Update the counts in `README.md` and add a CHANGELOG bullet under `## Unreleased`.

## Pull requests

- One concern per PR.
- Describe the method, the source, and one example prompt with the expected output shape.
- No promotional links, no tracking parameters, no executable content in skills without discussion.

## Releases

Maintainers bump the version in `scripts/plugins_meta.json`, add a `## vX.Y.Z — YYYY-MM-DD` heading in `CHANGELOG.md`, run the sync script, and tag.
