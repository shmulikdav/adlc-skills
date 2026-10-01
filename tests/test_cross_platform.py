"""Codex and Cursor packaging stays consistent with the Claude Code plugins."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = json.loads((ROOT / "scripts" / "plugins_meta.json").read_text(encoding="utf-8"))
NAME_RE = re.compile(r"^[a-z0-9]([a-z0-9.-]*[a-z0-9])?$")


def frontmatter_keys(path: Path) -> set:
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    return {line.split(":")[0].strip() for line in m.group(1).splitlines() if ":" in line} if m else set()


class CrossPlatform(unittest.TestCase):
    def test_manifests_agree(self):
        for pl in META["plugins"]:
            pdir = ROOT / pl["name"]
            claude = json.loads((pdir / ".claude-plugin" / "plugin.json").read_text())
            codex = json.loads((pdir / ".codex-plugin" / "plugin.json").read_text())
            cursor = json.loads((pdir / ".cursor-plugin" / "plugin.json").read_text())
            for m in (codex, cursor):
                self.assertEqual(m["name"], pl["name"])
                self.assertEqual(m["version"], claude["version"])
            self.assertRegex(pl["name"], NAME_RE)

    def test_codex_sees_skills_and_workflows(self):
        # Codex 0.159 replaces default skills/ discovery when `skills` is set, so both paths must be listed.
        for pl in META["plugins"]:
            codex = json.loads((ROOT / pl["name"] / ".codex-plugin" / "plugin.json").read_text())
            self.assertEqual(codex["skills"], ["./skills/", "./workflows/"])
            for key in ("displayName", "shortDescription", "developerName", "category"):
                self.assertTrue(codex["interface"].get(key), f"{pl['name']}: interface.{key}")

    def test_every_command_has_a_codex_workflow(self):
        for pl in META["plugins"]:
            pdir = ROOT / pl["name"]
            cmds = {p.stem for p in (pdir / "commands").glob("*.md")}
            wfs = {p.parent.name for p in (pdir / "workflows").glob("*/SKILL.md")}
            self.assertEqual(cmds, wfs, pl["name"])
            for wf in (pdir / "workflows").glob("*/SKILL.md"):
                self.assertNotIn("Skill tool call", wf.read_text(), f"{wf}: Claude-specific Step 0 left in Codex workflow")

    def test_cursor_frontmatter(self):
        for pl in META["plugins"]:
            pdir = ROOT / pl["name"]
            for glob in ("skills/*/SKILL.md", "commands/*.md", "agents/*.md"):
                for f in pdir.glob(glob):
                    keys = frontmatter_keys(f)
                    self.assertIn("name", keys, f"{f}: Cursor requires name")
                    self.assertIn("description", keys, f"{f}: Cursor requires description")

    def test_marketplaces_list_all_plugins(self):
        names = [pl["name"] for pl in META["plugins"]]
        codex = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text())
        cursor = json.loads((ROOT / ".cursor-plugin" / "marketplace.json").read_text())
        self.assertEqual([p["name"] for p in codex["plugins"]], names)
        self.assertEqual([p["name"] for p in cursor["plugins"]], names)
        for p in codex["plugins"]:
            self.assertEqual(p["source"], {"source": "local", "path": f"./{p['name']}"})
            self.assertIn(p["policy"]["installation"], {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"})
        for p in cursor["plugins"]:
            self.assertEqual(p["source"], f"./{p['name']}")


if __name__ == "__main__":
    unittest.main()
