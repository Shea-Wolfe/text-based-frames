def value_matcher(dictionary, string):
    return [value for key, value in dictionary.items() if string in key][0]


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
            item = dict_finder(self.inventory, item_name)
            if self.room == item.use:
                item.success()
                del self.inventory[item_name]
            else:
                print("You can't use that here")
        else:
            print('Please enter a valid item')

    def view_item(self, item):
        '''intented to cover viewing items in your inventory.
        viewing an item show hint at the puzzle it is intended to solve'''
        if item in self.inventory:
            print(dict_finder(self.inventory, item).description)
        else:
            print('That\'s not in your inventory!')

    def room_item_view(self, item):
        if item in self.room.items:
            print(dict_finder(self.room.items, item))
        else:
            print('That\'s not in the room!')

    def get_item(self, item):
        if item in self.room.items:
            item_name, item = [(key, value) for key, value in self.room.items.items() if item in key][0]
            self.inventory[item_name] = item
            print('You got {}'.format(item_name))
            del self.room.items[item_name]
        else:
            print('You can\'t get that!')

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
   def __init__(self, name, description, solved_exits=None, solved_items=None, solved_description=None, success_message=None):
        self.exits = {} #due to exits requiring other rooms they have to be added post init. format is {exit_name:Room}
        self.items = {} #Items in the room, a dictionary with {string:Item}, same issues as above.
        self.description = description #what they get from walking in
        self.name = name #What the player will see, hopefully, static on screen
        self.solved_exits = solved_exits #New exits that appear when you solve the room
        self.solved_items = solved_items #New items that appear when you solve the room
        self.solved_description = solved_description #A new description that appears after you solve the room
        self.success_message = success_message #A message that reads after you solve the room
    
   def add_exit(self, exit_name, room):
       '''intended for creation purposes, allows you to name an exit and attach it to another room'''
       self.exits[exit_name] = room
       return 'exit created'

   def add_item(self, name, description, view, use, success):
       self.items[name] = Item(name, description, view,  use, success)
    
   def solved(self):
       for exit in self.solved_exits:
           self.exits[exit] = self.solved_exits[exit]
       for item in self.solved_items:
           self.items[item] = self.solved_items[item]
       self.description = self.solved_description
       print(self.success_message)
       

            
class Item():
    """intended to cover all information about an item"""
    def __init__(self, name, description, view,  use, success):
        self.name = name
        self.view = view #what an item looks like in a room.
        self.description = description #seen with view_item()
        self.use = use #current setup if for each item to have one and only one use, based on location, thus this is a Room
        self.success_message = success #A text string describing what happens when you use an item.

    def success(self, use):
        print(self.success)
        use.solved()
