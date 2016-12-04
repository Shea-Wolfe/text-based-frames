from classes import Player, Room
import re
import sys
import pickle
def parse_text(player, room, rooms):
    text = input('> ')
    text = text.lower()
    #move rooms
    if re.search('move',text) or re.search('go',text):
        player.move_rooms(text)
    #take item
    elif re.search('take',text) or re.search('get',text):
        player.get_item(text)
    #look rooms/items
    elif re.search('look', text) or re.search('view', text):
        if len(text) == 4 or text == 'look room' or text == 'view room':
            player.view_room()
        elif re.search('inventory',text):
            player.view_inventory()
        elif re.search('exits',text):
            player.view_exits()
        else:
            player.view_item(text)
    #use item
    elif re.search('use',text):
        player.use_item(text)
    elif re.search('help',text):
        print('commands are \"move\", \"take\", \"look\", \"use\", or \"quit\"')
    elif re.search('quit',text):
        game_save = input('Please enter a name for your save game.')
        if game_save:
            with open(game_save, 'wb') as f:
                pickle.dump(room,f)
                pickle.dump(player,f)
        sys.exit()
    else:
        print('I didn\'t understand that.  Please start your statement with move, get, look, or use')
