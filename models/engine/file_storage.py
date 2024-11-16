#!/usr/bin/python3
'''File Storage'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel}

    def all(self):
        '''Return dictionary of <class>.<id> : object instance'''
        return self.__objects

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
        '''If JSON file exists, convert object dictionaries back to instances'''
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
