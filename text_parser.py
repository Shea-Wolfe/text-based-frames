from classes import Player, Room


def parse_text(player, room)
    text = input('> ')
    text = text.lower()
    words = text.split()
    if words[0] == 'move' or words[0] == 'go':
        try:
            player.move_rooms(words[1])
        except:
            'Please enter where you would like to move!'
    elif words[0] == 'look':
        #look at stuff
    elif words[0] == 'use':
        try:
            player.use_item(words[1])

    
