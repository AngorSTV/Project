#!/usr/bin/env python3
"""Generate docs/_snapshot.md for fast context sync.

Design goals:
- No third-party dependencies.
- Deterministic output.
- Works regardless of current working directory.

Notes:
- This file is generated during CI build and included into the Pages artifact.
- The repository copy of docs/_snapshot.md may be a placeholder.
"""

from __future__ import annotations

import glob
import os
import re
from datetime import datetime, timezone


def _read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def _repo_root() -> str:
    # tools/generate_snapshot.py -> repo root
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def _rewrite_links(markdown: str) -> str:
    """Rewrite relative links so they resolve from docs/_snapshot.md.

    The snapshot lives in docs/_snapshot.md (docs root). When we embed content from
    docs/adr/*.md, links like '0002-foo.md' become broken because they were intended
    to be relative to docs/adr/. Here we rewrite those to 'adr/0002-foo.md'.

    We also handle optional anchors: 0002-foo.md#section.
    """

    def repl(m: re.Match[str]) -> str:
        text = m.group(1)
        target = m.group(2)

        # Only rewrite simple ADR filename links (0001-*.md etc.) that are not already prefixed.
        if re.match(r"^(000\d-[^/]+\.md)(#.*)?$", target):
            return f"[{text}](adr/{target})"

        return m.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, markdown)


def main() -> None:
    repo_root = _repo_root()

    docs_root = os.path.join(repo_root, "docs")
    out_path = os.path.join(docs_root, "_snapshot.md")

    parts: list[tuple[str, str]] = []

    def add(title: str, rel_path: str) -> None:
        abs_path = os.path.join(repo_root, rel_path)
        if os.path.exists(abs_path):
            body = _read(abs_path)
            parts.append((title, _rewrite_links(body)))

    # Core
    add("Status / Context", "docs/context.md")
    add("Roadmap", "docs/roadmap.md")

    # ADR index + latest ADRs
    add("Decisions (ADR) – Index", "docs/adr/index.md")

    adr_dir = os.path.join(docs_root, "adr")
    adr_files = sorted(
        [
            p
            for p in glob.glob(os.path.join(adr_dir, "*.md"))
            if not p.endswith("index.md")
        ]
    )

    # Include up to last 5 ADRs by filename sort.
    for p in adr_files[-5:]:
        rel = os.path.relpath(p, repo_root)
        add(f"ADR: {os.path.basename(p)}", rel)

    # Changelog
    add("Changelog", "docs/changelog.md")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    out: list[str] = []
    out.append("# Snapshot")
    out.append("")
    out.append(f"Generated: **{now}**")
    out.append("")
    out.append("Эта страница — единый агрегированный контекст проекта (для быстрой синхронизации в новых чатах).")
    out.append("")
    out.append("## Chat bootstrap")
    out.append("")
    out.append("1. Проверь строку `Generated:` (контекст актуален, если дата свежая).")
    out.append("2. Пробеги глазами разделы **Status / Context** и **Roadmap**.")
    out.append("3. Для решений и политики смотри соответствующие **ADR** (ссылки ниже должны открываться корректно).")
    out.append("4. Для истории изменений — **Changelog**.")

    for title, body in parts:
        out.append("\n---\n")
        out.append(f"## {title}")
        out.append("")
        out.append(body)

    out.append("")

    os.makedirs(docs_root, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out).rstrip() + "\n")

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
