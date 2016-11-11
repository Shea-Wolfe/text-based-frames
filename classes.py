

class Player():
"""intended to cover all actions the player may make"""
    def __init__(self, starting_location):
        self.location = starting_location
        self.inventory = [,]
    

    def view_inventory(self):
        '''intended to allow for review of picked up items'''
        if len(self.inventory) == 0:
            print('You do not have anything on you')
        elif len(self.inventory) == 1:       
            print('You are currently holding {}'.format(self.inventory[0].name))
        else:
            item_list = 'You are currently holding '
            for item in self.inventory[:-1]:
                item_list + item.name + " and "
            item_list + self.inventory[-1].name
            print(item_list)

    def use_item(self, item):
        '''intended to cover item usage for puzzle solving, basic form'''
        if self.location == item.use and item in self.inventory:
            item.success()
            self.inventory.remove(item)
        elif item not in self.inventory:
            print("Please enter a valid item.")
        else:
            print("You can't use that here")

    def view_item(self, item):
        '''intented to cover viewing items in your inventory.
        viewing an item show hint at the puzzle it is intended to solve'''
        if item in self.inventory:
            print(item.description)


class Room(self): 
   """intended to cover all information about a room""" 
    def __init__(self, name, description,  exits, items):
        self.exits = exits
        self.items = items
        self.description = description
        self.name = name
    


            
class Item():
"""intended to cover all information about an item"""
    def __init__(self, name, description, use):
        self.name = name
        self.desciption = description
        self.use = use
        
