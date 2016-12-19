from classes import *
from text_parser import *
from generation import *
import os

room1 = Room('room 1', 'This is the basic starting room, any bugs?', 'The game is complete.  Good job')
room2 = Room('room 2', 'It\'s real dark in here, got any light?', 'The room is now well lit, showing an exit to the east')
room3 = Room('room 3', 'This is the bonus room')
room1.add_exit('north', room2)
room2.add_exit('south', room1)
room2.add_solved_exit('east', room3)
room1.add_item('a torch', 'shining brightly, maybe lights up something?', 'A torch on a wall', room2, 'The torch lights up the whole room, you can see the exit!')
player = Player(room1)
rooms = {'room 1':room1, 'room 2':room2, 'room 3':room3}
room3.add_item('gems', 'shiny, twinkly', 'There are gems on the ground!')
items = {'a torch': room1.items['a torch'], 'gems': room3.items['gems']}

def test_room_items():
    assert 'a torch' in room1.items
    assert 'gems' in room3.items
    assert 'gems' in items

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
    assert 'east' not in player.room.exits
    player.use_item('a torch')
    assert 'well lit' in player.room.description
    assert 'a torch' not in player.inventory
    assert 'east' in player.room.exits
    player.move_rooms('east')
    assert player.room == room3
    
def test_add_exit():
    exit1 = 'northeast'
    exit3 = 'southwest'
    generate_exit(room1, exit1, room3, exit3)
    player.move_rooms('southwest')
    assert player.room == room1
    assert 'northeast' in player.room.exits

def test_text_parser():
    parse_text(player, player.room, rooms, 'go north')
    assert player.room == room2
    parse_text(player, player.room, rooms, 'go east')
    assert player.room == room3
    parse_text(player, player.room, rooms, 'get gems')
    assert 'gems' in player.inventory

def test_checks():
    assert room_check('room5',rooms) == None
    assert item_check('a thingy', items) == None
    assert room_check('room 1', rooms) == room1
    assert item_check('gems', items) == player.inventory['gems']

def test_generate_solution():
    generate_solution('gems', 'room 1',items,rooms, 'it slices, it dices!')
    parse_text(player, player.room, rooms, 'go southwest')
    parse_text(player, player.room, rooms, 'use gems')
    assert 'gems' not in player.inventory

def test_class_creation():
    room4 = Room('room 4', 'this is the test room 4')
    item1 = Item('test item', 'This is used to test item creation', 'Wow it is a thing!')
    assert 'test' in room4.description
    assert room4.name == 'room 4'
    assert item1.name == 'test item'
    assert 'test' in item1.description
    assert 'thing' in item1.view

def test_save():
    parse_text(player, player.room, rooms, 'quit', 'test_save')
    assert os.path.exists('test_save')

def test_load():
    with open('test_save', 'rb') as f:
        rooms = pickle.load(f)
        player = pickle.load(f)
    assert player.room.name == room1.name 
    assert 'room 3' in rooms
    try:
        os.remove('test_save')
        assert os.path.exists('test_save') == False
    except:
        pass
