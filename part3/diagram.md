```mermaid
erDiagram
    
    User {
        string id PK
        string first_name
        string last_name
        string email
        boolean is_admin
    }

    Place {
        string id PK
        string title
        string description
        float price
        float latitude
        float longitude
        string owner_id FK
    }

    Reviews {
        string id PK
        string text
        string rating
        string user_id FK
        string place_id FK
    }

    Amenity {
        string id PK
        string name
    }

    Place_amenity {
        string place_id
        string amenity_id
    }

    User ||--o{ Place : owns
    User ||--o{ Reviews : writes
    Place ||--o{ Reviews : has
    Place ||--o{ Place_amenity : has
    Amenity ||--o{ Place_amenity : belongs to