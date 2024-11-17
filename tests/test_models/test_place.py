#!/usr/bin/python3
"""
A unittest for Place class
"""
import unittest
import os
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.place1 = Place()
        cls.place1.name = "suite"
        cls.place1.max_guest = 10
        cls.place1.price_by_night = 5000

    @classmethod
    def tearDownClass(cls):
        del cls.place1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


    def test_attributes(self):
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

if __name__ == "__main__":
    unittest.main()
