import random

def roll_dice():
    return random.randint(1,6)

while True:
    ans = input('Give number of players(2-4): ')

    if ans.isdigit():
        ans = int(ans)
        if 2 <= ans <= 4:
            print('ok')
            break
        else:
            print('Give a number between 2 and 4')
    else:
        print('Wrong input, try again')