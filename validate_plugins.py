#!/usr/bin/env python3
"""ADLC Skills validator.

Checks every plugin listed in .claude-plugin/marketplace.json:
- plugin.json: required fields, name matches directory, semver, author, keywords
- skills/<name>/SKILL.md: frontmatter with name + description; name matches directory; kebab-case
- commands/*.md: frontmatter with description + argument-hint; uses $ARGUMENTS
- agents/*.md: frontmatter with name + description
- commands only reference skills that exist in the same plugin (no cross-plugin hard references)
- README.md present
Exit code 1 on any error.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KEBAB = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
errors, warnings = [], []


def fm(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    data = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if kv:
            data[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return data, text[m.end():]


def err(msg):
    errors.append(msg)


def main():
    mp_path = ROOT / ".claude-plugin" / "marketplace.json"
    mp = json.loads(mp_path.read_text(encoding="utf-8"))
    for key in ("name", "owner", "plugins"):
        if key not in mp:
            err(f"marketplace.json: missing '{key}'")
    all_skill_names = {}
    for entry in mp.get("plugins", []):
        name = entry["name"]
        pdir = ROOT / entry["source"].lstrip("./")
        if not pdir.is_dir():
            err(f"{name}: source directory {entry['source']} not found")
            continue
        man_path = pdir / ".claude-plugin" / "plugin.json"
        if not man_path.exists():
            err(f"{name}: missing .claude-plugin/plugin.json")
            continue
        man = json.loads(man_path.read_text(encoding="utf-8"))
        for f in ("name", "version", "description", "author", "keywords", "license"):
            if f not in man:
                err(f"{name}: plugin.json missing '{f}'")
        if man.get("name") != pdir.name:
            err(f"{name}: plugin.json name '{man.get('name')}' != directory '{pdir.name}'")
        if not SEMVER.match(str(man.get("version", ""))):
            err(f"{name}: version is not semver")
        if "name" not in man.get("author", {}):
            err(f"{name}: author.name required")
        extra = [p.name for p in (pdir / ".claude-plugin").iterdir() if p.name != "plugin.json"]
        if extra:
            err(f"{name}: only plugin.json belongs in .claude-plugin/ (found {extra})")
        if not (pdir / "README.md").exists():
            err(f"{name}: README.md missing")

        skills = set()
        for sk in sorted(pdir.glob("skills/*/SKILL.md")):
            d, body = fm(sk)
            rel = sk.relative_to(ROOT)
            if d is None:
                err(f"{rel}: missing YAML frontmatter")
                continue
            for f in ("name", "description"):
                if not d.get(f):
                    err(f"{rel}: frontmatter '{f}' required")
            if d.get("name") != sk.parent.name:
                err(f"{rel}: name '{d.get('name')}' must match directory '{sk.parent.name}'")
            if not KEBAB.match(sk.parent.name):
                err(f"{rel}: skill directory must be kebab-case")
            desc = d.get("description", "")
            if len(desc) > 1024:
                err(f"{rel}: description exceeds 1024 characters")
            if not re.match(r"^Use (when|before|after) ", desc):
                err(f"{rel}: description must start with 'Use when/before/after' (trigger conditions, not a workflow summary)")
            if len(desc) > 500:
                warnings.append(f"{rel}: description over 500 characters")
            if len(body.splitlines()) > 500:
                warnings.append(f"{rel}: body over 500 lines; consider references/")
            if sk.parent.name in all_skill_names:
                err(f"{rel}: skill name duplicates {all_skill_names[sk.parent.name]}")
            all_skill_names[sk.parent.name] = name
            skills.add(sk.parent.name)

        for cmd in sorted(pdir.glob("commands/*.md")):
            d, body = fm(cmd)
            rel = cmd.relative_to(ROOT)
            if d is None:
                err(f"{rel}: missing YAML frontmatter")
                continue
            for f in ("description", "argument-hint"):
                if not d.get(f):
                    err(f"{rel}: frontmatter '{f}' required")
            if "$ARGUMENTS" not in body and "[$ARGUMENTS]" not in body:
                warnings.append(f"{rel}: does not use $ARGUMENTS")
            for ref in re.findall(r"\*\*([a-z0-9-]+)\*\*", body):
                if KEBAB.match(ref) and "-" in ref and ref not in skills and ref in all_skill_names:
                    err(f"{rel}: references skill '{ref}' from another plugin ({all_skill_names[ref]})")

        # eval suite (claude plugin eval format)
        ev = pdir / "evals"
        cases = [c for c in ev.glob("*/prompt.md")] if ev.is_dir() else []
        if not cases:
            warnings.append(f"{name}: no eval suite under evals/")
        tested = set()
        negative = False
        for pm in cases:
            d, body = fm(pm)
            rel = pm.relative_to(ROOT)
            if d is None or not body.strip():
                err(f"{rel}: prompt.md needs frontmatter and a prompt body")
                continue
            graders = list((pm.parent / "graders").glob("*.md"))
            if not graders:
                err(f"{rel}: case has no graders")
            for g in graders:
                gd, _ = fm(g)
                if not gd or gd.get("type") not in {"regex", "tool_used", "tool_order", "file_exists", "llm", "baseline"}:
                    err(f"{g.relative_to(ROOT)}: grader needs a valid type")
                elif gd.get("type") == "tool_used" and gd.get("max") == "0":
                    negative = True
                elif gd.get("type") == "tool_used":
                    mm = re.search(r"\?\)\?([a-z0-9-]+)\\?\"", gd.get("input_match", ""))
                    for s in skills:
                        if s in gd.get("input_match", ""):
                            tested.add(s)
            if re.search(r"\b(" + "|".join(map(re.escape, skills)) + r")\b", body) if skills else False:
                err(f"{rel}: prompt names a skill; use natural phrasing so triggering is actually tested")
        if cases and not negative:
            warnings.append(f"{name}: eval suite has no negative (must-not-trigger) case")
        for s in sorted(skills - tested):
            if cases:
                warnings.append(f"{name}: skill '{s}' has no eval case")

        for ag in sorted(pdir.glob("agents/*.md")):
            d, _ = fm(ag)
            rel = ag.relative_to(ROOT)
            if d is None or not d.get("name") or not d.get("description"):
                err(f"{rel}: agent frontmatter needs name + description")
            elif d["name"] != ag.stem:
                err(f"{rel}: agent name must match file name")

    # second pass for cross-plugin refs to skills defined later in the list
    for entry in mp.get("plugins", []):
        pdir = ROOT / entry["source"].lstrip("./")
        own = {p.parent.name for p in pdir.glob("skills/*/SKILL.md")}
        for cmd in pdir.glob("commands/*.md"):
            _, body = fm(cmd)
            for ref in set(re.findall(r"\*\*([a-z0-9-]+)\*\*", body)):
                if ref in all_skill_names and ref not in own:
                    msg = f"{cmd.relative_to(ROOT)}: references skill '{ref}' from another plugin ({all_skill_names[ref]})"
                    if msg not in errors:
                        err(msg)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(mp.get('plugins', []))} plugins, {len(all_skill_names)} skills checked — "
          f"{len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
