from classes import *
from text_parser import *
from generation import *

room1 = Room('room 1', 'This is the basic starting room, any bugs?', 'The game is complete.  Good job', 'You find a slot for the coin and insert it.  You have won the game!')
room2 = Room('room 2', 'It\'s real dark in here, got any light?', 'The room is now well lit, showing an exit to the east', 'The torch illuminates the room, revealing an exit to the east!')
room3 = Room('room 3', 'This is the bonus room')
room1.add_exit('north', room2)
room2.add_exit('south', room1)
room2.add_solved_exit('east', room3)
room1.add_item('a torch', 'shining brightly, maybe lights up something?', 'A torch on a wall', room2, 'The torch lights up the whole room, you can see the exit!')
player = Player(room1)
rooms = {'room 1':room1, 'room 2':room2, 'room 3':room3}
room3.add_item('gold', 'shiny, twinkly', 'There is gold on the ground!', success='You find a small slot and put the gold in. You win!')
items = {'a torch': room1.items['a torch'], 'gold': room3.items['gold']}

def test_room_items():
    assert 'a torch' in room1.items
    assert 'gold' in room3.items
    assert 'gold' in items

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

def test_use():
    player.move_rooms('north')
    player.move_rooms('east')
    assert player.room == room2
    player.use_item('a torch')
    assert 'well lit' in player.room.description
    assert 'a torch' not in player.inventory
    player.move_rooms('east')
    assert player.room == room3
    
def test_add_exit():
    exit1 = 'northeast'
    exit3 = 'southwest'
    generate_exit(room1, exit1, room3, exit3)
    player.move_rooms('southwest')
    assert player.room == room1
    player.move_rooms('northeast')

