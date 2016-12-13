import pickle
from classes import *

rooms = {}
items = {}

def print_rooms(existing_rooms):
    '''A helper function to print all rooms in a group of rooms'''
    for room in existing_rooms:
        print(room)

def print_items(existing_items):
    '''A helper function to print all items in a group of items'''
    for item in existing_items:
        print(item)

def room_check(room, rooms=rooms):
    '''Checks to see if a room is in your rooms dictionary, if so returns the room, else returns None'''
    if room in rooms:
        return rooms[room]
    else:
        return None

def item_check(item, items=items):
    '''Checks to see if an item is in your items dictionary, if so returns the item, else returns None'''
    if item in items:
        return items[item]
    else:
        return None

def generation_loop():
    '''The loop that contains all the game creation functions.  ends by writing a game file.'''
    while True:
        text = input('please (C)reate, (E)dit, (V)iew, or  (D)one \n> ').lower()
        if text == 'c' or text == 'create':
            while True:
                creation_text = input('Would you like to make\nA (R)oom\nAdd an (I)tem to an existing room\nAdd a (S)olution to a room/item combo\nAn (E)xit between two rooms\nGo (B)ack to the previous menu \n> ').lower()
                if creation_text == 'r' or creation_text == 'room':
                    room = generate_room()
                    rooms[room.name] = room
                elif creation_text == 'i' or creation_text == 'item':
                    if len(rooms) > 0:
                        item = generate_item()
                        items[item.name] = item
                    else:
                        input('You need a room to put an item in before you can make an item.  Press enter to continue')
                elif creation_text == 's' or creation_text == 'solution':
                    item, room = generate_solution()
                    input('The use for {} is now in {}.'.format(item.name,room.name))
                elif creation_text == 'e' or creation_text == 'exit':
                    room1, room2, exit1, exit2 = generate_exit()
                    input('{} has an exit {} to {}'.format(room1.name, exit1, room2.name))
                    input('{} has an exit {} to {}'.format(room2.name, exit2, room1.name))
                elif creation_text == 'b' or creation_text == 'back':
                    break
        elif text == 'e' or text == 'edit':
            while True:
                editable = input('Please enter the room or item you would like to edit. Type back to retern to the previous menu \n> ').lower()
                if editable in rooms:
                    edit_room(rooms[editable])
                elif editable in items:
                    edit_item(items[item])
                elif editable == 'back':
                    break
                else:
                    input('I did not find that item or room.  Press enter for a list of rooms and items')
                    print_rooms(rooms)
                    print_items(items)
        elif text == 'v' or text == 'view':
            for room in rooms.values():
                print(room.name + ' contains the following:')
                for item in room.items.values():
                    print('\t' + item.name)
        elif text == 'd' or text == 'done':
            while True:
                starting_room = input('Please enter the name of the starting room \n> ').lower()
                if room_check(starting_room):
                    rooms[starting_room].starting_room = True
                    break
                else:
                    input('I\'m sorry, I could not find that room.  Press enter to see existing rooms')
                    print_rooms(rooms)
            filename = input('Please enter the name of the file. letters and numbers only please. \n> ').lower()
            if filename:
                with open(filename, 'wb') as f:
                    pickle.dump([room for room in rooms.values()], f)
            break


            
def generate_room():
    '''A function to create a room.  Relies on human input'''
    name = input('Please enter the name of the room \n> ').lower()
    description = input('Please enter what the player sees when they enter or view the room \n> ').lower()
    room = Room(name, description)
    while True:
        new_items = input('Would you like to add an item to the room? Y/N \n> ').lower()
        if new_items == 'y' or new_items == 'yes':
            item = generate_item(room)
            items[item.name] = item
        else:
            break
    return room 

def generate_item(room=None, solved=False):
    '''A function to create an item, requires a room. Relies on human input'''
    name = input('Please enter the name of the item \n> ').lower()
    view = input('Please enter what the item looks like in the room\n > ').lower()
    description = input('Please enter what the item looks like in the player inventory\n > ').lower()
    if solved and room:
        room.add_solved_item(name, description, view)
        return room.solved_items[name]
    elif room:
        room.add_item(name, description, view)
        return  room.items[name]
    else:
        while True:
            if room == None:
                room = input('Please enter the name of the room this item is in \n> ').lower()
            if room in rooms:
                room = rooms[room]
                if solved:
                    room.add_solved_item(name, description, view)
                    return room.solved_items[name]
                else:
                    room.add_item(name, description, view)
                    return room.items[name]
            elif room == 'exit' or room == 'quit':
                break
            else:
                input('I\'m sorry, I could not find that room.  Press enter to see existing rooms')
                print_rooms(rooms)
                room = None

