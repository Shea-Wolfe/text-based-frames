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
    elif words[0] == 'look':
        try:
            if words[1] == 'room':
                player.view_room()
            elif words[1] in player.inventory:
                player.view_inventory(words[1])
            elif words[1] in room.items:
                print(room.items[words[1]].view)
            else:
                print('What did you want to look at?')
        except:
            print('Please enter what you\'d like to look at!')
    elif words[0] == 'use':
        try:
            player.use_item(words[1])
        except:
            print('What do you want to use?')
    else:
        print('Invalid command, try look, move, or use')
    
