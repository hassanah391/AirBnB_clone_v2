#!/usr/bin/python3
"""

Module amenity has a class called Amenity that inherits from
Basemodel class 
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class that represent the amenity ways in Airbnb
    Public class attributes:
        name: string - empty string
    """
    name = ""
