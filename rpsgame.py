from time import sleep
from random import randint

list = ['Rock', 'Paper', 'Scissor']

print('''Available Moves:
[0]Rock
[1]Paper
[2]Scissor''')

print('=-'*18)
player = int(input('Choose your move: '))
if player >= 3:
    print('Invalid Play!')
else:

    opponent = randint(0, 2)
    sleep(1)
    print('=-'*18)
    print('You threw: {}'.format(list[player]))
    print('Opponent threw: {}'.format(list[opponent]))
    print('=-'*18)
    sleep(1)
    
    if opponent == 0:
        if player == 0:
            print('DRAW')
        elif player == 1:
            print('YOU WON')
        elif player == 2:
            print('OPPONENT WON')
    elif opponent == 1:
        if player == 0:
            print('OPPONENT WON')
        elif player == 1:
            print('DRAW')
        elif player == 2:
            print('YOU WON')
    elif opponent == 2:
        if player == 0:
            print('YOU WON')
        elif player == 1:
            print('OPPONENT WON')
        elif player == 2:
            print('DRAW')
