from room import Room
from player import Player
from item import Item
from player_actions import *

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Torch", "A burning stick")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Dagger", "A short pointed weapon")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Helmet", "A protective head covering made of hard material")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",  [Item("Gold coin", "A coin made of gold")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Gold coin", "A coin made of gold")]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


def quit_game( _, __):
    global game_on
    game_on = False
    

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user_name = input("Please enter your name... ")
player = Player(user_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# def check_location(direction):
#     pass

game_on = True

print(f"{player.current_room.name}, {player.current_room.desc} \n")
print("Items in room:")
print(*[item for item in player.current_room.items], sep=',')

player_action = {

    'q': quit_game,
    'take': take_item,
    'drop': drop_item,
    'i': check_inventory,
    'n': move_north,
    'e': move_east,
    's': move_south,
    'w': move_west,

    }

while game_on:
    user_input = input("Where would you like to do? q to quit game ")
    print('\n')

    user_input = user_input.split(" ")
    try:
        player_action.get(user_input[0])(user_input, player)
    except:
        print(f"{user_input[0]} is not a valid input")
    
    if game_on == True:
        print(f"{player.current_room.name}, {player.current_room.desc}\n")
        print("Items in room:")
        print(*[item for item in player.current_room.items], sep=',')
