from board import *
from engine import *
from best_move import all_moves

board = initialise_board()
print_board(board)

i = 0
for move in all_moves(board, 1):
    #print(move.from_square)
    print(move.to_square)
    i = i+1
print(i)