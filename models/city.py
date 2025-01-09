#!/usr/bin/python3
"""

Module city has a class called City that inherits from
Basemodel class
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.state import State
from os import getenv

class City(BaseModel, Base):
    """A class that represents a city in Airbnb
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    __tablename__ = "cities"
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        # state = relationship("State", back_populates="cities")
    
    else:
        state_id = ""
        name = ""
