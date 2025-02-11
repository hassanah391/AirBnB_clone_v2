#!/usr/bin/python3
"""

Module amenity has a class called Amenity that inherits
from Basemodel class
"""
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """A class that represent the amenity ways in Airbnb
    Public class attributes:
        name: string - empty string
    """
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary="place_amenity",
            back_populates="amenities"
            )
    else:
        name = ""