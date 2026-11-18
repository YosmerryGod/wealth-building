#!/usr/bin/env python3
"""Validate skills.json paths, Markdown links, and README/INDEX coverage."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []

def fail(message):
    errors.append(message)

index_path = ROOT / "skills.json"
if not index_path.exists():
    fail("skills.json is missing")
    data = {"skills": []}
else:
    data = json.loads(index_path.read_text(encoding="utf-8"))

indexed = {item["path"] for item in data.get("skills", [])}
for path in sorted(indexed):
    if not (ROOT / path).is_file():
        fail(f"skills.json path does not exist: {path}")

actual = {p.relative_to(ROOT).as_posix() for p in ROOT.glob("**/SKILL.md")}
for path in sorted(actual - indexed):
    fail(f"SKILL.md missing from skills.json: {path}")
for path in sorted(indexed - actual):
    fail(f"skills.json points to non-SKILL.md path: {path}")

for markdown in ROOT.glob("**/*.md"):
    if any(part in {".git", ".venv", "node_modules"} for part in markdown.parts):
        continue
    content = markdown.read_text(encoding="utf-8")
    for target in re.findall(r"!?[[^]]*](([^)]+))", content):
        target = target.strip().split()[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = unquote(target.split("#", 1)[0])
        if target and not (markdown.parent / target).resolve().exists():
            fail(f"Broken Markdown link in {markdown.relative_to(ROOT)}: {target}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
index = (ROOT / "INDEX.md").read_text(encoding="utf-8")
if "INDEX.md" not in readme or "RUNTIME.md" not in readme:
    fail("README.md is missing required navigation links")
for path in sorted(indexed):
    if path not in index:
        fail(f"INDEX.md does not include indexed skill path: {path}")
if len(readme.splitlines()) >= 150:
    fail(f"README.md must stay below 150 lines (found {len(readme.splitlines())})")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Validated {len(indexed)} skills, {len(actual)} skill files, Markdown links, and README/INDEX coverage.")
