# UML Diagrams

Диаграммы рендерятся из PlantUML локально в CI (Java + Graphviz).

## 1) System context

```plantuml
@startuml
skinparam shadowing false
skinparam monochrome true

actor User
rectangle "Frontend\n(Angular)" as FE
rectangle "Backend API\n(Spring Boot)" as BE
database "PostgreSQL" as DB
node "Keycloak" as KC
queue "Kafka" as KFK
cloud "ML Service\n(Python)" as ML
storage "S3 Storage" as S3
component "PC Agent\n(.NET)" as AG

User --> FE
FE --> BE
AG --> BE : Upload metrics ZIP
BE --> DB
BE --> KC
BE --> S3
BE --> KFK
KFK --> ML
ML --> BE : predictions
@enduml
```

## 2) Component diagram (high level)

```plantuml
@startuml
skinparam shadowing false
skinparam monochrome true

package "Frontend" {
  [UI] as UI
  [API Client] as APIC
  UI --> APIC
}

package "Backend" {
  [REST API] as REST
  [Auth/JWT] as AUTH
  [Recommendation Engine] as REC
  [Processing] as PROC
  REST --> AUTH
  REST --> REC
  REST --> PROC
}

package "Infrastructure" {
  database "PostgreSQL" as DB
  node "Keycloak" as KC
  queue "Kafka" as KFK
  storage "S3" as S3
}

APIC --> REST
AUTH --> KC
REST --> DB
PROC --> KFK
PROC --> S3
KFK --> [ML Service]
[ML Service] --> REST
@enduml
```

## 3) Sequence: upload test

```plantuml
@startuml
skinparam shadowing false
skinparam monochrome true

actor Agent
participant Backend
database DB
queue Kafka
participant ML

Agent -> Backend : POST /api/upload (zip)
Backend -> DB : create test record
Backend -> Kafka : publish task
Kafka -> ML : consume task
ML -> Backend : prediction + insights
Backend -> DB : store results
@enduml
```

## 4) Class: AnalyzeResponse (draft)

```plantuml
@startuml
skinparam shadowing false
skinparam monochrome true

class AnalyzeResponseDto {
  +String scenario
  +double score
  +String summary
  +List<Recommendation> recommendations
}

class Recommendation {
  +String title
  +String details
  +String severity
  +List<Action> actions
}

class Action {
  +String type
  +String payload
}

AnalyzeResponseDto "1" o-- "many" Recommendation
Recommendation "1" o-- "many" Action
@enduml
```
