from .BaseModel import BaseModel
from app.extensions import db
from sqlalchemy.orm import validates


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False)
    
    @validates('name')
    def validate_name(self, key, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        if not value:
            raise ValueError("name can't be empty")
        if len(value) > 50:
            raise ValueError("name must be less than 50 characters")
        return value
