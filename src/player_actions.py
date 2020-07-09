from room import Room
from player import Player
from item import Item


def take_item(user_input, player):
    if len(user_input) > 2:
        user_input = [' '.join(user_input[1:])]
        user_input.insert(0, '_')
    for i, v in enumerate(player.current_room.items):
        if user_input[1].lower() == v.name.lower():
            player.inventory.append(player.current_room.items[i])
            print(player.current_room.items[i].on_take())
            player.current_room.items.pop(i)
            break
        if i == (len(player.current_room.items) - 1):
            print(f"{user_input[1]} is not in the room.")

def drop_item(user_input, player):
    if len(user_input) > 2:
        user_input = [' '.join(user_input[1:])]
        user_input.insert(0, '_')
    for i, v in enumerate(player.inventory):
        if user_input[1].lower() == v.name.lower():
            player.current_room.items.append(player.inventory[i])
            print(player.inventory[i].on_drop())
            player.inventory.pop(i)
            break
        if i == (len(player.inventory) - 1):
            print(f"{user_input[1]} is not in your inventory.")   

def check_inventory(_, player):
    print(f"{player.name}'s, Inventory:")
    print(*[item for item in player.inventory], sep=', ')

def move_north(user_input, player):
    try: 
        player.current_room.n_to.name
        player.current_room = player.current_room.n_to
    except:
        print(f"You cannot go {user_input[0]} from here...\n")

def move_east(user_input, player):
    try: 
        player.current_room.e_to.name
        player.current_room = player.current_room.e_to
    except:
        print(f"You cannot go {user_input[0]} from here...\n")

def move_south(user_input, player):
    try: 
        player.current_room.s_to.name
        player.current_room = player.current_room.s_to
    except:
        print(f"You cannot go {user_input[0]} from here...\n")

def move_west(user_input, player):
    try: 
        player.current_room.w_to.name
        player.current_room = player.current_room.w_to
    except:
        print(f"You cannot go {user_input[0]} from here...\n")