import random
import os

def roll_dice():
    return random.randint(1, 6)

os.system('clear')
while True:
    ans = input('Give number of players (2-4): ')

    if ans.isdigit():
        players = int(ans)
        if 2 <= players <= 4:
            break
        else:
            print('Give a number between 2 and 4')
    else:
        print('Wrong input, try again')

scores = [0 for _ in range(players)]

player = (player + 1) % players # Here!
still_playing = True
total, value = 0, 0 
while still_playing:
    ans = input('Roll (r) or Stop (s)?: ')
    if ans.lower() == 'r':
        value = roll_dice()
        print('Rolled:', value)
        if value == 1:
            print('You rolled 1, you lost your turn')
        total = total + value
        print('Total score:', total)
    elif ans.lower() == 's':
        still_playing = False
    else:
        print('Wrong input, try again')
