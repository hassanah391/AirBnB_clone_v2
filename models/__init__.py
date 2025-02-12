#!/usr/bin/python3
'''comment'''
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

type_storage = getenv("HBNB_TYPE_STORAGE")

class_dict = {
            "BaseModel": BaseModel,
            "User": User, "State": State,
            "City": City,
            "Review": Review,
            "Amenity": Amenity,
            "Place": Place
            }

if (type_storage == "db"):
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
