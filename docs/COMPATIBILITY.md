# Compatibility

What has been verified on each platform, how, and what has not. Updated whenever a platform is re-tested.

| Platform | Version tested | Date | Install | Skills | Commands | Review agents | Behavioral evals |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Code (CLI) | 2.1.286 | 2026-10-01 | ✅ From GitHub marketplace | ✅ 47 load | ✅ 28/28 run as documented and load their skills (`scripts/smoke_commands.sh`) | Used by `/review-agent-pr` and `/vet-extension`; not separately tested | ✅ adlc-verify measured ([EVAL-RESULTS.md](EVAL-RESULTS.md)); 7 plugins pending |
| Claude Cowork | Claude desktop app | 2026-10-01 | ✅ Settings → Plugins → Add marketplace | ✅ Listed in the slash menu | ✅ Listed in the slash menu | Not tested | Not available (evals run in Claude Code) |
| OpenAI Codex (CLI) | 0.159.3 | 2026-10-01 | ✅ 8/8 plugins install and enable | ✅ 47/47 visible to the model (`codex debug prompt-input`) | ✅ 28/28 as `$command` workflow skills, visible to the model | Not available in Codex plugins | Not yet run |
| Cursor | Desktop app | 2026-10-01 | ✅ Local plugin via `scripts/install-cursor.sh`; official schema and validator pass | ✅ Listed in the slash menu | ✅ Listed in the slash menu, with argument hints | Not tested | Not yet run |
| Other Agent Skills tools (Gemini CLI, OpenCode) | — | — | Not tested | Should load from the tool's skills directory | Not available | Not available | Not available |

**What "verified" means here.** Install and listing checks confirm the kit loads where each tool looks for it. Behavioral evals confirm a skill changes the answer. Only Claude Code has both so far. Codex and Cursor behavioral runs are on the roadmap; reports from your own runs are welcome in [Discussions](https://github.com/shmulikdav/adlc-skills/discussions).

**Known platform differences**

- **Codex** plugins have no slash commands, so each command ships as a workflow skill: `$adlc-assess` instead of `/adlc-assess`. Codex 0.159 replaces its default skill discovery when a manifest lists skill paths, so the Codex manifests list both `./skills/` and `./workflows/`.
- **Cursor** requires `name` in command and agent frontmatter, and skips symlinked plugin folders, which is why the installer copies.
- **Cowork** shows each plugin's `displayName` ("ADLC Verify") from v2.4.0 on.
