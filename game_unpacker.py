from sys import argv
import pickle

from classes import *
from text_parser import *

filename = argv[1] #We take a save game or new game file from the command line
with open(filename, 'rb') as f:
    try: #First we assume we've been fed a game and pull the player and rooms out of it
        game = pickle.load(f)
        rooms = game.rooms
        player = game.player
        print('{} welcome back!'.format(player.name))
    except: #If we fail we've been fed a rooms file, so we get a player name and set up the game
        rooms = game.rooms 
        for room in rooms:
            if room.starting_room:
                name = input('Please enter your name\n> ')
                player = Player(room, name)
                break
            else:
                pass
print(player.room.description)
while True: #Just a simple loop, the quit command writes a save file then returns false, hence why we check a ret each time
    ret = parse_text(player, player.room, rooms)
    if ret == False:
        break
