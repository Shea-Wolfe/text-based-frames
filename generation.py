from classes import *
rooms = {}
items = {}

def print_rooms(existing_rooms):
    for room in existing_rooms:
        print(room)

def print_items(existing_items):
    for item in existing_items:
        print(item)

def test_room(room):
    if room in rooms:
        return rooms[room]
    else:
        return None

def test_item(item):
    if item in items:
        return items[item]
    else:
        return None

def generation_loop():
    while True:
        text = input('please (C)reate, (E)dit, or  (D)one').lower()
        if text == 'c' or text == 'create':
            while True:
                creation_text = input('Would you like to make\nA (R)oom\nAdd an (I)tem to an existing room\nAdd a (S)olution to a room/item combo\nAn (E)xit between two rooms\nGo (B)ack to the previous menu').lower()
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
                editable = input('Please enter the room or item you would like to edit. Type back to retern to the previous menu').lower()
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

        elif text == 'd' or text == 'done':
            pass#write the file

            
def generate_room():
    name = input('Please enter the name of the room').lower()
    description = input('Please enter what the player sees when they enter or view the room').lower()
    room = Room(name, description)
    while True:
        items = input('Would you like to add an item to the room? Y/N').lower()
        if items == 'y' or items == 'yes':
            item = generate_item(room)
            room.items[item.name] = item
        else:
            break
    return room 

def generate_item(room=None):
    name = input('Please enter the name of the item').lower()
    view = input('Please enter what the item looks like in the room').lower()
    description = input('Please enter what the item looks like in the player inventory').lower()
    if room:
        room.add_item(name, description, view)
    else:
        while True:
            if room == None:
                room = input('Please enter the name of the room this item is in').lower()
            if room in rooms:
                room = rooms[room]
                return item
            elif room == 'exit' or room == 'quit':
                break
            else:
                input('I\'m sorry, I could not find that room.  Press enter to see existing rooms')
                print_rooms(rooms)
                room = None

def generate_solution(item=None, room=None, items=items, rooms=rooms):
    '''given an item and a room, creates a solution for the item in the room.'''
    while True:
        if item == None:
            item = input('Please enter the item you want to provide a use for').lower()
        item = test_item(item)
        if item:
            while True:
                if room == None:
                    room = input('Please enter the room name you want {} to solve'.format(item.name)).lower()
                room = test_room(room)
                if room:
                    return (item,room) 
                else:
                    input('I\'m sorry, I could not find that room. Press enter to see all existing rooms')
                    print_rooms(rooms)
        else:
            input('I\'m sorry, I could not find that item.  Press enter to see existing items')
            print_items(items)
            item = None

def generate_exit(room1=None, exit1=None, room2=None, exit2=None):
    if room1 == None:
        while True:
            room1 = input('Please enter the first room you want an exit in.').lower()
            room1 = test_room(room1)
            if room1:
                break
            else:
                input('I\'m sorry, I could not find that room. Press enter to see all existing rooms')
                print_rooms(rooms)
    if room2 == None:
        while True:
            room2 = input('Please enter the second room you want an exit in.').lower()
            room2 = test_room(room2)
            if room2:
                break
            else:
                input('I\'m sorry, I could not find that room. Press enter to see all existing rooms')
                print_rooms(rooms)
    if exit1 == None:
        exit1 = input('Please enter the name of the exit from {} to {}.  Ex. North.'.format(room1.name, room2.name)).lower()
    if exit2 == None:
        exit2 = input('Please enter the name of the exit from {} to {}. Ex. South'.format(room2.name, room1.name)).lower()
    room1.exits[exit1] = room2
    room2.exits[exit2] = room1 
    return (room1, room2, exit1, exit2)

def edit_room(room):
    while True:
        editable = input('Would you like to edit the \n(N)ame of the room \n(D)escription of the room \n(I)tems in the room \n(E)xits in the room \n (P)uzzle parameters of the room \n(S)ave and quit').lower()
        if editable == 'n':
            name = input('Please enter the new name for the room').lower()
            room.name = name
        elif editable == 'd':
            description = input('Please enter the new description for the room').lower()
            room.description = description
        elif editable == 'i':
            while True:
                print_items(room.items)
                item = input('Please enter one of the above items to edit \n(A)dd a new item \n(B)ack to room editing').lower()
                if item == 'a':
                    add_item(room)
                elif item in room.items:
                    item = room.items[item]
                    edit_item(item)
                elif item == 'b':
                    break
                else:
                    print('I did not find that item.  Please re-enter.')
        elif editable == 'p':
            pass #change the solved paramaters of the room
        elif editable == 's':
            break
        else:
            input('I did not understand that input.  Press enter to continue')

def edit_item(item):
    while True:
        editable = input('''Would you like to edit the \n
                            (N)ame of the item \n
                            (D)escription of the item in your inventory \n
                            (V)iew of the item in the room \n
                            (U)se of the item \n
                            (M)essage the item gives after use
                            (Q)uit editing the item''').lower()
        if ediable == 'n':
            name = input('Please enter the new name for the item').lower()
            del items[item]
            item.name = name
            items(name) = item
        elif ediable == 'd':
            description = input('Please enter the new description for the item while in your inventory').lower()
            item.description = description
        elif editable == 'v':
            view = input('Please enter the new view for the item while still in the room').lower()
            item.view = view
        elif editable == 'u':
            while True:
                room = room_test(input('Please enter the first room you want an exit in.').lower())
                if room: 
                    item.use = room
                    break
                else:
                    input('I\'m sorry, I could not find that room. Press enter to see all existing rooms')
                    print_rooms(rooms)
        elif editable == 'm':
            success_message = input('Please enter the message for the item to read on successful usage.').lower()
            item.success_message = success_message
        elif editable == 'q':
            break


