```mermaid
classDiagram
    class PresentationLayer {
        <<Interface>>
        +UserService
        +PlaceService
        +ReviewService
        +AmenityService
    }

    class BusinessLogicLayer {
        <<Logic>>
        +User
        +Place
        +Review
        +Amenity
    }

    class PersistenceLayer {
        <<Database>>
        +User's datas
        +Place's datas
        +Review's datas
        +Amenity's datas
    }

    PresentationLayer --> BusinessLogicLayer : Access
    BusinessLogicLayer --> PersistenceLayer : Database Operations
