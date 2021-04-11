from src.room import Room
from src.guest import Guest
from src.song import Song

guest = Guest("James")
room = Room("The Real Funky Room")
song = Song("Get Up Offa That Thing")

def guest_check_in(room, guest):
    if len(room.guests_and_songs["guest_list"]) < 3:
        room.guests_and_songs["guest_list"].append(guest)
    else:
        return "Sorry cool cats, this Karaoke ain't funky enough for four of you!"

def add_to_playlist(room, song):
    room.guests_and_songs["playlist"].append(song)

def remove_guest(room, guest):
    room.guests_and_songs["guest_list"].remove(guest)
   


