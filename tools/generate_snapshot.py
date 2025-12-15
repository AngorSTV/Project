#!/usr/bin/env python3
"""Generate docs/_snapshot.md for fast context sync.

This script intentionally stays dependency-free.
It concatenates selected key documents into a single Markdown page.
"""

from __future__ import annotations

import glob
import os
from datetime import datetime, timezone


def _read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def main() -> None:
    repo_root = os.path.abspath(os.path.dirname(__file__))

    docs_root = os.path.join(repo_root, "docs")
    out_path = os.path.join(docs_root, "_snapshot.md")

    parts: list[tuple[str, str]] = []

    def add(title: str, rel_path: str) -> None:
        abs_path = os.path.join(repo_root, rel_path)
        if os.path.exists(abs_path):
            parts.append((title, _read(abs_path)))

    # Core
    add("Status / Context", "docs/context.md")
    add("Roadmap", "docs/roadmap.md")

    # ADR index + latest ADRs
    add("Decisions (ADR) – Index", "docs/adr/index.md")

    adr_dir = os.path.join(docs_root, "adr")
    adr_files = sorted(
        [p for p in glob.glob(os.path.join(adr_dir, "*.md")) if not p.endswith("0001-template.md") and not p.endswith("index.md")]
    )

    # Include up to last 5 ADRs by filename sort.
    for p in adr_files[-5:]:
        rel = os.path.relpath(p, repo_root)
        add(f"ADR: {os.path.basename(p)}", rel)

    # Changelog
    add("Changelog", "docs/changelog.md")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    out = []
    out.append("# Snapshot")
    out.append("")
    out.append(f"Generated: **{now}**")
    out.append("")
    out.append("Этот файл — агрегированный срез ключевых заметок проекта (для быстрой синхронизации контекста).")

    for title, body in parts:
        out.append("\n---\n")
        out.append(f"## {title}")
        out.append("")
        out.append(body)

    out.append("\n")

    os.makedirs(docs_root, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out).rstrip() + "\n")

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
