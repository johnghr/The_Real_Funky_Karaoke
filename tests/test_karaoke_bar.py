import unittest
from src.karaoke_bar import *
from src.song import Song 
from src.guest import Guest
from src.room import Room

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Get Up Offa That Thing")
        self.song_2 = Song("Can't Stop")
        self.room = Room("The Real Funky Room")
        self.guest_1 = Guest("James Brown", 50.00, "Can't Stop")
        self.guest_2 = Guest("Bootsy Collins", 40.00, "All around the world")
        self.guest_3 = Guest("Stevie Wonder", 60.00, "By the way")
        self.guest_4 = Guest("George Clinton", 70.00, "Give it away")
        self.guest_5 = Guest("Robert 'Kool' Bell", 80.00, "Aeroplane")
        self.group = []
        self.group.append(self.guest_1) 
        self.group.append(self.guest_2) 
        self.group.append(self.guest_3)
        self.group.append(self.guest_4)
        self.group_2 = []
        self.group_2.append(self.guest_1) 
        self.group_2.append(self.guest_2) 
        self.group_2.append(self.guest_3)
        self.group_2.append(self.guest_4)
        self.group_2.append(self.guest_5)
        self.songs = []
        self.songs.append(self.song_1)
        self.songs.append(self.song_2)


    def test_karaoke_can_check_guest_into_room(self):
        guest_check_in(self.room, self.guest_1)
        self.assertEqual(1, len(self.room.guests_and_songs["guest_list"]))

    def test_karaoke_can_add_song_to_playlist(self):
        add_to_playlist(self.room, self.song_1)
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

    def test_guests_cheer_their_favorite_song(self):
        guest_check_in(self.room, self.guest_1)
        add_to_playlist(self.room, self.song_2)
        self.assertEqual("Damn thats Funky!", check_for_favorite_song(self.room, self.guest_1))

    def test_group_booking(self):
        group_booking(self.room, self.group)
        self.assertEqual(4, len(self.room.guests_and_songs["guest_list"]))

    def test_group_booking_has_capacity(self):
        self.assertEqual("Sorry cool cats, this Karaoke ain't funky enough for five!", group_booking(self.room, self.group_2))

    def test_add_multiple_songs_to_playlist(self):
        add_multiple_songs_to_playlist(self.room, self.songs)
        self.assertEqual(2, len(self.room.guests_and_songs["playlist"]))
    
   

        
    

        

   