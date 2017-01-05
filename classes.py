from re import search 

class Player(): #Used to track player location and items
    """intended to cover all actions the player may make"""
    def __init__(self, starting_location, name):
        self.room = starting_location #We need to know where to start, so we use this rather than forcing a starting room name
        self.inventory = {} #Where items the player pick up go, we check this to confirm a player can use something
        self.name = name #Only used for greetings currently, but a nice thing to have
    

    def view_inventory(self): #When a player 'look inventory' they get to see this list
        '''intended to allow for review of picked up items'''
        if len(self.inventory) == 0:
            print('You do not have anything on you')
        else:
            item_list = 'Your inventory contains  \n'
            print(item_list + "\n".join(self.inventory.keys()))    

    def view_exits(self): #When a player 'look exits' they get to see this list
        '''let's the player see potential exits'''
        exit_list = 'Exits are: '
        print(exit_list + ', '.join(self.room.exits.keys())) 


    def use_item(self, text): #Called with use 'item_name'
        '''intended to cover item usage for puzzle solving, basic form'''
        for item in self.inventory:
            if search(item, text): #Looks for the item name in the entered text.
                use_item = self.inventory[item] #Gets the Item object out of the inventory
                if use_item.use == self.room: #Check to see if the current room is where the item is used
                    self.room.solved() #Modifies the room with add'l exits and/or items
                    print(use_item.success_message) #Used to alert the player to success/give feedback
                    del self.inventory[item] #Removes the item from the game, no multi-use items
                    return
                else:
                    print('You can\'t use that here!') #If the player uses a real item in the wrong room we let them know

        print('Please enter a valid item') #If we can't find the entered item we let the player know
        

    def view_item(self, text): #Called with 'look item' or 'view item'
        for item in self.room.items: #First we see if the item is in the room
            if search(item, text):
                return self.room.items[item].far_view() # If so we give the player info they would see from a distance
        for item in self.inventory: #Then we check if it is in the inventory.
            if search(item, text):
                return self.inventory[item].close_view() #If so we give the players a more detailed description
        print('Please enter a valid item or \"inventory\" to view your entire inventory') #Let the player know if there isn't an item found
        

    def get_item(self, text): #Called with 'get item' or 'take item'
        for item in self.room.items: 
            if search(item, text):
                self.inventory[item] = self.room.items[item] #If one of the items in the room are being taken, we add it to inventory
                del self.room.items[item] #Then we delete the item from the room, each item will hopefully only ever exist in one place.
                print('you got {}'.format(item)) #Let the player know it worked
                break
        else:
            print('You can\'t get that!') #Perhaps needs refinement, lets the player know they failed

    def view_room(self): #Called with 'look room'
        '''allows player to get information about a room'''
        print(self.room.description) # Simply repeats the info you get for entering a room

    def move_rooms(self, text): #Called with 'move exit' or 'go exit'
        for exit in self.room.exits: #We scan through the exits that exist in the room we are in
            if search(exit,text): 
                self.room = self.room.exits[exit] #If we find one we change the players room to the one indicated by the exit (remember exits are a dictionary of {name:Room}
                print(self.room.description) #Give the player feedback to the new room they have entered
                break
        else:
            print('That\'s not a valid exit!') #Let the player know if the action fails

class Room(): 
    """intended to cover all information about a room""" 
    def __init__(self, name, description, solved_description=None):
        self.exits = {} #due to exits requiring other rooms they have to be added post init. format is {exit_name:Room}
        self.items = {} #Items in the room, a dictionary with {string:Item}, same issues as above.
        self.description = description #what they get from walking in
        self.name = name #What the player will see, hopefully, static on screen
        self.solved_exits = {} #New exits that appear when you solve the room
        self.solved_items = {} #New items that appear when you solve the room
        self.solved_description = solved_description #A new description that appears after you solve the room
        self.starting_room = False
    
    def add_exit(self, exit_name, room):
        '''intended for creation purposes, allows you to name an exit and attach it to another room'''
        self.exits[exit_name] = room
        return 'exit created'

    def add_item(self, name, description, view, use=None, success=None):
        self.items[name] = Item(name, description, view,  use, success)
        
    def add_solved_exit(self, exit_name, room):
        self.solved_exits[exit_name] = room
    
    def add_solved_item(self, name, description, view, use=None, success=None):
        self.solved_items[name] = Item(name, description, view, use, success)
  
    def add_solved_description(self, solved_description):
        self.solved_description = solved_description

    def solved(self):
        for exit in self.solved_exits:
            self.exits[exit] = self.solved_exits[exit]
        for item in self.solved_items:
            self.items[item] = self.solved_items[item]
        self.description = self.solved_description
       

            
class Item():
    """intended to cover all information about an item"""
    def __init__(self, name, description, view,  use=None, success=None):
        self.name = name
        self.view = view #what an item looks like in a room.
        self.description = description #seen with view_item()
        self.use = use #current setup if for each item to have one and only one use, based on location, thus this is a Room
        self.success_message = success #A text string describing what happens when you use an item.

    def close_view(self):
        print(self.description)

    def far_view(self):
        print(self.view)

    def add_use(self, room, success_message):
        self.use = room
        self.success_message = success_message

class Game():
    '''Intended to hold a single game session, used for saving/loading'''
    def __init__(self, rooms, player=None):
        self.player = player
        self.rooms = rooms

