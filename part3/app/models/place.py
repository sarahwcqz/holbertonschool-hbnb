from .BaseModel import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities


    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if not value:
            raise ValueError("Title can't be empty")
        if len(value) > 100:
            raise ValueError("Title must be less than 100 charaters")
        self.__title = value


    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be an integer")
        if value < 0:
            raise ValueError("Price must be positive")
        self.__price = value


    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        self.__description = value

    @property
    def latitude(self):
        return self.__latitude
    
    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Latitude must be a float")
        if value < -90 or value > 90:
            raise ValueError("Latitude must be in range of -90.0 to 90.0")
        self.__latitude = value


    @property
    def longitude(self):
        return self.__longitude
    
    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Longitude must be a float")
        if value < -180 or value > 180:
            raise ValueError("Longitude must be in range of -180.0 to 180.0")
        self.__longitude = value


    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
