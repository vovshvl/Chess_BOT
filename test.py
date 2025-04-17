from board import print_board, initialise_board,initialise_test_board
from engine import *
board = initialise_test_board()

print_board(board)

if board[3][3].is_check(board)== True:
    print('defended')
else:
    print("false")

