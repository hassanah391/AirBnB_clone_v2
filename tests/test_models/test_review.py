#!/usr/bin/python3
"""
A unittest for Review class
"""
import unittest
import os
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.review1 = Review()
        cls.review1.text = "Hassan"

    @classmethod
    def tearDownClass(cls):
        del cls.review1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


    def test_attributes(self):
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))
    

if __name__ == "__main__":
    unittest.main()
