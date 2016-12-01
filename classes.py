from re import search

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
            print(item_list + "\n".join(self.inventory.keys()))    

    def view_exits(self):
        '''let's the player see potential exits'''
        exit_list = 'Exits are: '
        print(exit_list + ', '.join(self.room.exits.keys())) 


    def use_item(self, text):
        '''intended to cover item usage for puzzle solving, basic form'''
        for item in self.inventory:
            if search(item, text):
                use_item = self.inventory[item]
                if use_item.use == self.room:
                    self.room.solved()
                    print(use_item.success_message)
                    del self.inventory[item]
                    return
                else:
                    print('You can\'t use that here!')

        print('Please enter a valid item')
        

    def view_item(self, text):
        for item in self.room.items:
            if search(item, text):
                return self.room.items[item].far_view()
        for item in self.inventory:
            if search(item, text):
                return self.inventory[item].close_view()
        if search(text, 'inventory'):
            return self.view_inventory()
        print('Please enter a valid item or \"inventory\" to view your entire inventory')
        

    def get_item(self, text):
        for item in self.room.items:
            if search(item, text):
                self.inventory[item] = self.room.items[item]
                del self.room.items[item]
                print('you got {}'.format(item))
                break
        else:
            print('You can\'t get that!')

    def view_room(self):
        '''allows player to get information about a room'''
        print(self.room.description)

    def move_rooms(self, text):
        for exit in self.room.exits:
            if search(exit,text):
                self.room = self.room.exits[exit]
                print(self.room.description)
                break
        else:
            print('That\'s not a valid exit!')

class Room(): 
    """intended to cover all information about a room""" 
    def __init__(self, name, description, solved_description=None, success_message=None):
        self.exits = {} #due to exits requiring other rooms they have to be added post init. format is {exit_name:Room}
        self.items = {} #Items in the room, a dictionary with {string:Item}, same issues as above.
        self.description = description #what they get from walking in
        self.name = name #What the player will see, hopefully, static on screen
        self.solved_exits = {} #New exits that appear when you solve the room
        self.solved_items = {} #New items that appear when you solve the room
        self.solved_description = solved_description #A new description that appears after you solve the room
        self.success_message = success_message #A message that reads after you solve the room
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


