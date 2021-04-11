def guest_check_in(room, guest):
        if len(room.guests_and_songs["guest_list"]) < 3:
            room.guests_and_songs["guest_list"].append(guest)
        else:
            return "Sorry cool cats, this Karaoke ain't funky enough for four!"

def add_to_playlist(room, song):
    room.guests_and_songs["playlist"].append(song)

def add_multiple_songs_to_playlist(room, songs):
    for song in songs:
        room.guests_and_songs["playlist"].append(song)

def remove_guest(room, guest):
    room.guests_and_songs["guest_list"].remove(guest)

def charge_entry_fee(guest):
    guest.wallet -= 5.00

def check_for_favorite_song(room, guest):
    if room.guests_and_songs["playlist"][0].name == guest.favorite_song:
            return "Damn thats Funky!"
   
def group_booking(room, group):
    for guest in group:
        if len(group) > 4:
            return "Sorry cool cats, this Karaoke ain't funky enough for five!"
        else:
            room.guests_and_songs["guest_list"].append(guest)
            
        
            
                
    


