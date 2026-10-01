#!/usr/bin/env python3
"""Generate Codex and Cursor packaging from the Claude Code plugins.

Source of truth stays the same: skills/, commands/, agents/ and scripts/plugins_meta.json.
This script writes, per plugin:
  .codex-plugin/plugin.json   Codex manifest (schema: openai/codex plugin-creator spec)
  .cursor-plugin/plugin.json  Cursor manifest (schema: cursor/plugins schemas/plugin.schema.json)
  workflows/<command>/SKILL.md  each command as a Codex skill, because Codex plugins have no slash commands
and at the repo root:
  .agents/plugins/marketplace.json   Codex marketplace
  .cursor-plugin/marketplace.json    Cursor marketplace
It also makes sure every command and agent has a `name` in its frontmatter (Cursor requires it).
Run via scripts/sync_manifests.py; do not edit the generated files by hand.
"""
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = json.loads((ROOT / "scripts" / "plugins_meta.json").read_text(encoding="utf-8"))
SITE = "https://braightwave.com/adlc"


def dump(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def split_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def ensure_name(path: Path) -> None:
    """Add `name:` as the first frontmatter key if missing (required by Cursor for commands and agents)."""
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    if fm is None or re.search(r"^name:\s*", fm, re.M):
        return
    path.write_text(f"---\nname: {path.stem}\n{fm}\n---\n{body}", encoding="utf-8")


def fm_value(fm: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.*)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else ""


def workflow_skill(plugin: str, cmd: Path, all_commands: list) -> str:
    """Translate a Claude Code command into a Codex skill with the same workflow."""
    fm, body = split_frontmatter(cmd.read_text(encoding="utf-8"))
    name = cmd.stem
    m = re.search(r"^# /[\w-]+\s+--\s+(.+)$", body, re.M)
    title = (m.group(1).strip() if m else name.replace("-", " ")).rstrip(".")
    # Trigger-only, like every authored skill: say when to load it, never summarize the steps.
    description = (f"Use when the user invokes ${name}, or asks to run the {title} workflow "
                   f"from the {plugin} plugin end to end.")
    body = body.replace("$ARGUMENTS", "the user's request")
    for other in sorted(all_commands, key=len, reverse=True):
        body = re.sub(rf"(?<![\w/])/{re.escape(other)}(?![\w-])", f"${other}", body)
    # Step 0 in Codex terms: skills are opened from the plugin's skill list, not via a Skill tool.
    body = re.sub(
        r"Your first action must be a Skill tool call for each of these skills: (.*?)\. This command file is only an outline",
        lambda m: ("Before anything else, open and read each of these skills from this plugin's skill list: "
                   + m.group(1) + ". This workflow is only an outline"),
        body,
    )
    note = ("> Generated from the Claude Code command `/" + name + "` by scripts/sync_cross_platform.py. "
            "Do not edit; edit the command instead.\n\n")
    desc_yaml = json.dumps(description, ensure_ascii=False)
    return f"---\nname: {name}\ndescription: {desc_yaml}\n---\n\n{note}{body.lstrip()}"


def main() -> None:
    version = META["version"]
    owner = META["owner"]
    repo_url = f"https://github.com/{META['repo']}"
    codex_entries, cursor_entries = [], []
    counts = {"workflows": 0, "codex": 0, "cursor": 0}
    all_commands = [p.stem for p in ROOT.glob("adlc-*/commands/*.md")]

    for pl in META["plugins"]:
        name = pl["name"]
        pdir = ROOT / name
        commands = sorted((pdir / "commands").glob("*.md"))
        for f in commands + sorted((pdir / "agents").glob("*.md")):
            ensure_name(f)

        # Codex: commands become workflow skills
        wdir = pdir / "workflows"
        if wdir.exists():
            shutil.rmtree(wdir)
        for cmd in commands:
            out = wdir / cmd.stem / "SKILL.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(workflow_skill(name, cmd, all_commands), encoding="utf-8")
            counts["workflows"] += 1

        display = f"ADLC {name.replace('adlc-', '').replace('-', ' ').title()}"
        first_cmds = [c.stem for c in commands][:3]
        dump(pdir / ".codex-plugin" / "plugin.json", {
            "name": name,
            "version": version,
            "description": pl["description"],
            "author": owner,
            "homepage": SITE,
            "repository": repo_url,
            "license": "MIT",
            "keywords": pl["keywords"],
            "skills": ["./skills/", "./workflows/"],
            "interface": {
                "displayName": display,
                "shortDescription": pl["title"],
                "longDescription": pl["description"],
                "developerName": "BrAIght Wave",
                "category": "Coding",
                "capabilities": ["Interactive", "Write"],
                "websiteURL": SITE,
                "defaultPrompt": [f"Run ${c}" for c in first_cmds],
            },
        })
        counts["codex"] += 1

        dump(pdir / ".cursor-plugin" / "plugin.json", {
            "name": name,
            "displayName": display,
            "version": version,
            "description": pl["description"],
            "author": {"name": owner["name"], "email": owner["email"]},
            "homepage": SITE,
            "repository": repo_url,
            "license": "MIT",
            "keywords": pl["keywords"],
        })
        counts["cursor"] += 1

        codex_entries.append({
            "name": name,
            "source": {"source": "local", "path": f"./{name}"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": "Coding",
        })
        cursor_entries.append({"name": name, "source": f"./{name}", "description": pl["description"]})

    dump(ROOT / ".agents" / "plugins" / "marketplace.json", {
        "name": META["marketplace"],
        "interface": {"displayName": "ADLC Skills"},
        "plugins": codex_entries,
    })
    dump(ROOT / ".cursor-plugin" / "marketplace.json", {
        "name": META["marketplace"],
        "owner": {"name": owner["name"], "email": owner["email"]},
        "metadata": {"description": "The Agentic Development Lifecycle as skills, commands and agents.", "version": version},
        "plugins": cursor_entries,
    })
    print(f"Cross-platform: {counts['codex']} Codex and {counts['cursor']} Cursor manifests, {counts['workflows']} Codex workflow skills")


if __name__ == "__main__":
    main()
