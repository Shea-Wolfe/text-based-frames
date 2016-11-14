
from classes import *
from text_parser import *

room1 = Room('Room 1', 'This is the basic starting room, any bugs?')
room2 = Room('Room 2', 'It\'s real dark in here, got any light?')
room1.add_exit('north', room2)
room2.add_exit('south', room1)
room1.add_item('A torch', 'shining brightly, maybe lights up something?', 'A torch on a wall', room2, 'The torch lights up the whole room, you can see the exit!')
player = Player(room1)

while True:
    parse_text(player, player.room)
    
