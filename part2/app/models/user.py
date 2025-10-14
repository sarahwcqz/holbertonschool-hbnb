from .BaseModel import BaseModel
class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        if len(first_name) < 51:
            self.first_name = first_name
        else:
            raise ValueError("first name must be less than 50 characters")
        if len(last_name) < 51:
            self.last_name = last_name
        else:
            raise ValueError("last name must be less than 50 characters")
        self.email = email
        self.is_admin = is_admin
        self.places = []

    def add_place(self, place):
        """Creating a new place for the user"""
        self.places.append(place)
