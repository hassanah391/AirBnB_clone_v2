import unittest
from console import HBNBCommand
from models import storage, State, Place

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        storage._FileStorage__objects = {}  # Clear storage before each test

    def test_create_with_parameters(self):
        self.console.onecmd('create State name="California"')
        self.console.onecmd('create State name="Arizona"')
        self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')

        states = storage.all(State)
        places = storage.all(Place)

        self.assertEqual(len(states), 2)
        self.assertEqual(len(places), 1)

        state_names = [state.name for state in states.values()]
        self.assertIn("California", state_names)
        self.assertIn("Arizona", state_names)

        place = list(places.values())[0]
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