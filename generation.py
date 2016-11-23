from classes import *
rooms = {}
items = {}

def print_rooms(existing_rooms):
    for room in existing_rooms:
        print(room)

def print_items(existing_items):
    for item in existing_items:
        print(item)

def generation_loop():
    whlie True:
        text = input('please (C)reate, (E)dit, or  (D)one').lower()
        if text == 'c' or text == 'create':
            while True:
                creation_text = input('Would you like to make\nA (R)oom\nAdd an (I)tem to an existing room\nAdd a (S)olution to a room/item combo\nAn (E)xit between two rooms\nGo (B)ack to the previous menu').lower()
                if creation_text == 'r' or creation_text == 'room':
                    room = generate_room()
                    rooms[room.name] = room
                elif creation_text == 'i' or creation_text == 'item':
                    item = generate_item()
                    items[item.name] = item
                elif creation_text == 's' or creation_text == 'solution':
                    generate_solution()
                elif creation_text == 'e' or creation_text == 'exit':
                    generate_exit()
                elif creation_text == 'b' or creation_text == 'back':
                    break
        elif text == 'e' or text == 'edit':
            #edit rooms/items
        elif text == 'd' or text == 'done':
            #write the file

            
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
            room = input('Please enter the name of the room this item is in').lower()
            if room in rooms:
                room = rooms[room]
                return item
            elif room == 'exit' or room == 'quit'
                break
            else:
                input('I\'m sorry, I could not find that room.  Press enter to see existing rooms')
                print_rooms(rooms)

def generate_solutions():
    while True:
        item = input('Please enter the item you want to provide a use for').lower()
        if item in items:
            item = items[item]
            while True:
                room = input('Please enter the room name you want {} to solve'.format(item.name)).lower()
                if room in rooms:
                    item.use = rooms[room]
                    input('The use for {} is now in {}.  Press enter to continue'.format(item.name,room.name))
                    return
                else:
                    input('I\'m sorry, I could not find that room. Press enter to see all existing rooms')
                    print_rooms(rooms)
        else:
            input('I\'m sorry, I could not find that item.  Press enter to see existing items')
            print_items(items)


