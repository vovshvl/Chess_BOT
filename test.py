from board import *
from engine import *
from best_move import *

board = initialise_test_board()
print_board(board)

move = all_moves(board, -1)[11]
make_move(board, move)
print_board(board)

undo_move(board, move)
print_board(board)