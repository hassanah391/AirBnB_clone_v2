#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''testing file storage'''

    @classmethod
    def setUpClass(cls):
        cls.rev1.place_id = "Raleigh"
        cls.rev1.user_id = "Greg"
        cls.rev1.text = "Grade A"

    @classmethod
    def teardown(cls):
        del cls.rev1

    def teardown(self):
        try:
            os.remove("file.json")
        except:
            pass

   
    def test_all(self):
        """
        Tests method: all (returns dictionary <class>.<id> : <obj instance>)
        """
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

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