#!/usr/bin/python3
"""

Module user has a class called User
 that inherits from BaseModel
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
