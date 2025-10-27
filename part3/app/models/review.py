from .BaseModel import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id


    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            raise TypeError("Text must be a string")
        if not value:
            raise ValueError("Text can't be empty string")
        self.__text = value


    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise TypeError("Rating must be an integer")
        if value < 1 or value > 5:
            raise ValueError("Rating must be from 1 to 5")
        self.__rating = value
        