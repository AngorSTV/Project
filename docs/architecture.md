
# Архитектура

## Общий обзор

```plantuml
@startuml
agent "PC Agent (.NET)" as AG
control "Backend API
Spring Boot" as BE
database "PostgreSQL" as DB
queue "Kafka" as K
cloud "ML Service
Python" as ML
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

## Потоки данных
1. Агент → Backend: загрузка zip архива с метриками
2. Backend → Kafka: постановка задач обработки
3. ML → Backend: предсказания FPS и рекомендации
4. Backend → FE: отображение результатов в реальном времени
