# ML Module

## Связанные документы

- Методики измерений: [metrics/measurement_methodology.md](metrics/measurement_methodology.md)
- Архитектура: [architecture.md](architecture.md)
- SLA & Risks: [sla_risks.md](sla_risks.md)

## Цель ML слоя

1) Производные инсайты и прогнозы (например, Predicted FPS gain).
2) Улучшение качества рекомендаций на базе исторических данных.
3) Контроль доверия: качество входных данных (quality flags) и стабильность моделей (дрейф).

## Pipeline

1. Preprocessing
2. Feature engineering
3. XGBoost model
4. PyTorch model (deep FPS prediction)
5. Postprocessing recommendations

## Диаграмма

    Raw Metrics --> Preprocess --> Model(XGBoost/PyTorch) --> FPS Prediction --> Recommendations

## Контракты входа (минимум)

ML получает:
- агрегаты метрик (percentiles/low/jitter/stutter, load/temp/throttling и т.п.)
- метаданные теста (hardware profile, версия агента, сценарий)
- quality flags (как первичный сигнал доверия)

Источник определений: [metrics/measurement_methodology.md](metrics/measurement_methodology.md)

## Выходы ML (минимум)

- `predicted_fps_gain` (Pro): прогноз эффекта от апгрейда/изменения конфигурации
- `confidence` / `reliability` (обязательное поле для UI и отчётов)
- объясняющие факторы (top features) — по возможности, чтобы поддержать explainability

## Мониторинг качества (для 2026 и B2B-ready)

- accuracy на эталонном наборе
- детект дрейфа (данные/фичи/ошибка)
- возможность rollback модели (версионирование + быстрый откат)
