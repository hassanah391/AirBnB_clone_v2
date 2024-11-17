#!/usr/bin/python3
"""

Module state has a class called State that inherits from
Basemodel class 
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A class that represents a state in Airbnb
    Public class attributes:
        name: string - empty string
    """
    name = ""
