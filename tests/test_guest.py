import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.guest = Guest("James Brown")
    
    def test_guest_has_name(self):
        self.assertEqual("James Brown", self.guest.name)

       

    