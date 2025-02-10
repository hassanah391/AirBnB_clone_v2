#!/usr/bin/python3
"""
Module for User class.

This module defines the User class that inherits from BaseModel and Base.
The User class represents a user in the HBNB application with attributes
like email, password, name and relationships to places and reviews.

Classes:
    User: Represents a user in the application
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place

class User(BaseModel, Base):
    """User class for managing user information in HBNB.
    
    Attributes:
        email (str): User's email address
        password (str): User's password
        first_name (str): User's first name
        last_name (str): User's last name
        places (relationship): Relationship with Place objects
        reviews (relationship): Relationship with Review objects
    """
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", back_populates="user", cascade="all, delete")
        reviews = relationship("Review", back_populates="user", cascade="all, delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
