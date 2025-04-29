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
    King(-6, 0, 4)

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

white_king_square = (7, 4)
black_king_square = (0, 4)

def make_move(board, move):
    from_row, from_col = move.from_square
    to_row, to_col = move.to_square
    move.piece_captured = board[to_row][to_col]

    moving_piece = board[from_row][from_col]

    if moving_piece is None:
        return False
    #King
    if moving_piece.value == 6:
        global white_king_square
        white_king_square = (to_row, to_col)
    if moving_piece.value == -6:
        global black_king_square
        black_king_square = (to_row, to_col)
    #Promotion
    if (moving_piece.value == 1 or moving_piece.value == -1) and (to_row == 0 or to_row == 7):
        board[to_row][to_col] = move.promotion
    else:
        board[to_row][to_col] = moving_piece

    #Castling
    if move.castling_king is not None:
        board[to_row][to_col] = moving_piece
        board[from_row][from_col] = None
        board[to_row][to_col-1] = move.castling_king
        board[to_row][to_col+1] = None

    if move.castling_queen is not None:
        board[to_row][to_col] = moving_piece
        board[from_row][from_col] = None
        board[to_row][to_col+1] = move.castling_queen
        board[to_row][to_col-2] = None

    #Rest
    moving_piece.row = to_row
    moving_piece.col = to_col
    board[from_row][from_col] = None

def undo_move(board, move):
    from_row, from_col = move.from_square
    to_row, to_col = move.to_square

    moving_piece = board[to_row][to_col]
    if moving_piece is None:
        return False

    if move.promotion is not None:
        if moving_piece.value>0:
            val = 1
        else:
            val = -1
        board[from_row][from_col] = Pawn(val, from_row, from_col)
    else:
        board[from_row][from_col] = moving_piece

    if move.castling_king is not None:
        board[move.castling_king.row][move.castling_king.col] = Rook(move.castling_king.value, move.castling_king.row, move.castling_king.col)
        board[from_row][from_col+1] = None
    if move.castling_queen is not None:
        board[move.castling_queen.row][move.castling_queen.col] = Rook(move.castling_queen.value, move.castling_queen.row, move.castling_queen.col)
        board[from_row][from_col-1] = None

    #Rest
    moving_piece.row = from_row
    moving_piece.col = from_col
    board[to_row][to_col] = move.piece_captured



def get_white_king_square():
    return white_king_square

def get_black_king_square():
    return black_king_square

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