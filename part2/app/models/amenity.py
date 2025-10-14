from .BaseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        if len(name) < 50:
            self.name = name
        else:
            raise ValueError("name must be less than 50 characters")
        self.place = []
