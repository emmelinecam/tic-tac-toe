# 2D arrays


import random
import time

grid= [['1','-','-','-'],['2','-','-','-'],['3', '-','-','-']]

squares = ['1,a','1,b','1,c','2,a','2,b','2,c','3,a','3,b','3,c']

def print_board():
    print('  a b c')
    print(" ".join(grid[0]))
    print(" ".join(grid[1]))
    print(" ".join(grid[2]))

def position_to_indexes(position):
    """
    takes a position in the format '1,a' and converts it into 2 0-indexed coordinates e.g. 0,1
    """
    x,y = position.split(',')
    x = int(x)-1
    y = ord(y) - 97
    return x, y


def board_change(position, symbol):
    x,y=position_to_indexes(position)
    grid[x][y+1] = symbol
    squares.remove(position)
    

print_board()
print('welcome to tic tac toe!')
print('are you ready to play? type the name of a square in the format \'row, column\' to start playing.')


while squares:
    player_position_choice = input('player choice: ')
    board_change(player_position_choice, 'o')
    print_board()


    print('the computer is making it\'s choice...')
    time.sleep(3)
    computer_position_choice = random.choice(squares)
    board_change(computer_position_choice, 'x')
    print_board()
