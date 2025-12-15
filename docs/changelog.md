# Changelog

Короткий журнал изменений “заметок проекта”.

## 2025-12-15
- Добавлен PlantUML style guide в `docs/diagrams/uml.md`.
- Исправлены внутренние ссылки в `docs/notes/index.md` (чтобы `mkdocs build --strict` не падал на warnings).
- Добавлен раздел **Chat bootstrap** в `docs/notes/index.md` (единый сценарий синхронизации контекста через Snapshot).

## 2025-12-13
- Починен локальный рендер PlantUML в CI (зависимости и синтаксис диаграмм).
- Починен `actions/setup-python` pip cache (через `cache-dependency-path`).

> Правило: фиксировать здесь изменения контекста/ADR/инфраструктуры, которые влияют на работу проекта.
