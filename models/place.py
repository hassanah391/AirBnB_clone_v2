#!/usr/bin/python3
"""

Module place has a class called Place that inherits from
Basemodel class
"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, INTEGER, String, ForeignKey, FLOAT
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """A class that represents a place in Airbnb
    Public class attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - empty list:
        it will be the list of Amenity.id later
    """
    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(INTEGER, nullable=False, default=0)
        number_bathrooms = Column(INTEGER, nullable=False, default=0)
        max_guest = Column(INTEGER, nullable=False, default=0)
        price_by_night = Column(INTEGER, nullable=False, default=0)
        latitude = Column(FLOAT, nullable=True)
        longitude = Column(FLOAT, nullable=True)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
