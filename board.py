from pieces import King, Piece
from pieces import Queen
from pieces import Bishop
from pieces import Knight
from pieces import Rook
from pieces import Pawn

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
    Rook(-5, 0, 0)

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

def make_move(board, move):
    from_row, from_col = move.from_square
    to_row, to_col = move.to_square
    move.piece_captured = board[to_row][to_col]

    moving_piece = board[from_row][from_col]

    board[to_row][to_col] = moving_piece
    moving_piece.row = to_row
    moving_piece.col = to_col
    board[from_row][from_col] = None

def undo_move(board, move):
    from_row, from_col = move.from_square
    to_row, to_col = move.to_square

    moving_piece = board[to_row][to_col]

    board[from_row][from_col] = moving_piece
    moving_piece.row = from_row
    moving_piece.col = from_col
    board[to_row][to_col] = None



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