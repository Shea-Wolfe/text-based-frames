from classes import Player, Room
import re

def parse_text(player, room):
    text = input('> ')
    text = text.lower()
    #move rooms
    if re.search('move',text) or re.search('go',text)::
        player.move_rooms(text)
    #take item
    elif re.search('take',text) or re.search('get',text):
        player.get_item(text)
    #look rooms/items
    elif re.search('look', text) or re.search('view', text):
        if len(text) == 4:
            player.view_room()
        else:
            player.view_item(text)
    #use item
    elif re.search('use',text):
        player.use_item(text)
    else:
        print('I didn\'t understand that.  Please start your statement with move, get, look, or use')
