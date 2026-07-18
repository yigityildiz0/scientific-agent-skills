from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".txt", ".py", ".js", ".ts", ".sh", ".yaml", ".yml", ".json", ".html", ".css", ".svg"}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected", type=int, required=True)
    args = parser.parse_args()
    errors: list[str] = []

    catalog_path = ROOT / "manifests" / "catalog.json"
    docs_catalog_path = ROOT / "docs" / "catalog.json"
    csv_path = ROOT / "manifests" / "catalog.csv"
    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        docs_catalog = json.loads(docs_catalog_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"catalog parse failed: {exc}")
        catalog = []
        docs_catalog = []
    if len(catalog) != args.expected or len(docs_catalog) != args.expected:
        errors.append(f"catalog count mismatch: manifest={len(catalog)} docs={len(docs_catalog)} expected={args.expected}")
    try:
        with csv_path.open(encoding="utf-8", newline="") as stream:
            csv_count = sum(1 for _ in csv.DictReader(stream))
        if csv_count != args.expected:
            errors.append(f"CSV count mismatch: {csv_count}")
    except Exception as exc:
        errors.append(f"CSV parse failed: {exc}")

    for item in catalog:
        for relative in item.get("downloads", {}).values():
            if not (ROOT / relative).is_file():
                errors.append(f"missing package: {relative}")
        archive = item.get("archive_download")
        if archive and not (ROOT / archive).is_file():
            errors.append(f"missing archive package: {archive}")

    for skill_file in sorted((ROOT / "skills").rglob("SKILL.md")):
        try:
            text = skill_file.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"invalid UTF-8: {skill_file.relative_to(ROOT)}: {exc}")
            continue
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
        if not match:
            errors.append(f"missing frontmatter: {skill_file.relative_to(ROOT)}")
            continue
        name_match = re.search(r"(?m)^name:\s*['\"]?([^'\"\n]+)", match.group(1))
        if not name_match:
            errors.append(f"missing frontmatter name: {skill_file.relative_to(ROOT)}")
        elif name_match.group(1).strip() != skill_file.parent.name:
            errors.append(f"name/folder mismatch: {skill_file.relative_to(ROOT)} -> {name_match.group(1).strip()}")

    for package in sorted((ROOT / "packages").rglob("*.zip")):
        try:
            with zipfile.ZipFile(package) as archive:
                if archive.testzip() is not None:
                    errors.append(f"CRC failure: {package.relative_to(ROOT)}")
                roots: set[str] = set()
                for member in archive.infolist():
                    pure = PurePosixPath(member.filename.replace("\\", "/"))
                    if pure.is_absolute() or ".." in pure.parts:
                        errors.append(f"unsafe ZIP member: {package.relative_to(ROOT)}::{member.filename}")
                    if pure.parts:
                        roots.add(pure.parts[0])
                    lowered = member.filename.lower()
                    if "__pycache__" in lowered or lowered.endswith(".pyc"):
                        errors.append(f"cache in ZIP: {package.relative_to(ROOT)}::{member.filename}")
                if roots != {package.stem}:
                    errors.append(f"ZIP root mismatch: {package.relative_to(ROOT)} -> {sorted(roots)}")
        except zipfile.BadZipFile as exc:
            errors.append(f"bad ZIP: {package.relative_to(ROOT)}: {exc}")

    active_pipe = re.compile(r"curl[^\n]*\|\s*(?:ba)?sh\b", re.I)
    for path in sorted(item for item in ROOT.rglob("*") if item.is_file() and item.suffix.lower() in TEXT_SUFFIXES):
        if path.is_symlink():
            errors.append(f"symlink not allowed: {path.relative_to(ROOT)}")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"invalid UTF-8: {path.relative_to(ROOT)}: {exc}")
            continue
        if re.search(r"C:[/\\]Users[/\\]Gaming|C:[/\\]Ai[/\\]ComfyUI", text, re.I):
            errors.append(f"workstation path: {path.relative_to(ROOT)}")
        for line_number, line in enumerate(text.splitlines(), 1):
            lowered = line.lower()
            if active_pipe.search(line) and not any(marker in lowered for marker in ("do not use", "don't use", "never use", "avoid ")):
                errors.append(f"active pipe-to-shell: {path.relative_to(ROOT)}:{line_number}")

    sums = ROOT / "manifests" / "SHA256SUMS.txt"
    if sums.is_file():
        for line in sums.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            expected, relative = line.split(None, 1)
            target = ROOT / relative.strip()
            if not target.exists() and relative.replace("\\", "/").startswith("release-assets/"):
                continue
            if not target.is_file() or digest(target) != expected:
                errors.append(f"checksum mismatch: {relative.strip()}")

    for required in ("README.md", "README.tr.md", "INSTALL.md", "INSTALL.tr.md", "LICENSE.md", "THIRD_PARTY_NOTICES.md", "PUBLISHING.md"):
        if not (ROOT / required).is_file():
            errors.append(f"missing required file: {required}")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALIDATION OK: {args.expected} catalog entries, packages and checksums verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
