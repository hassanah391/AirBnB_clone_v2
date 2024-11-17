#!/usr/bin/python3
"""
A unittest for City class
"""
import unittest
import os
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.city1 = City()
        cls.city1.name = "philadelphia"

    @classmethod
    def tearDownClass(cls):
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


    def test_attributes(self):
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "state_id"))
    

if __name__ == "__main__":
    unittest.main()
