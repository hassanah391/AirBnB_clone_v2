#!/usr/bin/python3
"""
Place Module for HBNB project.

This module defines the Place class that inherits from BaseModel and Base.
It represents accommodation places in the application with support for both
database and file storage. Places have relationships with City (location),
User (owner), and Review (feedback) models.

The class handles both SQLAlchemy database storage and File storage modes,
automatically detecting and using the appropriate storage method based on
configuration.
"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
import models

class Place(BaseModel, Base):
    """Place class for managing accommodation listings.
    
    Attributes for both storage types:
        city_id (str): City ID where place is located (foreign key cities.id)
        user_id (str): User ID who owns the place (foreign key users.id)
        name (str): Name of the place
        description (str): Description of the place
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum number of guests
        price_by_night (int): Price per night
        latitude (float): Geographical latitude
        longitude (float): Geographical longitude
        
    DB Storage specific:
        user: Relationship to User (owner)
        cities: Relationship to City (location)
        reviews: Relationship to Review (cascade delete)
        
    File Storage specific:
        reviews (property): Returns linked Review instances
        amenity_ids (list): List of linked Amenity IDs
    """
    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place", cascade="all, delete")

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

    @property
    def reviews(self):
        """Returns the list of Review instances with place_id = current Place.id"""
        return [review for review in models.storage.all(Review).values()
                if review.place_id == self.id]
