import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage, State, Place

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        storage._FileStorage__objects = {}  # Clear storage before each test

    def test_create_with_parameters(self):
        """Test create command with parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California"')
            id1 = f.getvalue().strip()
        
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="Arizona"')
            id2 = f.getvalue().strip()
        
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            id3 = f.getvalue().strip()
        
        # Verify State objects
        key1 = f"State.{id1}"
        key2 = f"State.{id2}"
        self.assertEqual(storage.all()[key1].name, "California")
        self.assertEqual(storage.all()[key2].name, "Arizona")
        
        # Verify Place object
        key3 = f"Place.{id3}"
        place = storage.all()[key3]
        self.assertEqual(place.city_id, "0001")
        self.assertEqual(place.user_id, "0001")
        self.assertEqual(place.name, "My little house")
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 300)
        self.assertEqual(place.latitude, 37.773972)
        self.assertEqual(place.longitude, -122.431297)

if __name__ == "__main__":
    unittest.main()