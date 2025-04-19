from board import *

# Constants
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6


def is_on_board(row, col):
    return 0 <= row < 8 and 0 <= col < 8


#def print_board(board):
#    print("    0 1 2 3 4 5 6 7")
#    print("   ----------------")
 #   for row in range(8):
  #      print(row, "|", end=' ')
   #     for col in range(8):
    #        print(board[row][col], end=' ')
     #   print("|")
    #print("   ----------------")
    #print("    0 1 2 3 4 5 6 7")


def print_coordinates():
    for row in range(8):
        for col in range(8):
            print(f"({row}, {col})", end=" ")
        print()


def empty_board():
    board = [[0 for _ in range(8)] for _ in range(8)]

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
        if board is None:
            raise ValueError("Board cannot be None")

        sign = 1 if self.value > 0 else -1  # Positive = white, Negative = black

        # Sliding piece directions
        sliding_dirs = [
            (1, 0), (-1, 0), (0, -1), (0, 1),  # Rook & Queen
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Bishop & Queen
        ]

        for dr, dc in sliding_dirs:
            r, c = row + dr, col + dc
            while self.is_on_board(r, c):
                target = board[r][c]
                if target is None:
                    r += dr
                    c += dc
                    continue

                if target.value * sign > 0:  # Same color
                    break

                abs_val = abs(target.value)
                if abs(dr) == abs(dc) and abs_val in [3, 5]:  # Bishop or Queen
                    return True
                if (dr == 0 or dc == 0) and abs_val in [4, 5]:  # Rook or Queen
                    return True
                break  # Blocked

        # Knight moves
        knight_moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        for dr, dc in knight_moves:
            r, c = row + dr, col + dc
            if self.is_on_board(r, c):
                target = board[r][c]
                if target is not None and target.value == 2 * -sign:
                    return True

        # Pawn captures
        for dc in [-1, 1]:
            r, c = row - sign, col + dc
            if self.is_on_board(r, c):
                target = board[r][c]
                if target is not None and target.value == 1 * -sign:
                    return True

        return False

    def is_defended(self, board):
        sign = -1 if self.value > 0 else 1
        row, col = self.row, self.col

        # Straight and diagonal directions (for queen, rook, bishop)
        directions = [
            (1, 0), (-1, 0), (0, -1), (0, 1),  # Rook / Queen
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Bishop / Queen
        ]

        # Sliding pieces
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.is_on_board(r, c):
                if board is None:
                    break
                target = board[r][c]
                if target is None:
                    r += dr
                    c += dc
                    continue

                if (target.value * sign) < 0:  # Opponent piece
                    abs_val = abs(target.value)
                    if (abs(dr) == abs(dc) and abs_val in [3, 5]) or \
                            ((dr == 0 or dc == 0) and abs_val in [4, 5]):
                        return True
                break  # Blocked by any piece

        # Knight directions
        knight_moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        for dr, dc in knight_moves:
            r, c = row + dr, col + dc
            if self.is_on_board(r, c):
                if board is None:
                    break
                target = board[r][c]
                if target is not None and target.value == 2 * -sign:
                    return True

        # Pawn capture direction
        for dc in [-1, 1]:
            r, c = row - sign, col + dc
            if self.is_on_board(r, c):
                if board is None:
                    break
                target = board[r][c]
                if target is not None and target.value == 1 * -sign:
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

    def move(self, board, new_row, new_col, promotion=None):
        if not self.is_on_board(new_row, new_col):
            print("Move out of bounds.")
            return False

        target = board[new_row][new_col]

        # Optional: add legality checks, like not capturing own pieces
        if target is not None and (target.value * self.value > 0):
            print("Cannot capture your own piece.")
            return False

        # Update board: clear old position
        board[self.row][self.col] = None

        # Capture opponent (if any)
        if target is not None:
            print(f"Captured: {target}")

        # Move piece
        self.row = new_row
        self.col = new_col
        board[new_row][new_col] = self

        # === Pawn Promotion ===
        if abs(self.value) == 1:  # If it's a pawn
            if (self.value > 0 and new_row == 0) or (self.value < 0 and new_row == 7):
                sign = 1 if self.value > 0 else -1
                if promotion == "q":
                    board[new_row][new_col] = Queen(sign * 5, new_row, new_col)
                elif promotion == "r":
                    board[new_row][new_col] = Rook(sign * 4, new_row, new_col)
                elif promotion == "b":
                    board[new_row][new_col] = Bishop(sign * 3, new_row, new_col)
                elif promotion == "n":
                    board[new_row][new_col] = Knight(sign * 2, new_row, new_col)
                else:
                    board[new_row][new_col] = Queen(sign * 5, new_row, new_col)  # default to queen
                print("Pawn promoted!")

        return True


class King(Piece):


    def __init__(self, value, row, col, has_moved=False):
        super().__init__(value, row, col, has_moved)

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
    def is_check(self,board):
        if self.under_attack(board, self.row, self.col)== True:
            return True
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

def castling(board ):
    board[0][6] = King
    if King.is_check == False and King.has_moved==False:
        if board.under_attack[0][0] == False and Rook(board).has_moved==False:
            if Rook.legal_moves(board) == False :
                print('h')



