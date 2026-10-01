# CLAUDE.md

Guidance for agents working in this repository. Single source of truth for structure and maintenance.

## Project

**ADLC Skills** (`braightwave/adlc-skills`) — a Claude Code / Cowork plugin marketplace of 8 plugins that encode the Agentic Development Lifecycle as skills, commands, and agents. Owner: Shmulik Davar, BrAIght Wave — shmulik@braightwave.com.

## Structure

```
.claude-plugin/marketplace.json   <- generated; lists all plugins
scripts/plugins_meta.json         <- SOURCE for plugin names, descriptions, keywords, version, owner
scripts/sync_manifests.py         <- regenerates plugin.json files, plugin READMEs, marketplace.json
validate_plugins.py               <- structural validator
tests/                            <- consistency tests (counts, versions, sync)
templates/                        <- opt-in hooks and file templates (never auto-activated)
docs/ADLC-RESEARCH.md             <- research notes and sources behind the skills
adlc-<name>/
  .claude-plugin/plugin.json      <- generated; only this file belongs in .claude-plugin/
  skills/<skill>/SKILL.md         <- one folder per skill; name == folder
  commands/<command>.md           <- workflows chaining skills in the same plugin
  agents/<agent>.md               <- optional subagents
  README.md                       <- generated
```

## Design rules

- **Skills are methods (nouns); commands are workflows (verbs).**
- **No cross-plugin hard references.** A command may only reference skills in its own plugin by name (`**skill-name**`). Mention other plugins' capabilities in natural language only. The validator enforces this.
- Skill frontmatter: `name` (matches folder, kebab-case) and `description` (what + when, with trigger phrases, ≤1024 chars). Keep bodies well under 500 lines.
- Command frontmatter: `description` and `argument-hint`; use `$ARGUMENTS` once.
- Agents: `name` (matches file), `description`, `tools`. Reviewer agents are read-only.
- Every skill ends with `### Further Reading` linking primary sources only (no promotional links).
- Templates and hooks are opt-in. Never ship active hooks inside a plugin without an explicit decision recorded in CHANGELOG.
- Voice: practitioner, direct, no hype words. Numbers over adjectives.

## After any change

1. Edit `scripts/plugins_meta.json` if a plugin's description/keywords changed.
2. `python3 scripts/sync_manifests.py`
3. Update counts in `README.md` (headline and per-plugin headers) if skills/commands were added or removed.
4. `python3 validate_plugins.py && python3 -m unittest discover -s tests`
5. Add a bullet under `## Unreleased` in `CHANGELOG.md`.

## Releases

Version lives in `scripts/plugins_meta.json` and must equal the newest `## vX.Y.Z` heading in `CHANGELOG.md` (tested). Semver: new skills/commands = minor; fixes/docs = patch; renames/removals = major.
