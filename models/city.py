#!/usr/bin/python3
"""

Module city has a class called City that inherits from
Basemodel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class that represents a city in Airbnb
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
