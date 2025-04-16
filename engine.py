# Constants
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

def is_on_board(row, col):
    return 0 <= row < 8 and 0 <= col < 8

def print_board(board):
    for row in range(8):
        print(8 - row, "|", end=' ')
        for col in range(8):
            print(board[row][col], end=' ')
        print("|")
    print("   ----------------")
    print("    a b c d e f g h")

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

class Piece:
    def __init__(self, value, cur_row, cur_col):
        self.value = value
        self.cur_row = cur_row
        self.cur_col = cur_col

    def is_on_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def collision(self, row, col, board):
        if not self.is_on_board(row, col):
            return False
        target = board[row][col]
        if target == 0:
            return False
        return (target > 0) == (self.value > 0)

class King(Piece):
    def legal_moves(self, board):
        legal_moves = []
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                nr = self.cur_row + dr
                nc = self.cur_col + dc
                if self.is_on_board(nr, nc) and not self.collision(nr, nc, board):
                    legal_moves.append((nr, nc))
        return legal_moves
class Bishop(Piece):
    def legal_moves(self, board):
        legal_moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonal directions

        for dr, dc in directions:
            r, c = self.cur_row, self.cur_col
            while True:
                r += dr
                c += dc
                if not self.is_on_board(r, c):
                    break

                target = board[r][c]
                if target == 0:
                    legal_moves.append((r, c))
                elif (target > 0) != (self.value > 0):
                    legal_moves.append((r, c)) #мне кажется надо так же указывать фигуру
                    break  #вражеская фигура
                else:
                    break  #своя фигура

        return legal_moves

class Rook(Piece):
    def legal_moves(self, board):
        legal_moves = []
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            r, c = self.cur_row, self.cur_col
            while True:
                r += dr
                c += dc
                if not self.is_on_board(r, c):
                    break

                target = board[r][c]
                if target == 0:
                    legal_moves.append((r, c))
                elif (target > 0) != (self.value > 0):
                    legal_moves.append((r, c)) #мне кажется надо так же указывать фигуру
                    break  #вражеская фигура
                else:
                    break  #своя фигура
        return legal_moves

class Queen(Piece):
    def legal_moves(self, board):
        legal_moves = []
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = self.cur_row, self.cur_col
            while True:
                r += dr
                c += dc
                if not self.is_on_board(r, c):
                    break

                target = board[r][c]
                if target == 0:
                    legal_moves.append((r, c))
                elif (target > 0) != (self.value > 0):
                    legal_moves.append((r, c)) #мне кажется надо так же указывать фигуру
                    break  #вражеская фигура
                else:
                    break  #своя фигура
        return legal_moves
 class Knight(Piece):
     def legal_moves(self, board):
         legal_moves = []


def main():
    board = Board_Setup()
    print_board(board)

    # Test: white king at 5, 5
    k = King(KING, 7, 7)
    print("Legal moves for king at (5,5):", k.legal_moves(board))

main()
