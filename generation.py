from classes import *
rooms = {}
items = []
def generation_loop():
    whlie True:
        text = input('please (C)reate, (E)dit, or  (D)one').lower()
        if text == 'c' or text == 'create':
            creation_text = input('Would you like to make\nA (R)oom\nAdd an (I)tem to an existing room\nAdd a (S)olution to a room/item combo\nAn (E)xit between two rooms\nGo (B)ack to the previous menu').lower()
            if creation_text == 'r' or creation_text == 'room':
                room = generate_room()
                rooms[room.name] = room
            elif creation_text == 'i' or creation_text == 'item':
                items.append(generate_item())
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
            item = generate_item()
            room.items[item.name] = item
        else:
            break
    

