# Архитектура

## Общий обзор

```plantuml
@startuml
skinparam shadowing false
skinparam monochrome true

agent "PC Agent (.NET)" as AG
control "Backend API\nSpring Boot" as BE
database "PostgreSQL" as DB
queue "Kafka" as K
cloud "ML Service\nPython" as ML
cloud "Frontend Angular" as FE
storage "S3 Storage" as S3

AG --> BE : Upload metrics ZIP
BE --> K : push metric tasks
K --> ML : consume events
ML --> BE : predictions
BE --> FE : REST/SSE
BE --> DB : store tests
BE --> S3 : store archives
@enduml
```

## Пояснения
- **AG** собирает метрики и отправляет архив теста (ZIP).
- **BE** принимает тест, сохраняет артефакты и публикует задачу обработки.
- **Kafka** используется как транспорт для асинхронной обработки.
- **ML** рассчитывает предсказания/инсайты и возвращает их в Backend.
- **FE** отображает результаты пользователю, включая live‑метрики (SSE).
