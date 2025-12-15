# Project Notes Index

Эта страница — точка входа в “заметки проекта” и самый быстрый способ синхронизировать контекст.

## Читать в первую очередь

- **Status / Context**: [context](../context.md)
- **Roadmap**: [roadmap](../roadmap.md)
- **Snapshot (автогенерация в CI)**: [snapshot](../_snapshot.md)
- **Decisions (ADR)**: [ADR index](../adr/index.md)
- **Changelog**: [changelog](../changelog.md)

## Chat bootstrap

Если ты открываешь новый чат по проекту и нужно быстро синхронизировать общий контекст:

1. Открой **Snapshot** и проверь время генерации (строка `Generated:`).
2. Пробеги глазами **Status / Context** и **Roadmap** — это оперативный “источник правды”.
3. Если обсуждение упирается в политику/решение — смотри соответствующий **ADR**.
4. Если непонятно “почему так стало” — смотри **Changelog** за последние даты.

> Snapshot на GitHub Pages всегда актуален: он генерируется в CI перед `mkdocs build` и попадает в артефакт Pages.

## Ссылки (Pages / raw)

> Pages — предпочтительно. Raw — резервный вариант (если нужно открыть исходник напрямую).

- Status / Context:
  - Pages: `context/`
  - Raw: `https://raw.githubusercontent.com/AngorSTV/Project/main/docs/context.md`

- Roadmap:
  - Pages: `roadmap/`
  - Raw: `https://raw.githubusercontent.com/AngorSTV/Project/main/docs/roadmap.md`

- Snapshot:
  - Pages: `_snapshot/`
  - Raw: `docs/_snapshot.md` (в репозитории может быть placeholder; актуальная версия всегда в Pages, т.к. генерируется в CI при сборке)

- ADR index:
  - Pages: `adr/`
  - Raw: `https://raw.githubusercontent.com/AngorSTV/Project/main/docs/adr/index.md`

- Changelog:
  - Pages: `changelog/`
  - Raw: `https://raw.githubusercontent.com/AngorSTV/Project/main/docs/changelog.md`

## Как вносить изменения

- Любые изменения заметок и решений делать через PR.
- В описании PR писать 3–7 буллетов “Summary for Context”.
- Все изменения, которые влияют на рекомендации/монетизацию/деплой, фиксировать ADR.
