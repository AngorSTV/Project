# UML Diagrams

Эта страница содержит основные UML-диаграммы проекта в формате Mermaid.

## 1) System context

<div class="mermaid">
flowchart LR
  U[User] --> FE[Frontend (Angular)]
  FE --> BE[Backend (Spring Boot)]
  BE --> DB[(PostgreSQL)]
  BE --> KC[Keycloak]
  BE --> S3[(S3 Storage)]
  BE --> KFK[Kafka]
  AG[PC Agent (.NET)] --> BE
  KFK --> ML[ML Service]
</div>

## 2) Component diagram (high level)

<div class="mermaid">
flowchart TB
  subgraph FE[Frontend]
    UI[UI]
    APIc[API Client]
  end

  subgraph BE[Backend]
    REST[REST API]
    AUTH[Auth/JWT]
    REC[Recommendation Engine]
    PROC[Processing]
  end

  subgraph INF[Infrastructure]
    KC[Keycloak]
    DB[(PostgreSQL)]
    KFK[Kafka]
    S3[(S3)]
    MON[Monitoring]
  end

  AG[Agent] --> REST
  UI --> APIc --> REST
  REST --> AUTH --> KC
  REST --> DB
  PROC --> KFK
  PROC --> S3
  KFK --> ML[ML Service]
  ML --> REST
  MON --- REST
  MON --- KFK
  MON --- DB
</div>

## 3) Sequence: upload test

<div class="mermaid">
sequenceDiagram
  autonumber
  participant A as Agent
  participant B as Backend
  participant D as DB
  participant K as Kafka
  participant M as ML

  A->>B: POST /api/upload (zip)
  B->>D: create test record
  B->>K: publish task
  K->>M: consume task
  M->>B: prediction + insights
  B->>D: store results
</div>

## 4) Class: AnalyzeResponse (draft)

<div class="mermaid">
classDiagram
  class AnalyzeResponseDto {
    +String scenario
    +double score
    +String summary
    +List~Recommendation~ recommendations
  }

  class Recommendation {
    +String title
    +String details
    +String severity
    +List~Action~ actions
  }

  class Action {
    +String type
    +String payload
  }

  AnalyzeResponseDto "1" o-- "many" Recommendation
  Recommendation "1" o-- "many" Action
</div>
