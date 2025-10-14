from .BaseModel import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        if 0 < rating < 6:
            self.rating = rating
        else:
            raise ValueError("rating must be from 1 to 5")
        self.place = place
        self.user = user
