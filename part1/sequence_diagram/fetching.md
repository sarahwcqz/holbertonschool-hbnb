```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: GET : Fetching List of Places
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: List of Criteria
Database-->>BusinessLogic: Return List of Place w/ Matching Criterias
BusinessLogic-->>API: Return Response
API-->>User: 200 : Display List of Matching Places / 404 : Not found
