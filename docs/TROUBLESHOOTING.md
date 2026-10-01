# Troubleshooting

Problems people hit, and the fix for each. If yours isn't here, open a [Discussion](https://github.com/shmulikdav/adlc-skills/discussions).

## Installing and updating

**A command says "unknown command".**
The plugin that owns it isn't installed. Each command belongs to one plugin (see the README's plugin list); install that plugin and start a new session. Every command also works with its plugin prefix, for example `/adlc-verify:derive-tests`.

**Two kits have a command with the same name.**
If you also use pm-skills, both kits have `/derive-tests`. Use the prefixed form, `/adlc-verify:derive-tests`, to get this kit's version.

**I updated, but nothing changed.**
- Claude Code: `claude plugin marketplace update adlc-skills`, then `claude plugin update <plugin>@adlc-skills`, then start a new session.
- Cowork: remove and re-add the marketplace under Settings → Plugins.
- Codex: `codex plugin marketplace upgrade`, then start a new session.
- Cursor: `git pull` in your clone, run `bash scripts/install-cursor.sh <plugins>` again, then **Developer: Reload Window**.

**Cursor doesn't show the plugin.**
Run **Developer: Reload Window** after installing. On Cursor Teams or Enterprise, an admin may have turned off **Allow Local Plugin Imports** (Dashboard → Settings → Security & Identity). Plugins must be copied into `~/.cursor/plugins/local`, not symlinked; the installer copies for you.

**Codex lists the skills but not the `$command` workflows.**
Use Codex CLI 0.159 or later (the version tested) and start a new session after installing. `codex plugin list` should show the plugin as `installed, enabled`.

## Using the kit

**A skill didn't load on its own.**
Skills load when Claude judges your request matches their description, and that is probabilistic. Two options: run the matching command (commands load their skills explicitly), or name it ("use the review-capacity skill"). Two skills are known not to auto-trigger reliably: `agent-code-review` when a diff is pasted inline, and `tests-from-specs` when test cases are pasted inline. Use `/review-agent-pr` and `/derive-tests` for those. See [EVAL-RESULTS.md](EVAL-RESULTS.md).

**A command asked me questions instead of answering.**
That's by design when key inputs are missing: assessments score unknowns as unknown rather than guess. Give it the context in one message, or tell it to state its assumptions and proceed.

**The answer said it couldn't load a skill.**
The plugin that owns that skill isn't installed or enabled. Commands only load skills from their own plugin; cross-plugin suggestions name the plugin to install.

## Evals and tests

**`claude plugin eval` fails with "Not logged in".**
Run `claude`, then `/login`, then `/exit`, and run the eval again.

**Eval costs.**
A full plugin suite is roughly 40–60 agent runs plus judge calls. Cap spend with `--max-cost-usd`. For a quick read, use `--case <name> --runs 1`. Judge with Sonnet (`--judge-model sonnet`): small judges mark correct long answers wrong.

**Both arms score 1.00 (or both 0.00).**
The case isn't measuring the skill. Either the rubric is too easy (split it into atomic criteria) or the prompt refers to material the empty eval sandbox doesn't have (put it inline). [EVAL-RESULTS.md](EVAL-RESULTS.md) records how we fixed both.

**The smoke test shows WARN (no skill loaded).**
Usually the generic test scenario gave the command nothing specific to work on. Re-run that command alone with a realistic argument and check the skill count.

**CI says generated files are out of date.**
Run `python3 scripts/sync_manifests.py` and commit the result. Never edit `plugin.json`, the plugin READMEs, `.codex-plugin/`, `.cursor-plugin/` or `workflows/` by hand.
