import unittest
from src.karaoke_bar import *
from src.song import Song 
from src.guest import Guest
from src.room import Room

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        self.song = Song("Get Up Offa That Thing")
        self.room = Room("The Real Funky Room")
        self.guest = Guest("James Brown")

    def test_karaoke_can_check_guest_into_room(self):
        guest_check_in(self.room, self.guest)
        self.assertEqual(1, len(self.room.guests_and_songs["guest_list"]))

    def test_karaoke_can_add_song_to_playlist(self):
        add_to_playlist(self.room, self.song)
        self.assertEqual(1, len(self.room.guests_and_songs["playlist"]))
        self.assertEqual("Get Up Offa That Thing", self.room.guests_and_songs["playlist"][0].name)

    def test_karaoke_can_remove_guest(self):
        guest_check_in(self.room, self.guest)
        remove_guest(self.room, self.guest)
        self.assertEqual(0, len(self.room.guests_and_songs["guest_list"]))



   