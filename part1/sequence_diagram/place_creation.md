```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: GET : the list of amenities
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: Retrieve list of amenities
Database-->>BusinessLogic: return list of amenities
BusinessLogic-->>API: Return response
API-->>User: 200: Display list of amenities

User->>API: POST : create an new place
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: Save Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Response
API-->>User: Return Success(201)
