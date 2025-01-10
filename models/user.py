#!/usr/bin/python3
"""

Module user has a class called User
 that inherits from BaseModel
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String

class User(BaseModel, Base):
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
