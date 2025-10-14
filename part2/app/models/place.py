from .BaseModel import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        if len(title) < 101:
            self.title = title
        else:
            raise ValueError("Title must be less than 100 charaters")
        self.description = description
        if price >= 0:
            self.price = price
        else:
            raise ValueError("Price must be positive")
        if -90.0 <latitude < 90.0:
            self.latitude = latitude
        else:
            raise ValueError("Latitude must be in range of -90.0 to 90.0")
        if -180 <longitude< 180:
            self.longitude = longitude
        else:
            raise ValueError("Longitude must be in range of -180 to 180")
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)