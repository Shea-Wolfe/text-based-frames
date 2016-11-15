from classes import Player, Room


def parse_text(player, room):
    text = input('> ')
    text = text.lower()
    words = text.split()
    if words[0] == 'move' or words[0] == 'go':
        try:
            player.move_rooms(words[1])
        except:
           print('Please enter where you would like to move!')
    elif words[0] == 'look' or words[0] == 'view':
        try:
            if words[1] == 'room':
                player.view_room()
            elif ' '.join(words[1:]) in player.inventory:
                player.view_item(' '.join(words[1:]))
            elif ' '.join(words[1]) in room.items:
                room_item_view(' '.join(words[1:]))
            else:
                print('What did you want to look at?')
        except:
            print('Please enter what you\'d like to look at!')
    elif words[0] == 'use':
        try:
            player.use_item(' '.join(words[1:]))
        except:
            print('What do you want to use?')
    elif words[0] == 'get' or words[0] == 'take':
        try:
            player.get_item(' '.join((words[1:])))
        except:
            print('You can\'t get that!')
    else:
        print('Invalid command, try look, move, or use')
    
