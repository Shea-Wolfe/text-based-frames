from sys import argv
import pickle

from classes import *
from text_parser import *

filename = argv[1]
with open(filename, 'rb') as f:
    try:
        game = pickle.load(f)
        rooms = game.rooms
        player = game.player
        print('{} welcome back!'.format(player.name))
    except:
        rooms = game.rooms
        for room in rooms:
            if room.starting_room:
                name = input('Please enter your name')
                player = Player(room, name)
                break
            else:
                pass
print(player.room.description)
while True:
    ret = parse_text(player, player.room, rooms)
    if ret == False:
        break
