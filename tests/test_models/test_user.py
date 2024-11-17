#!/usr/bin/python3
"""
A unittest for User class
"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user1 = User()
        cls.user1.first_name = "Hassan"
        cls.user1.last_name = "Ahmed"

    @classmethod
    def tearDownClass(cls):
        del cls.user1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


    def test_attributes(self):
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    

if __name__ == "__main__":
    unittest.main()
