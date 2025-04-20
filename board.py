from engine import King, Piece
from engine import Queen
from engine import Bishop
from engine import Knight
from engine import Rook
from engine import Pawn

pieces = [
    # Pawns
    *[Pawn(-1, 1, i) for i in range(8)],
    *[Pawn(1, 6, i) for i in range(8)],

    # Rooks
    Rook(-4, 0, 0),
    Rook(-4, 0, 7),
    Rook(4, 7, 0),
    Rook(4, 7, 7),

    # Knights
    Knight(-2, 0, 1),
    Knight(-2, 0, 6),
    Knight(2, 7, 1),
    Knight(2, 7, 6),

    # Bishops
    Bishop(-3, 0, 2),
    Bishop(-3, 0, 5),
    Bishop(3, 7, 2),
    Bishop(3, 7, 5),

    # Kings
    King(-6, 0, 4),
    King(6, 7, 4),

    # Queens
    Queen(-5, 0, 3),
    Queen(5, 7, 3),
]
testpieces = [
    King(6, 0,4),

    Queen(4, 4, 6),
    Knight(-2, 0, 1),
]
board = [[None for _ in range(8)] for _ in range(8)]
def initialise_board():

    for piece in pieces:
        board[piece.row][piece.col] = piece
    return board


def initialise_test_board():
    board = [[None for _ in range(8)] for _ in range(8)]
    for piece in testpieces:
        board[piece.row][piece.col] = piece
    return board
def print_board(board):
    print("  0 1 2 3 4 5 6 7")
    print("-----------------")
    for r in range(8):
        print(f"{r}|", end="")
        for c in range(8):
            value = board[r][c]
            print(f"{value.value if value else '0':2} ", end="")  # Or use value.symbol()
        print()
    print("-----------------")