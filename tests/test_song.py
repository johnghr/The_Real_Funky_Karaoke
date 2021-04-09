import unittest
from src.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Get Up Offa That Thing")

    def test_song_has_name(self):
        self.assertEqual("Get Up Offa That Thing", self.song.name)

