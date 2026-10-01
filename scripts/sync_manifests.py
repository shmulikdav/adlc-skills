#!/usr/bin/env python3
"""Regenerate plugin.json files, per-plugin READMEs, and marketplace.json from
scripts/plugins_meta.json plus the skill/command/agent files on disk.

Run after adding, removing, or renaming a skill, command, or agent:
    python3 scripts/sync_manifests.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = json.loads((ROOT / "scripts" / "plugins_meta.json").read_text(encoding="utf-8"))


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    out = {}
    if not m:
        return out
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if kv:
            out[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return out


def first_sentence(text: str) -> str:
    s = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]
    return s.rstrip(".")


def inventory(pdir: Path):
    skills = sorted((p.parent.name, frontmatter(p)) for p in pdir.glob("skills/*/SKILL.md"))
    commands = sorted((p.stem, frontmatter(p)) for p in pdir.glob("commands/*.md"))
    agents = sorted((p.stem, frontmatter(p)) for p in pdir.glob("agents/*.md"))
    return skills, commands, agents


def main():
    version = META["version"]
    owner = META["owner"]
    entries = []
    totals = {"skills": 0, "commands": 0, "agents": 0}
    for pl in META["plugins"]:
        pdir = ROOT / pl["name"]
        skills, commands, agents = inventory(pdir)
        totals["skills"] += len(skills)
        totals["commands"] += len(commands)
        totals["agents"] += len(agents)

        manifest = {
            "name": pl["name"],
            "displayName": "ADLC " + pl["name"].replace("adlc-", "").replace("-", " ").title(),
            "version": version,
            "description": pl["description"],
            "author": owner,
            "homepage": f"https://github.com/{META['repo']}",
            "repository": f"https://github.com/{META['repo']}",
            "license": "MIT",
            "keywords": pl["keywords"],
        }
        (pdir / ".claude-plugin").mkdir(exist_ok=True)
        (pdir / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        lines = [f"# {pl['name']} — {pl['title']}", "", f"**ADLC phase:** {pl['phase']}", "", "## Overview", "", pl["description"], "",
                 "## Install", "", "```", f"claude plugin marketplace add {META['repo']}", f"claude plugin install {pl['name']}@{META['marketplace']}", "```", "",
                 f"## Skills ({len(skills)})", ""]
        lines += [f"- `{n}` — {first_sentence(fm.get('description', ''))}" for n, fm in skills]
        lines += ["", f"## Commands ({len(commands)})", ""]
        lines += [f"- `/{n}` — {fm.get('description', '')}" for n, fm in commands]
        n_evals = len(list(pdir.glob("evals/*/prompt.md")))
        if agents:
            lines += ["", f"## Agents ({len(agents)})", ""]
            lines += [f"- `{n}` — {first_sentence(fm.get('description', ''))}" for n, fm in agents]
        lines += ["", f"## Evals ({n_evals} cases)", "", "Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.", "", "```", f"claude plugin eval ./{pl['name']}", "```"]
        lines += ["", "---", "", "Part of [ADLC Skills](../README.md). MIT licensed.", ""]
        (pdir / "README.md").write_text("\n".join(lines), encoding="utf-8")

        entries.append({"name": pl["name"], "description": pl["description"], "source": f"./{pl['name']}", "category": "development"})

    marketplace = {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": META["marketplace"],
        "version": version,
        "description": (f"ADLC Skills: the Agentic Development Lifecycle as {totals['skills']} skills, {totals['commands']} commands and "
                        f"{totals['agents']} agents across {len(entries)} plugins — from readiness and agent-ready specs to context engineering, "
                        "agentic build, verification, governance, operations, and agent engineering."),
        "owner": owner,
        "plugins": entries,
    }
    (ROOT / ".claude-plugin" / "marketplace.json").write_text(json.dumps(marketplace, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Synced {len(entries)} plugins: {totals}")
    import sync_cross_platform
    sync_cross_platform.main()


if __name__ == "__main__":
    main()
