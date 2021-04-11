import unittest
from src.karaoke_bar import *
from src.song import Song 
from src.guest import Guest
from src.room import Room

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        self.song = Song("Get Up Offa That Thing")
        self.room = Room("The Real Funky Room")
        self.guest_1 = Guest("James Brown", 50.00)
        self.guest_2 = Guest("Bootsy Collins", 40.00)
        self.guest_3 = Guest("Stevie Wonder", 60.00)
        self.guest_4 = Guest("George Clinton", 70.00)

    def test_karaoke_can_check_guest_into_room(self):
        guest_check_in(self.room, self.guest_1)
        guest_check_in(self.room, self.guest_2)
        guest_check_in(self.room, self.guest_3)
        self.assertEqual(3, len(self.room.guests_and_songs["guest_list"]))

    def test_karaoke_can_add_song_to_playlist(self):
        add_to_playlist(self.room, self.song)
        self.assertEqual(1, len(self.room.guests_and_songs["playlist"]))
        self.assertEqual("Get Up Offa That Thing", self.room.guests_and_songs["playlist"][0].name)

    def test_karaoke_can_remove_guest(self):
        guest_check_in(self.room, self.guest_1)
        remove_guest(self.room, self.guest_1)
        self.assertEqual(0, len(self.room.guests_and_songs["guest_list"]))

    def test_karaoke_bar_has_capacity_limit(self):
        guest_check_in(self.room, self.guest_1)
        guest_check_in(self.room, self.guest_2)
        guest_check_in(self.room, self.guest_3)
        self.assertEqual(3, len(self.room.guests_and_songs["guest_list"]))
        self.assertEqual("Sorry cool cats, this Karaoke ain't funky enough for four!", guest_check_in(self.room, self.guest_4))

    def test_karaoke_can_charge_entry_fee(self):
        charge_entry_fee(self.guest_1)
        self.assertEqual(45.00, self.guest_1.wallet)


   