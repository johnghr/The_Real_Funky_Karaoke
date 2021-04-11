import pdb
from src.room import Room
from src.guest import Guest
from src.song import Song

guest = Guest("James")
room = Room("The Real Funky Room")
song = Song("Get Up Offa That Thing")

def guest_check_in(room, guest):
    room.guests_and_songs["guest_list"].append(guest)

def add_to_playlist(room, song):
    
    pdb.set_trace()
    room.guests_and_songs["playlist"].append(song)
   


