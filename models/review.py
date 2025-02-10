#!/usr/bin/python3
"""
Review Module for HBNB project.

This module defines the Review class that inherits from BaseModel and Base.
It represents reviews made by users for places in the application, storing
the review text and maintaining relationships with Place and User models.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    """Review class for managing place reviews.
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Reviews.
        text (str): The review text content (1024 chars).
        place_id (str): The Place id that the review belongs to.
        user_id (str): The User id that created the review.

    Relationships:
        place: Relationship with the Place class (place.reviews)
        user: Relationship with the User class (user.reviews)
    """
    __tablename__ = "reviews"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
