from .BaseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.places = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        if not value:
            raise ValueError("name can't be empty")
        if len(value) > 50:
            raise ValueError("name must be less than 50 characters")
        self.__name = value


    def add_places(self, place):
        """Add a place to the amenity."""
        self.places.append(place)
