from classes import *
from text_parser import *

room1 = Room('room 1', 'This is the basic starting room, any bugs?')
room2 = Room('room 2', 'It\'s real dark in here, got any light?')
room1.add_exit('north', room2)
room2.add_exit('south', room1)
room1.add_item('a torch', 'shining brightly, maybe lights up something?', 'A torch on a wall', room2, 'The torch lights up the whole room, you can see the exit!')
player = Player(room1)


def test_inventory():
    player.get_item('a torch')
    assert len(player.inventory) == 1
    assert player.inventory['a torch']
    assert 'wall' in  player.inventory['a torch'].view 
    assert 'shining brightly' in player.inventory['a torch'].description

def test_move():
    assert player.room == room1
    player.move_rooms('north')
    assert player.room == room2
    player.move_rooms('south')
    assert player.room == room1
