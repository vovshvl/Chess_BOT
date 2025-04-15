def print_board(board):
    for row in range(8):
        print(8 - row, "|", end=' ')
        for col in range(8):
            print(board[row][col], end=' ')
        print("|")
# Use integers with sign for color
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

# Negative = black, Positive = white
# Example: 3 = white bishop, -3 = black bishop
def Board_Setup():
    board = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        board[1][i] = -PAWN
        board[6][i] = PAWN
    board[0][0] = -ROOK
    board[0][7] = -ROOK
    board[7][7] = ROOK
    board[7][0] = ROOK
    board[0][6] = -KNIGHT
    board[0][1] = -KNIGHT
    board[7][6] = KNIGHT
    board[7][1] = KNIGHT
    board[0][2] = -BISHOP
    board[7][2] = BISHOP
    board[7][5] = BISHOP
    board[0][5] = -BISHOP
    board[0][4] = -KING
    board[7][4] = KING
    board[0][3] = -QUEEN
    board[7][3] = QUEEN
    return board

board = Board_Setup()



print_board(board)

