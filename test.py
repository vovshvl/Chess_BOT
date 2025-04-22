from board import *
from engine import *
from best_move import *
from Move import Move

def test_moves():
    board = initialise_test_board()
    print_board(board)

    move = all_moves(board, 1)[15]
    # move = Move((1, 1), (0, 1), None, Queen(6, 0, 1))
    make_move(board, move)
    print_board(board)

    undo_move(board, move)
    print_board(board)

def test_allmoves():
    board = initialise_board()
    moves1 = all_moves(board, 1)
    moves2 = all_moves(board, -1)


def test_minmax():
    board = initialise_board()
    make_move(board,Move((6,4),(4,4)))
    print_board(board)
    print (evaluate_board(board))
    moves = all_moves(board, 1)
    print(minmax(board, moves, 4, -float('inf'), float('inf'), 1)[1].to_square)

test_minmax()
#test_allmoves()