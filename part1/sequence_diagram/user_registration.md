```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: POST: user registration
API->>BusinessLogic: Validate format of [-first name, -last name, -email, -password]
BusinessLogic->>API: Validate
API->>BusinessLogic: Check if email exists
BusinessLogic->>Database: Checks if email exists
Database-->>BusinessLogic: Email doesn't exists
BusinessLogic->>Database: Save Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Response
API-->>User: Return Success (201)
