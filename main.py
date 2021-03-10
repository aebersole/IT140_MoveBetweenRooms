# 6-4 Milestone Move Between Rooms
# Adam Ebersole IT-140

import time

player_directions = [
    'n', 's', 'e', 'w'
]
player_commands = [
    'search', 'quit', 'look'
]


def promenade():
    prom_description = 'You are standing in the Promenade, you see an exit to the South'
    print(prom_description)

    room_p = 1
    while room_p == 1:
        time.sleep(0.5)
        player_input = input(
            'What would you like to do? '
        ).lower()

        if player_input == 'look':
            print(prom_description)
            room_p = 1
        elif player_input == 'search':
            print('You search the room but find nothing useful.')
            room_p = 1
        elif player_input == 's':
            print('You head south out of the room.')
            time.sleep(1)
            room_p = 2
            passenger_lounge()
        #       elif player_input == 'n' or 'e' or 'w':
        #           print('There is nothing in that direction.')
        #           room_p = 1
        elif player_input == 'quit':
            print('Thanks for playing!')
            quit()
            room_p = 2
        else:
            print('Invalid Entry, please try again.')
            room_p = 1


def passenger_lounge():
    pl_description = 'You are standing in the Passenger Lounge, you see an exit to the North.'
    print(pl_description)

    room_pl = 1
    while room_pl == 1:
        time.sleep(0.5)
        player_input = input(
            'What would you like to do? '
        ).lower()

        if player_input == 'look':
            print(pl_description)
            room_pl = 1
        elif player_input == 'search':
            print('You search the room but find nothing useful.')
            room_pl = 1
        elif player_input == 'n':
            print('You head North out of the room.')
            time.sleep(1)
            room_pl = 2
            promenade()
        #       elif player_input == 's' or 'e' or 'w':
        #           print('There is nothing in that direction.')
        #           room_pl = 1
        elif player_input == 'quit':
            print('Thanks for playing!')
            quit()
            room_pl = 2
        else:
            print('Invalid Entry, please try again.')
            room_pl = 1


print('Welcome to the game!')
time.sleep(.5)
print('#FIXME to work with help.')
time.sleep(.5)
promenade()
