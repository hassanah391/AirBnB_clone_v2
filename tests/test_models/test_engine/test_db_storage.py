#!/usr/bin/python3
'''
    Testing the file_storage module.
'''
import unittest
from models import storage
from models.user import User
from models.state import State
from models.engine.db_storage import DBStorage
from console import HBNBCommand
from os import getenv
import sys
from io import StringIO
import time
from models import storage

db = getenv("HBNB_TYPE_STORAGE")

@unittest.skipIf(db != 'db', "Testing DBstorage only")
class test_DBStorage(unittest.TestCase):
    '''
        Tests DB_Storage class
    '''
    @classmethod
    def setUpClass(cls):
        '''
            Initializes some classes for unit tests
        '''
        cls.dbstorage = DBStorage()
        cls.output = StringIO()
        sys.stdout = cls.output

    @classmethod
    def tearDownClass(cls):
        '''
            Deletes some variables
        '''
        del cls.dbstorage
        del cls.output

    def create(self):
        '''
            returns an instance of HBNBCommand class
        '''
        return HBNBCommand()

    def test_new(self):
        '''
            Tests database new
        '''
        new_obj = State(name="California")
        self.assertEqual(new_obj.name, "California")

    def test_dbstorage_user_attr(self):
        '''
            Tests User class attributes
        '''
        new = User(email="melissa@hbtn.com", password="hello")
        self.assertTrue(new.email, "melissa@hbtn.com")


    def test_dbstorage_new_save(self):
        '''
           Tests save()
        '''
        new_state = State(name="NewYork")
        storage.new(new_state)
        save_id = new_state.id
        result = storage.all("State")
        temp_list = []
        for k, v in result.items():
            temp_list.append(k.split('.')[1])
            obj = v
        self.assertTrue(save_id in temp_list)
        self.assertIsInstance(obj, State)

    def test_dbstorage_all(self):
        '''
            Tests all methods
        '''
        storage.reload()
        result = storage.all("")
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)
        new = User(email="adriel@hbtn.com", password="abc")
        console = self.create()
        console.onecmd("create State name=California")
        result = storage.all("State")
        self.assertTrue(len(result) > 0)

    def test_dbstorage_delete(self):
        '''
            Tests delete()
        '''
        new_user = User(email="haha@hehe.com", password="abc",
                        first_name="Adriel", last_name="Tolentino")
        storage.new(new_user)
        save_id = new_user.id
        key = "User.{}".format(save_id)
        self.assertIsInstance(new_user, User)
        storage.save()
        old_result = storage.all("User")
        del_user_obj = old_result[key]
        storage.delete(del_user_obj)
        new_result = storage.all("User")
        self.assertNotEqual(len(old_result), len(new_result))

    def test_dbstorage_check_method(self):
        '''
            Checks if the methods exists
        '''
        self.assertTrue(hasattr(self.dbstorage, "all"))
        self.assertTrue(hasattr(self.dbstorage, "__init__"))
        self.assertTrue(hasattr(self.dbstorage, "new"))
        self.assertTrue(hasattr(self.dbstorage, "save"))
        self.assertTrue(hasattr(self.dbstorage, "delete"))
        self.assertTrue(hasattr(self.dbstorage, "reload"))