import unittest
from src.room import *

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.room = Room("The Real Funky Room")

    def test_room_has_a_name(self):
        self.assertEqual("The Real Funky Room", self.room.name)