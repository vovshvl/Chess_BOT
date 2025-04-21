from board import *
from engine import *
from best_move import all_moves

board = initialise_test_board()
print_board(board)
#print(sorted(all_moves(board)))
print(board[1][1].legal_moves(board))

