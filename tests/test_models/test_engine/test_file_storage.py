#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''testing file storage'''

    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.storage = FileStorage()
        cls.rev1 = Review()
        cls.rev1.place_id = "Raleigh"
        cls.rev1.user_id = "Greg"
        cls.rev1.text = "Grade A"

    def setUp(self):
        """Set up for each test"""
        FileStorage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except:
            pass

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests"""
        try:
            os.remove("file.json")
        except:
            pass
        del cls.rev1
        del cls.storage

    def test_all(self):
        """Tests method: all (returns dictionary <class>.<id> : <obj instance>)"""
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(len(obj_dict), 0)
        
        # Test with new object
        new_state = State()
        new_state.name = "Test State"
        storage.new(new_state)
        self.assertEqual(len(storage.all()), 1)
        self.assertIn(f"State.{new_state.id}", storage.all())

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        u = BaseModel
        u.id = 999999
        u.name = "Hassan"
        m_storage.new(u)
        key = u.__class__.__name__ + "." + str(u.id)
        #print(instances_dic[key])
        self.assertIsNotNone(instances_dic[key])

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)