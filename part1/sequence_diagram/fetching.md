```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Fetching List of Places
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: List of Criteria
Database-->>BusinessLogic: Return List of Place w/ Matching Criterias
BusinessLogic-->>API: Return Response
API-->>User: Display List of Matching Places
