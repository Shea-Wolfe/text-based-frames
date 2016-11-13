
from classes import *

room1 = Room('Room 1', 'This is the basic starting room, any bugs?')
room2 = Room('Room 2', 'It\'s real dark in here, got any light?')
room1.add_exit('North', room2)
room2.add_exit('South', room1)
room1.add_item('A torch', 'shining brightly, maybe lights up something?', room2)
player = Player(room1)

while True:
    entry = input('==> ')
    #for basic testing
    if entry.lower() == 'move':
        player.move_rooms('North')
    else:
        print('nope')
    
