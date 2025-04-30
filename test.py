from board import *
from engine import *
from best_move import *
from Move import Move

def test_moves():
    board = initialise_test_board()
    print_board(board)

    #move1 = Move((0, 0), (0, 5))
    moves = all_moves(board, 1)

    make_move(board, moves[15])
    print_board(board)

    undo_move(board, moves[15])
    print_board(board)

#test_moves()



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
    print(moves)
    move1 = minmax(board, moves, 3, -float('inf'), float('inf'), 1)[1]
    print (move1)
    make_move(board, move1)
    print_board(board)
    print(evaluate_board(board))

    moves = all_moves(board, -1)
    move2 = minmax(board, moves, 3, -float('inf'), float('inf'), -1)[1]
    make_move(board, move2)
    print_board(board)
    print(evaluate_board(board))


def inialisegame():
    board = initialise_board()
    starting_color = 1
    play_moves(board, starting_color, 50)

def play_moves(board, starting_color, moves_to_play, depth=5):
    color = starting_color
    for _ in range(moves_to_play):
        print_board(board)
        print("Evaluation:", evaluate_board(board))

        moves = all_moves(board, color)
        if not moves:
            print(f"No moves available for color {color}.")
            break

        best_move = minmax(board, moves, depth, -float('inf'), float('inf'), color)[1]
        print("Best move:", best_move)
        make_move(board, best_move)

        # Switch color for next move
        color = -color

    # Final board state after all moves
    print_board(board)
    print("Final Evaluation:", evaluate_board(board))


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
test_game()
#test_allmoves()

def test_eval():
    board = initialise_test_board()

    print(evaluate_board(board))

#test_eval()
#test_moves()
inialisegame()
def test_is_checkmate():
    board = initialise_test_board()
    print_board(board)

    if board[0][4].is_checkmate(board) == True:
        print("checkmate")
    else:
        print("not checkmate")

#test_is_checkmate()