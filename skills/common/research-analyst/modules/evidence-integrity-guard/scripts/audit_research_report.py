#!/usr/bin/env python3
"""Heuristic lint for unsupported-looking claims and citation defects in Markdown.

This script never determines factual truth. It flags places that need human/model
verification against opened sources.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


URL_RE = re.compile(r"https?://[^\s)>\]]+")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
NUMERIC_RE = re.compile(
    r"(?:\b(?:19|20)\d{2}\b|"
    r"(?<!\w)(?:\d{1,3}(?:[.,]\d{3})+|\d+(?:[.,]\d+)?)\s?"
    r"(?:%|TL|TRY|USD|EUR|GBP|₺|\$|€|mg|g|kg|cm|mm|km|x)\b|"
    r"(?<![\w.-])\d{2,}(?:[.,]\d+)?(?![\w.-]))",
    re.I,
)
DATE_RE = re.compile(r"\b(?:19|20)\d{2}\b")
# A linked numeric label such as `[1](https://...)` is already a self-contained
# citation, not a reference-list marker that needs a separate `[1]` definition.
NUMERIC_CITATION_RE = re.compile(r"\[([0-9]+)\](?!\()")
AUTHOR_YEAR_RE = re.compile(r"\([A-ZÇĞİÖŞÜ][^)]*,\s*(?:19|20)\d{2}[a-z]?\)")
NUMERIC_REFERENCE_RE = re.compile(
    r"^\s*(?:\[([0-9]+)\](?::|\s+)|(\d+)[.)]\s+).*(?:https?://|doi\b|pmid\b|(?:19|20)\d{2})",
    re.I,
)
CERTAINTY_RE = re.compile(r"\b(?:kesin(?:likle)?|garanti|kanıtlar|ispatlar|şüphesiz|always|never|guarantee[sd]?|proves?)\b", re.I)
PLACEHOLDER_RE = re.compile(r"(?:\bTODO\b|\bTBD\b|\bexample\.com\b|\[insert\b|<insert\b|\bXX+\b)", re.I)
HEADING_OR_CODE_RE = re.compile(r"^\s*(?:#|```|[-*]\s*$)")
QUALIFIER_RE = re.compile(r"\b(?:örnek|varsayım|senaryo|tahmin|yaklaşık|illustrative|example|assumption|scenario|estimate|estimated)\b", re.I)


def lint(text: str) -> dict:
    issues: list[dict[str, object]] = []
    urls = [match.rstrip(".,;:") for match in URL_RE.findall(text)]
    duplicates = sorted({url for url in urls if urls.count(url) > 1})
    reference_ids: set[str] = set()
    for candidate in text.splitlines():
        match = NUMERIC_REFERENCE_RE.search(candidate)
        if match:
            reference_ids.add(match.group(1) or match.group(2))

    in_code_fence = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue
        if PLACEHOLDER_RE.search(line):
            issues.append({"severity": "critical", "line": lineno, "code": "placeholder", "text": line.strip()[:180]})
        if CERTAINTY_RE.search(line) and not QUALIFIER_RE.search(line):
            issues.append({"severity": "warning", "line": lineno, "code": "absolute-certainty", "text": line.strip()[:180]})
        citation_ids = set(NUMERIC_CITATION_RE.findall(line))
        is_reference_definition = NUMERIC_REFERENCE_RE.search(line) is not None
        dangling_ids = sorted(citation_ids - reference_ids, key=int)
        if dangling_ids and not is_reference_definition:
            issues.append({
                "severity": "warning",
                "line": lineno,
                "code": "dangling-citation-marker",
                "text": f"Undefined reference marker(s): {', '.join(f'[{item}]' for item in dangling_ids)}",
            })
        is_table_row = line.lstrip().startswith("|")
        if HEADING_OR_CODE_RE.search(line) or (len(line.strip()) < 20 and not is_table_row):
            continue
        prose = re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", "", line)
        has_material_number = bool(NUMERIC_RE.search(prose) or DATE_RE.search(prose))
        has_resolved_numeric_citation = bool(citation_ids & reference_ids)
        has_visible_support = bool(
            URL_RE.search(line)
            or MARKDOWN_LINK_RE.search(line)
            or AUTHOR_YEAR_RE.search(line)
            or has_resolved_numeric_citation
        )
        if has_material_number and not has_visible_support and not QUALIFIER_RE.search(line):
            issues.append({"severity": "warning", "line": lineno, "code": "numeric-claim-needs-source-or-label", "text": line.strip()[:180]})

    for url in duplicates:
        issues.append({"severity": "info", "line": None, "code": "duplicate-link", "text": url[:180]})

    bare_urls = set(urls) - set(MARKDOWN_LINK_RE.findall(text))
    for url in sorted(bare_urls):
        issues.append({"severity": "info", "line": None, "code": "bare-url", "text": url[:180]})

    counts = {level: sum(issue["severity"] == level for issue in issues) for level in ("critical", "warning", "info")}
    status = "FAIL" if counts["critical"] else "REVIEW" if counts["warning"] else "PASS"
    return {
        "status": status,
        "disclaimer": "Heuristic lint only; PASS does not prove factual truth or source support.",
        "counts": counts,
        "issues": issues,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    result = lint(args.report.read_text(encoding="utf-8"))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["status"] == "FAIL" else 2 if result["status"] == "REVIEW" else 0


if __name__ == "__main__":
    raise SystemExit(main())
