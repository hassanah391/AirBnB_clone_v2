#!/usr/bin/python3
'''File Storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models import class_dict

class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        '''
        Returns a dictionary of all objects or objects of a specified class.

        If no class (`cls`) is provided, returns all objects.
        If a class (`cls`) is provided, returns only objects of that class.

        Args:
            cls (class, optional): The class to filter objects by. Defaults to None.
        
        Returns:
            dict: A dictionary of objects, filtered by class if `cls` is provided.
        '''
        if cls is None:
            return self.__objects
        else:
            objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    objects[key] = obj
            return objects

    def new(self, obj):
        '''Add new obj to existing dictionary of instances'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        '''Save obj dictionaries to json file'''
        my_dict = {}

        for key, obj in self.__objects.items():
            '''if type(obj) is dict:
            my_dict[key] = obj
            else:'''
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        '''If JSON file exists, convert obj dictionaries back to instances'''
        try:
            with open(self.__file_path, 'r') as f:
                try:
                    new_obj = json.load(f)
                except json.JSONDecodeError:
                    return
            for key, val in new_obj.items():
                try:
                    obj = self.class_dict[val['__class__']](**val)
                    self.__objects[key] = obj
                except KeyError:
                    print(f"Class {val['__class__']} is not recognized.")
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        "deletes obj from __objects if it's inside "
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
            else:
                pass
        else:
            pass

    def close(self):
        """Call the reload method to deserialize the JSON file to objects.
        """
        self.reload()