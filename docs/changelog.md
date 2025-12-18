# Changelog

Короткий журнал изменений “заметок проекта”.

## 2025-12-18
* Зафиксирована гипотеза упаковки и цен: добавлен `docs/monetization/pricing_packaging.md`.
* В ADR 0002 добавлен Appendix с feature matrix + pricing bands (v0).
* В `docs/context.md`, `docs/roadmap.md`, `docs/notes/index.md` добавлены ссылки на Pricing & Packaging как на текущую точку правды.

## 2025-12-15
* Добавлен PlantUML style guide в `docs/diagrams/uml.md`.
* Исправлены внутренние ссылки в `docs/notes/index.md` (чтобы `mkdocs build --strict` не падал на warnings).
* Устранены предупреждения MkDocs из Snapshot: ссылки на ADR теперь корректно переписываются в генераторе снапшота.
* В Snapshot и Notes Index добавлен **Chat bootstrap** (как синхронизировать контекст в новом чате через Snapshot).

## 2025-12-13
* Починен локальный рендер PlantUML в CI (зависимости и синтаксис диаграмм).
* Починен `actions/setup-python` pip cache (через `cache-dependency-path`).

> Правило: фиксировать здесь изменения контекста/ADR/инфраструктуры, которые влияют на работу проекта.
