#!/usr/bin/python3
"""
A unittest for State class
"""
import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.state1 = State()
        cls.state1.name = "Pennsylvania"

    @classmethod
    def tearDownClass(cls):
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


    def test_attributes(self):
        self.assertTrue(hasattr(State, "name"))

if __name__ == "__main__":
    unittest.main()
