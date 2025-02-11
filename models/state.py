#!/usr/bin/python3
"""
Module state has a class called State that inherits from
Basemodel class
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """A class that represents a state in Airbnb"""
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            cascade="all, delete-orphan",
            back_populates="state"
        )
    else:
        name = ""

        @property
        def cities(self):
            '''Returns the list of City instances with
            state_id equals to current State.id'''
            from models.city import City
            list_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
