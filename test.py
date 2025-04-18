from board import *
from engine import *
board = initialise_test_board()

print_board(board)
Piece=board[3][3]
Piece.move(board,3,4)
print(Piece)
print_board(board)
