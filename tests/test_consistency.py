"""Consistency tests: README counts, manifest sync, version sync, CHANGELOG format."""
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MP = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))


def counts():
    s = c = a = 0
    for e in MP["plugins"]:
        d = ROOT / e["source"].lstrip("./")
        s += len(list(d.glob("skills/*/SKILL.md")))
        c += len(list(d.glob("commands/*.md")))
        a += len(list(d.glob("agents/*.md")))
    return s, c, a


class TestConsistency(unittest.TestCase):
    def test_validator_passes(self):
        r = subprocess.run([sys.executable, str(ROOT / "validate_plugins.py")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_marketplace_lists_every_plugin_dir(self):
        dirs = {p.parent.parent.name for p in ROOT.glob("*/.claude-plugin/plugin.json")}
        listed = {e["name"] for e in MP["plugins"]}
        self.assertEqual(dirs, listed)

    def test_versions_in_sync(self):
        latest = re.search(r"^## v(\d+\.\d+\.\d+)", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), re.M).group(1)
        self.assertEqual(MP["version"], latest)
        for e in MP["plugins"]:
            man = json.loads((ROOT / e["name"] / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
            self.assertEqual(man["version"], latest, e["name"])

    def test_readme_headline_counts(self):
        s, c, a = counts()
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"{s} skills", readme)
        self.assertIn(f"{c} commands", readme)
        self.assertIn(f"{len(MP['plugins'])} plugins", readme)
        self.assertIn(f"{s} skills", MP["description"])

    def test_readme_eval_count(self):
        n = sum(len(list((ROOT / e["name"]).glob("evals/*/prompt.md"))) for e in MP["plugins"])
        self.assertIn(f"{n} eval cases", (ROOT / "README.md").read_text(encoding="utf-8"))

    def test_every_skill_has_eval_case(self):
        for e in MP["plugins"]:
            d = ROOT / e["name"]
            graders = "".join(g.read_text(encoding="utf-8") for g in d.glob("evals/*/graders/*.md"))
            for sk in d.glob("skills/*/SKILL.md"):
                self.assertIn(sk.parent.name, graders, f"{e['name']}:{sk.parent.name} has no eval case")

    def test_readme_per_plugin_counts(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for e in MP["plugins"]:
            d = ROOT / e["name"]
            s = len(list(d.glob("skills/*/SKILL.md")))
            c = len(list(d.glob("commands/*.md")))
            self.assertRegex(readme, rf"{re.escape(e['name'])}.*\({s} skills, {c} commands", e["name"])

    def test_plugin_readmes_match_disk(self):
        for e in MP["plugins"]:
            d = ROOT / e["name"]
            txt = (d / "README.md").read_text(encoding="utf-8")
            for sk in d.glob("skills/*/SKILL.md"):
                self.assertIn(f"`{sk.parent.name}`", txt)
            for cmd in d.glob("commands/*.md"):
                self.assertIn(f"`/{cmd.stem}`", txt)


if __name__ == "__main__":
    unittest.main()
