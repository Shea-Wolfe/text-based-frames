from sys import argv
import pickle

from classes import *
from text_parser import *

filename = argv[1]
with open(filename, 'rb') as f:
    rooms = pickle.load(f)
    try:
        player = pickle.load(f)
    except:
        for room in rooms:
            if room.starting_room:
                player = Player(room)
                break
            else:
                pass

while True:
    parse_text(player, player.room, rooms)

