from engine import King
from engine import Queen
from engine import Bishop
from engine import Knight
from engine import Rook

pieces =[
    King(-6, 0, 4),
    King(6, 7, 4),
    Rook(-4, 0, 0),
    Rook(-4, 0, 7),
    Rook(4, 7, 7),
    Rook(4, 7, 0)
]
board = [[None for _ in range(8)] for _ in range(8)]
def initialise_board():

    for piece in pieces:
        board[piece.row][piece.col] = piece


def print_board():
    print("  0 1 2 3 4 5 6 7")
    print("-----------------")
    for r in range(8):
        print(f"{r}|", end="")
        for c in range(8):
            value = board[r][c]
            print(f"{value:2} ", end="")

            print("-----------------")
