#!/usr/bin/python3
"""

Module user has a class called User
 that inherits from BaseModel
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place

class User(BaseModel, Base):
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", back_populates="user", cascade="all, delete, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
