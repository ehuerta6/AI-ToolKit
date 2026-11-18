#!/usr/bin/env python3
"""Lightweight consistency checks for the AI Toolkit catalog."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_local_markdown_links(
    doc: Path, content: str, errors: list[str], root: Path
) -> None:
    """Catch broken relative Markdown links while ignoring fenced code examples."""
    content = re.sub(
        r"(?ms)^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?^ {0,3}\1[ \t]*$",
        "",
        content,
    )
    content = re.sub(r"(?<!`)`+[^`\n]*`+(?!`)", "", content)
    doc = doc.resolve()
    patterns = (
        re.compile(r"!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))"),
        re.compile(r"(?m)^ {0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|([^\s]+))"),
    )
    root = root.resolve()
    for pattern in patterns:
        for match in pattern.finditer(content):
            destination = match.group(1) or match.group(2)
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target_name = unquote(parsed.path)
            if Path(target_name).suffix.lower() not in {".md", ".markdown"}:
                continue
            target = (doc.parent / target_name).resolve()
            if not target.is_relative_to(root):
                fail(
                    errors,
                    f"{doc.relative_to(root)} links outside the repository: '{destination}'",
                )
            elif not target.is_file():
                fail(errors, f"{doc.relative_to(root)} links to missing Markdown file '{destination}'")


def main() -> int:
    errors: list[str] = []
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    for path in skills:
        content = path.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            fail(errors, f"{path.relative_to(ROOT)} has no YAML front matter")
            continue
        parts = content.split("---\n", 2)
        if len(parts) < 3:
            fail(errors, f"{path.relative_to(ROOT)} has unclosed front matter")
            continue
        metadata = parts[1]
        name = re.search(r"^name:\s*([^\s#]+)\s*$", metadata, re.M)
        description = re.search(r"^description:\s*(.*?)\s*$", metadata, re.M)
        expected = path.parent.name
        if not name:
            fail(errors, f"{path.relative_to(ROOT)} is missing a valid name field")
        else:
            skill_name = name.group(1)
            if len(skill_name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_name):
                fail(errors, f"{path.relative_to(ROOT)} name does not meet Agent Skills naming requirements")
            if skill_name != expected:
                fail(errors, f"{path.relative_to(ROOT)} name '{skill_name}' does not match directory '{expected}'")
        if not description or not description.group(1):
            fail(errors, f"{path.relative_to(ROOT)} is missing a valid description field")
        elif len(description.group(1)) > 1024:
            fail(errors, f"{path.relative_to(ROOT)} description exceeds 1024 characters")
        if re.search(r"^metadata:\s*(?:#.*)?$", metadata, re.M):
            fail(errors, f"{path.relative_to(ROOT)} has empty metadata; omit it or provide string key-value fields")

    # Catch common repository-relative references in catalog and instruction docs.
    docs = sorted(
        path
        for path in ROOT.rglob("*.md")
        if not {".git", "node_modules", "dist"}.intersection(path.parts)
    )
    path_pattern = re.compile(r"(?<![\w./-])((?:skills|agents|rules|templates|project-instructions|scripts)/[\w./-]+\.(?:md|py))(?![\w.-])")
    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        check_local_markdown_links(doc, text, errors, ROOT)
        for ref in path_pattern.findall(text):
            if not (ROOT / ref).is_file():
                fail(errors, f"{doc.relative_to(ROOT)} references missing file '{ref}'")

    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Catalog validation passed ({len(skills)} skills, {len(list((ROOT / 'agents').glob('*.md')))} agents, {len(list((ROOT / 'project-instructions').glob('*.md')))} Project Instructions).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
