from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

while game_on:
    user_input = input("Where would you like to go? n, e, s, w. q to quit game ")
    print('\n')
    if user_input == 'q':
        game_on = False
    if user_input == 'n':
        try: 
            player.current_room.n_to.name
            player.current_room = player.current_room.n_to
        except:
            print(f"You cannot go {user_input} from here...\n")
    elif user_input == 'e':
        try: 
            player.current_room.e_to.name
            player.current_room = player.current_room.e_to
        except:
            print(f"You cannot go {user_input} from here...\n")
    elif user_input == 's':
        try: 
            player.current_room.s_to.name
            player.current_room = player.current_room.s_to
        except:
            print(f"You cannot go {user_input} from here...\n")
    elif user_input == 'w':
        try: 
            player.current_room.w_to.name
            player.current_room = player.current_room.w_to
        except:
            print(f"You cannot go {user_input} from here...\n")

    if game_on == True:
        print(f"{player.current_room.name}, {player.current_room.desc}\n")
