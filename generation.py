from classes import *
rooms = {}
items = []
def generation_loop():
    whlie True:
        text = input('please (C)reate, (E)dit, or  (D)one').lower()
        if text == 'c' or text == 'create':
            creation_text = input('Would you like to make\nA (R)oom\nAdd an (I)tem to an existing room\nAdd a (S)olution to a room/item combo\nAn (E)xit between two rooms\nGo (B)ack to the previous menu').lower()
            if creation_text == 'r' or creation_text == 'room':
                #make a room
            elif creation_text == 'i' or creation_text == 'item':
                #make an item in an existing room
            elif creation_text == 's' or creation_text == 'solution':
                #added solution elements to an existing room/item
            elif creation_text == 'e' or creation_text == 'exit':
                #create an exit link for two rooms
            elif creation_text == 'b' or creation_text == 'back':
                break
        elif text == 'e' or text == 'edit':
            #edit rooms/items
        elif text == 'd' or text == 'done':
            #write the file

            
    
