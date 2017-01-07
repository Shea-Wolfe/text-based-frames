from classes import Player, Room, Game
import re
import sys
import pickle
def parse_text(player, room, rooms, text=None, game_save=None):
    '''Takes text input and looks for key phrases and runs methods based on said phrases'''
    if not text: #For testing purposes I made it so you could feed the text directly
        text = input('> ')
    text = text.lower() #All text is lowered for consistancy
    #move rooms
    if re.search('move',text) or re.search('go',text): #Use the common move and go options, more could be added.
        player.move_rooms(text) #See classes.py for method descriptions, this changes player.room based on the exit input
    #take item
    elif re.search('take',text) or re.search('get',text):# Take or Get seem common choices here
        player.get_item(text) #See classes.py, this adds an item to the inventory based on input
    #look rooms/items
    elif re.search('look', text) or re.search('view', text): #For looking around the room
        if len(text) == 4 or text == 'look room' or text == 'view room': #If it's 4 we assume they just typed 'look' 
            player.view_room() #This just prints the room description
        elif re.search('inventory',text): 
            player.view_inventory() #Prints an inventory list.
        elif re.search('exits',text):
            player.view_exits() #Prints a neat list of exits that currently exist.  Does not see unsolved exits
        else:
            player.view_item(text) #If not otherwise specified we assume looking at an item.  Close or far is handled in classes.py
    #use item
    elif re.search('use',text):
        player.use_item(text) #The text should contain the name of the item being used
    elif re.search('help',text):
        print('commands are \"move\", \"take\", \"look\", \"use\", or \"quit\"') #We only give one option for each action, secondary options are just for comfort
    elif re.search('quit',text): #When a player wants to stop they quit, note there's no save and continue at present
        if not game_save: #For testing we allow a save name to be directly fed into the function
            game_save = input('Please enter a name for your save game.') #This will be pickled and can be reloaded using game_unpacker.py
        if game_save:
            with open(game_save, 'wb') as f:
                pickle.dump(Game(rooms, player),f) #This is how we pickle the game save
        return False 
    else:
        print('I didn\'t understand that.  Please try entering move, take, look, use, quit, or help') #Give feedback if they don't enter proper commands. 
