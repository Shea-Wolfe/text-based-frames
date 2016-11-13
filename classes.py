

class Player():
    """intended to cover all actions the player may make"""
    def __init__(self, starting_location):
        self.room = starting_location
        self.inventory = {} 
    

    def view_inventory(self):
        '''intended to allow for review of picked up items'''
        if len(self.inventory) == 0:
            print('You do not have anything on you')
        else:
            item_list = 'Your inventory contains  \n'
            print(item_list + "\n".join(self.inventory.values()))    

    def use_item(self, item_name):
        '''intended to cover item usage for puzzle solving, basic form'''
        if item_name in self.inventory:
            item = self.inventory[item_name]
            if self.room == item.use:
                item.success()
            else:
                print("You can't use that here")
        else:
            print('Please enter a valid item')

    def view_item(self, item):
        '''intented to cover viewing items in your inventory.
        viewing an item show hint at the puzzle it is intended to solve'''
        if item in self.inventory:
            print(self.inventory[item].description)

    def get_item(self, item):
        if item in self.room.items:
            self.inventory[item] = self.room.items[item]
            print('You got {}'.format(item))
            del self.room.items[item]

    def view_room(self):
        '''allows player to get information about a room'''
        print(self.room.description)

    def move_rooms(self, exit):
        if exit in self.room.exits:
            self.room = self.room.exits[exit]
            print(self.room.description)
        else:
            print('That\'s not a valid exit!')

class Room(): 
   """intended to cover all information about a room""" 
   def __init__(self, name, description):
        self.exits = {} #due to exits requiring other rooms they have to be added post init. format is {exit_name:Room}
        self.items = {} #Items in the room, a dictionary with {string:Item}, same issues as above.
        self.description = description #what they get from walking in
        self.name = name 
    
   def add_exit(self, exit_name, room):
       '''intended for creation purposes, allows you to name an exit and attach it to another room'''
       self.exits[exit_name] = room
       return 'exit created'

   def add_item(self, name, description, use):
       self.items[name] = Item(name, description, use)
    

            
class Item():
    """intended to cover all information about an item"""
    def __init__(self, name, description, use):
        self.name = name
        self.desciption = description #seen with view_item()
        self.use = use #current setup if for each item to have one and only one use, based on location, thus this is a Room
        
