# Agent Windows 10/11

## Связанные документы

- Методики измерений: [metrics/measurement_methodology.md](metrics/measurement_methodology.md)
- Архитектура: [architecture.md](architecture.md)
- SLA & Risks: [sla_risks.md](sla_risks.md)

## Стек используемых технологий

- Язык: C# (.NET 8)
- UI: WPF, livechartscore.skiasharpview.wpf 2.0.0-rc5.4
- Сбор данных: LibreHardwareMonitor, WMI, DirectX
- Обновления: Squirrel.Windows или кастомные
- Логирование: Serilog

## Сбор метрик

Источник правды по метрикам и интерпретации: [metrics/measurement_methodology.md](metrics/measurement_methodology.md)

### Базовый набор (MVP)

Использование LibreHardwareMonitor 0.9.4, сбор:

- CPU (temp, freq, load, power)
- GPU (load, temp, vram)
- RAM usage
- Disk I/O
- Fans, PSU

### Производительность (FPS / frametime)

Метрики FPS/frametime относятся к классу “поведенческих” и должны собираться согласованно с тестовым сценарием (игра/бенч). Минимальный контракт:

- P50 FPS, P1, 0.1% low
- jitter (вариативность frametime)
- stutter count (события фризов/скачков)

Примечание: конкретный механизм сборки frametime должен быть единым и воспроизводимым (важно для будущих отчётов и сравнения между тестами).

### Quality flags (качество данных)

Agent обязан маркировать качество данных (минимально):

- missing sensors (часть датчиков недоступна)
- gaps / sampling anomalies (пропуски/аномалии)
- подтверждённый throttling
- crash/errors
- sandbox integrity (если применимо)

Это напрямую влияет на:
- UI “светофор” и предупреждения,
- метрику `% incomplete_tests` в SLA,
- доверие к ML-предсказаниям.

## Архитектура агента

    +-------------------------------+
    |        WPF UI (Charts)        |
    +-------------------------------+
    | LiveCharts ⟷ Metrics Buffer   |
    +-------------------------------+
    | LibreHardwareMonitor Service  |
    +-------------------------------+
    | ZIP Packager & Network Sender |
    +-------------------------------+

## Отправка данных

Файлы JSON → ZIP → POST /api/upload (multipart/form-data).

Рекомендуемая структура артефакта теста (в перспективе для аналитики/отчётов):
- `metrics/*.json` — временные ряды и агрегаты
- `logs/*.txt|json` — логи тестов/агента
- `meta.json` — версия агента, сценарий, quality flags, окружение

## План развития

- автообновление
- очереди повторной отправки
- улучшенная обработка ошибок драйверов
- формализация “quality flags” как контракта (Agent → Backend → Frontend/ML)
