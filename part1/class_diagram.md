```mermaid
classDiagram
    class User {
        -id: UID
        -first name: str
        -last name: str
        -email: str
        -password: str
        -admin: bool
        -created at: datetime
        -updated at: datetime
        +register()
        +update_profile()
        +delete()
    }

    class Place {
        -id: UID
        -title: str
        -description: str
        -price: int
        -latitude: float
        -longitude: float
        -created at: datetime
        -updated at: datetime
        +create()
        +update()
        +delete()
        +list()
    }

    class Review {
        -id: UID
        -rating: int
        -comment: str
        -created at: datetime
        -updated at: datetime
        +create()
        +update()
        +delete()
        +list_by_place()
    }

    class Amenity {
        -id: UID
        -name: str
        -descritpion: str
        -created at: datetime
        -updated at: datetime
        +create()
        +update()
        +delete()
        +list()
    }

    %% --- Associations ---
    Place --* User : composition
    Place --o Amenity : aggregated
    Review --* Place : composition
