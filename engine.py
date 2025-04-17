

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
    print("    0 1 2 3 4 5 6 7")
    print("   ----------------")
    for row in range(8):
        print(row, "|", end=' ')
        for col in range(8):
            print(board[row][col], end=' ')
        print("|")
    print("   ----------------")
    print("    0 1 2 3 4 5 6 7")


def print_coordinates():
    for row in range(8):
        for col in range(8):
            print(f"({row}, {col})", end=" ")
        print()


def empty_board():
    board = [[0 for _ in range(8)] for _ in range(8)]

    return board


def board_setup():
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

    def __init__(self, value, row, col, has_moved=False):
        self.value = value  # type (1=Pawn, 2=Knight, etc.)
        self.row = row
        self.col = col
        self.has_moved = has_moved
        self.is_white = value > 0

    def position(self):
        return self.row, self.col

    def is_on_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def under_attack(self, board, row, col):
        directions =[(1, 0), (-1, 0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1),(2, 1), (2, -1), (1, -2), (1, 2), (-1, 2), (-1, -2), (-2, -1), (-2, 1)]
        sign = 1 if self.value > 0 else -1
        for dr, dc in directions:
            r, c = row, col
            while True:
                r += dr
                c += dc
                if not self.is_on_board(r, c):
                    break
                target = board[r][c]
                if sign > 0 and target > 0:
                    break
                if sign < 0 and target < 0:
                    break
                if abs(dr) == 1 and abs(dc) == 1 and target in (3, 5)*sign:
                    return True
                if (dr == 0 or dc == 0) and target in (4, 5)*sign:
                    return True
                if (abs(dr), abs(dc)) in [(2, 1), (1, 2)] and target == 2*sign:
                    return True
                if abs(dc) == 1 and dr == -1*sign and target == 1*sign:
                    return True
        return False

    def is_defended(self, board, row, col):
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1), (2, 1), (2, -1), (1, -2),
                      (1, 2), (-1, 2), (-1, -2), (-2, -1), (-2, 1)]
        sign = -1 if self.value > 0 else 1
        for dr, dc in directions:
            r, c = row, col
            while True:
                r += dr
                c += dc
                if not self.is_on_board(r, c):
                    break
                target = board[r][c]
                if sign > 0 and target < 0:
                    break
                if sign < 0 and target > 0:
                    break

                if abs(dr) == 1 and abs(dc) == 1 and target in (3, 5) * sign:
                        return True
                if (dr == 0 or dc == 0) and target in (4, 5) * sign:
                        return True
                if (abs(dr), abs(dc)) in [(2, 1), (1, 2)] and target == 2 * sign:
                        return True
                if abs(dc) == 1 and dr == -1 * sign and target == 1 * sign:
                        return True
        return False

    def directionscheck(self, directions, board):
        legal_moves = []
        for dr, dc in directions:
            r, c = self.row, self.col
            while True:
                r += dr
                c += dc
                if not self.is_on_board(r, c):
                    break

                target = board[r][c]
                if target == 0:
                    legal_moves.append((r, c))
                elif (target > 0) != (self.value > 0):
                    legal_moves.append((r, c))  # мне кажется надо так же указывать фигуру
                    break  # вражеская фигура
                else:
                    break  # своя фигура
        return legal_moves

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
                nr = self.  row + dr
                nc = self.  col + dc
                if self.is_on_board(nr, nc) and not self.collision(nr, nc, board):
                    legal_moves.append((nr, nc))
        return legal_moves

class Bishop(Piece):
    def legal_moves(self, board):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonal directions
        legal_moves = self.directionscheck(directions, board)
        return legal_moves


class Rook(Piece):
    def legal_moves(self, board):
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        legal_moves = self.directionscheck(directions, board)
        return legal_moves


class Queen(Piece):
    def legal_moves(self, board):
        legal_moves = []
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]
        legal_moves = self.directionscheck(directions, board)
        return legal_moves


class Knight(Piece):
     def legal_moves(self, board):
         directions = [(2, 1), (2, -1), (1, -2), (1, 2), (-1, 2), (-1, -2), (-2, -1), (-2, 1)]
         legal_moves = self.directionscheck(directions, board)
         return legal_moves


class Pawn(Piece):
    def legal_moves(self, board):
        legal_moves = []
        if self.value >0:
            directions = [(-1, 0)]
            attacks = [(-1, 1), (-1, -1)]
        else:
            directions = [(1, 0)]
            attacks = [(1, 1),(1, -1)]
        for dr, dc in directions:
            r, c = self.row, self.  col
            while True:
                r += dr
                c += dc
                if not self.is_on_board(r, c):
                    break
                target = board[r][c]
                if target == 0:
                    legal_moves.append((r, c))
                else:
                    break
        for dr, dc in attacks:
            r, c = self.row, self.  col
            while True:
                r += dr
                c += dc
                if not self.is_on_board(r, c):
                    break
                target = board[r][c]
                if self.value > 0:
                    if target < 0:
                        legal_moves.append((r, c))
                else:
                    if target > 0:
                        legal_moves.append((r, c))


        return legal_moves


def main():

    board = empty_board()
    print_board(board)
    board = board_setup()
    # Test: white king at 5, 5

    #print_board(board)
    #print(b.legal_moves(board))
    print_coordinates()


main()
