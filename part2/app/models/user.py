from .BaseModel import BaseModel
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []


    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Firstname must be a string")
        if not value:
            raise ValueError("Firstname can't be empty")
        if len(value) > 50:
            raise ValueError("Firstname must be less than 50 characters")
        
        self.__first_name = value


    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Lastname must be a string")
        if not value:
            raise ValueError("Lastname can't be empty")
        
        if len(value) > 50:
            raise ValueError("Lastname must be less than 50 characters")
        
        self.__last_name = value


    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        if not value:
            raise ValueError("email can't be empty")
        if not re.fullmatch(regex, value):
            raise ValueError("email not valid format")
        self.__email = value

    
    @property
    def is_admin(self):
        return self.__is_admin
    
    @is_admin.setter
    def is_admin(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_admin must be a boolean")
        self.__is_admin = value


    def add_place(self, place):
        """Creating a new place for the user"""
        self.places.append(place)