def generate_solution(item=None, room=None, items=items, rooms=rooms, success_message=None):
    '''given an item and a room, creates a solution for the item in the room.'''
    while True:
        if item == None:
            item = input('Please enter the item you want to provide a use for \n> ').lower()
        item = item_check(item, items)
        if item:
            while True:
                if room == None:
                    room = input('Please enter the room name you want {} to solve \n> '.format(item.name)).lower()
                room = room_check(room, rooms)
                if room:
                    item.use = room
                    if success_message:
                        item.success_message = success_message
                    else:
                        item.success_message = input('Please enter the message that will be read when you use the item \n> ').lower()
                    return (item,room) 
                else:
                    input('I\'m sorry, I could not find that room. Press enter to see all existing rooms')
                    print_rooms(rooms)
        else:
            input('I\'m sorry, I could not find that item.  Press enter to see existing items')
            print_items(items)
            item = None

def generate_exit(room1=None, exit1=None, room2=None, exit2=None, solved=False):
    '''Creates exits between 2 rooms, can be automated by feeding both rooms and both exit names'''
    if room1 == None:
        while True:
            room1 = input('Please enter the first room you want an exit in. \n> ').lower()
            room1 = room_check(room1)
            if room1:
                break
            else:
                input('I\'m sorry, I could not find that room. Press enter to see all existing rooms')
                print_rooms(rooms)
    if room2 == None:
        while True:
            room2 = input('Please enter the second room you want an exit in. \n> ').lower()
            room2 = room_check(room2)
            if room2:
                break
            else:
                input('I\'m sorry, I could not find that room. Press enter to see all existing rooms')
                print_rooms(rooms)
    if exit1 == None:
        exit1 = input('Please enter the name of the exit from {} to {}.  Ex. North. \n> '.format(room1.name, room2.name)).lower()
    if exit2 == None:
        exit2 = input('Please enter the name of the exit from {} to {}. Ex. South \n> '.format(room2.name, room1.name)).lower()
    if solved:
        room1.solved_exits[exit1] = room2
    else:
        room1.exits[exit1] = room2
    room2.exits[exit2] = room1 
    return (room1, room2, exit1, exit2)

def edit_room(room):
    '''Allows for editing of existing room parameters'''
    while True:
        editable = input('Would you like to edit the \n'
                        '(N)ame of the room \n'
                        '(D)escription of the room \n'
                        '(I)tems in the room \n'
                        '(E)xits in the room \n'
                        '(P)uzzle parameters of the room \n'
                        '(S)ave and quit \n> ').lower()
        if editable == 'n':
            name = input('Please enter the new name for the room \n> ').lower()
            room.name = name
        elif editable == 'd':
            description = input('Please enter the new description for the room \n> ').lower()
            room.description = description
        elif editable == 'i':
            while True:
                print_items(room.items)
                item = input('Please enter one of the above items to edit \n(A)dd a new item \n(B)ack to room editing \n> ').lower()
                if item == 'a':
                    add_item(room)
                elif item == 'b':
                    break
                elif item_check(item):
                    edit_item(item)
                else:
                    print('I did not find that item.  Please re-enter.')
        elif editable == 'p':
            while True:
                editable = input('Would you like to edit the \n'
                                '(D)escription of the room after solution \n'
                                '(I)tems in the room after solving \n'
                                '(E)xits in the room after solving \n'
                                '(B)ack to previous menu \n> ').lower()
                if editable == 'd':
                    description = input('Please enter the new description \n> ').lower()
                    room.solved_description = description
                elif editable == 'i':
                    item = generate_item(room, solved=True)
                    items[item.name] = item
                elif editable == 'e':
                    generate_exit(room, solved=True)
                elif editable == 'b':
                    break
                else:
                    input('I did not understand that input.  Press enter to continue')
        elif editable == 's':
            break
        else:
            input('I did not understand that input.  Press enter to continue')

def edit_item(item):
    '''Allows for editing of existing item parameters'''
    while True:
        editable = input('Would you like to edit the \n'
                         '(N)ame of the item \n'
                         '(D)escription of the item in your inventory \n'
                         '(V)iew of the item in the room \n'
                         '(U)se of the item \n'
                         '(M)essage the item gives after use \n'
                         '(Q)uit editing the item \n> ').lower()
        if ediable == 'n':
            name = input('Please enter the new name for the item \n> ').lower()
            del items[item]
            item.name = name
            items[name] = item
        elif ediable == 'd':
            description = input('Please enter the new description for the item while in your inventory \n> ').lower()
            item.description = description
        elif editable == 'v':
            view = input('Please enter the new view for the item while still in the room \n> ').lower()
            item.view = view
        elif editable == 'u':
            while True:
                room = room_check(input('Please enter the first room you want an exit in. \n> ').lower())
                if room: 
                    item.use = room
                    break
                else:
                    input('I\'m sorry, I could not find that room. Press enter to see all existing rooms')
                    print_rooms(rooms)
        elif editable == 'm':
            success_message = input('Please enter the message for the item to read on successful usage. \n> ').lower()
            item.success_message = success_message
        elif editable == 'q':
            break

if __name__ == '__main__':
    generation_loop()
