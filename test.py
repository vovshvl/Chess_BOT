from board import *
from engine import *
board = initialise_test_board()

print_board(board)
Piece = board[0][6]
Piece.move(board,1,6)
print_board(board)
