
# Backend (Spring Boot 3.5.5)

## Модули
- REST API
- Auth (Keycloak + JWT)
- Processing Queue (Kafka)
- Storage PostgreSQL
- Recommendation Engine
- S3 Storage

## API Sequence

```plantuml
@startuml
participant Agent
participant Backend
participant Kafka
participant ML
participant DB

Agent -> Backend: POST /api/upload
Backend -> DB: save test record
Backend -> Kafka: push task
Kafka -> ML: consume metric event
ML -> Backend: return prediction
Backend -> DB: store results
@enduml
```
