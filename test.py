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
    board = initialise_test_board()
    moves1 = all_moves(board, 1)
    for move in moves1:
        print(move.to_square)
    #moves2 = all_moves(board, -1)

def test_minmax():
    board = initialise_test_board()
    print_board(board)
    print (evaluate_board(board))
    moves = all_moves(board, 1)
    move1 = minmax(board, moves, 3, -float('inf'), float('inf'), 1)[1]
    make_move(board, move1)
    print_board(board)
    print(evaluate_board(board))


def test_game():
    board = initialise_board()
    print_board(board)
    print (evaluate_board(board))
    moves = all_moves(board, 1)
    move1 = minmax(board, moves, 3, -float('inf'), float('inf'), 1)[1]
    make_move(board, move1)
    print_board(board)
    print(evaluate_board(board))

    moves = all_moves(board, -1)
    move2 = minmax(board, moves, 3, -float('inf'), float('inf'), -1)[1]
    make_move(board, move2)
    print_board(board)
    print(evaluate_board(board))

    moves = all_moves(board, 1)
    move3 = minmax(board, moves, 3, -float('inf'), float('inf'), 1)[1]
    make_move(board, move3)
    print_board(board)
    print(evaluate_board(board))

def test_checks():
    board = initialise_test_board()
    print_board(board)
    moves = all_moves(board, 1)
    for move in moves:
        if move_leads_to_check(board, move, (0,4)) == True:
            make_move(board, move)
    print_board(board)

    if board[0][4].is_check(board) == True:
        print("check")
    else:
        print("not check")

def test_sort_moves():
    board = initialise_test_board()
    print_board(board)
    moves = all_moves(board, 1)
    sort_moves(board, moves)
    for move in moves:
        print(move.move_score)
        print(move.to_square)
#test_game()
#test_allmoves()
test_minmax()
#test_checks()
#test_sort_moves()