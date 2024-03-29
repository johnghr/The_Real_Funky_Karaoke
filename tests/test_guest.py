import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.guest = Guest("James Brown", 40.00, "Can't Stop")
    
    def test_guest_has_name(self):
        self.assertEqual("James Brown", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(40.00, self.guest.wallet)

    def test_guest_has_favorite_song(self):
        self.assertEqual("Can't Stop", self.guest.favorite_song)

       

    