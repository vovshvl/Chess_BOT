from Move import Move
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

    def is_attacked(self, board, row, col):


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

    def collision(self, row, col, board):
        if not self.is_on_board(row, col):
            return False
        target = board[row][col]
        if target == 0 or target is None:
            return False
        return (target.value > 0) == (self.value > 0)

    def directionscheck(self, directions, board):
        legal_moves = []
        attacks =[]
        for dr, dc in directions:
            r, c = self.row, self.col
            while True:
                r += dr
                c += dc
                if not self.is_on_board(r, c):
                    break

                target = board[r][c]
                if target == 0 or target is None:
                    legal_moves.append(Move((self.row, self.col), (r,c)))
                elif (target.value > 0) != (self.value > 0):
                    legal_moves.append(Move((self.row, self.col), (r,c)))
                    attacks.append(Move((self.row, self.col), (r,c)))
                    break  # вражеская фигура
                else:
                    break  # своя фигура
        return {
            'legal_moves': legal_moves,
            'attacks': attacks
        }

    def move(self, board, new_row, new_col, promotion=None, turn=1):
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
        self.has_moved = True
        board[new_row][new_col] = self
        turn = turn * -1
        # === Pawn Promotion ===
        """
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
        """


        #move_history.append(((new_row, ),()))
        return True

class Pawn(Piece):
    def legal_moves(self, board):
        legal_moves = []
        if self.value >0:
            if self.row == 1:
                directions = [(-1, 0), (-2,0)]
            else:
                directions = [(-1, 0)]
            attack_direction= [(-1, 1), (-1, -1)]
        else:
            if self.row == 6:
                directions = [(1, 0), (2,0)]
            else:
                directions = [(1, 0)]
            attack_direction = [(1, 1),(1, -1)]
        for dr, dc in directions:
            r, c = self.row, self.  col
            for i in range(2):
                r += dr
                c += dc

                if not self.is_on_board(r, c):
                    break
                target = board[r][c]
                if target == 0 or target is None:
                    legal_moves.append(Move((self.row, self.col), (r,c)))
                else:
                    break
        attacks =[]
        for dr, dc in attack_direction:
            r, c = self.row, self.col
            while True:
                r += dr
                c += dc
                if not self.is_on_board(r, c):
                    break
                target = board[r][c]
                if target == 0 or target is None:
                    break
                if self.value > 0:
                    if target < 0:
                        legal_moves.append(Move((self.row, self.col), (r,c)))
                        attacks.append(Move((self.row, self.col), (r,c)))

                else:
                    if target.value > 0:
                        legal_moves.append(Move((self.row, self.col), (r,c)))
                        attacks.append(Move((self.row, self.col), (r,c)))

        return {
            'legal_moves': legal_moves,
            'attacks': attacks
        }

class Rook(Piece):
    def legal_moves(self, board):
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        result = self.directionscheck(directions, board)
        legal_moves = result['legal_moves']
        attacks = result['attacks']
        return {
            'legal_moves': legal_moves,
            'attacks': attacks
        }

class Bishop(Piece):
    def legal_moves(self, board):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonal directions
        result = self.directionscheck(directions, board)
        legal_moves = result['legal_moves']
        attacks = result['attacks']
        return {
            'legal_moves': legal_moves,
            'attacks': attacks
        }


class Knight(Piece):
    def legal_moves(self, board):
        directions = [(2, 1), (2, -1), (1, -2), (1, 2), (-1, 2), (-1, -2), (-2, -1), (-2, 1)]
        legal_moves = []
        attacks = []
        for dr, dc in directions:
            r = self.row + dr
            c = self.col + dc

            if self.is_on_board(r, c):
                target = board[r][c]
                if target == 0 or target is None:
                    legal_moves.append(Move((self.row, self.col), (r, c)))
                elif (target.value > 0) != (self.value > 0):
                    legal_moves.append(Move((self.row, self.col), (r, c)))
                    attacks.append(Move((self.row, self.col), (r, c)))
        return {
            'legal_moves': legal_moves,
            'attacks': attacks
        }

class Queen(Piece):
    def legal_moves(self, board):

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]

        result = self.directionscheck(directions, board)
        legal_moves = result['legal_moves']
        attacks = result['attacks']
        return {
            'legal_moves': legal_moves,
            'attacks': attacks
        }

class King(Piece):
    def legal_moves(self, board):
        legal_moves = []
        attacks = []

        # Normal king moves
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                nr = self.row + dr
                nc = self.col + dc

                if not self.is_on_board(nr, nc):
                    continue

                target = board[nr][nc]

                if target is None or target == 0:
                    legal_moves.append(Move((self.row, self.col), (nr,nc)))
                elif (target.value * self.value) < 0:  # Enemy piece
                    legal_moves.append((nr, nc))
                    attacks.append(Move((self.row, self.col), (nr,nc)))

        # Castling
        if not self.has_moved:
            sign = 1 if self.value > 0 else -1
            row = self.row

            # Kingside castling
            if (self.col + 2 < 8 and
                    board[row][self.col + 1] in [0, None] and
                    board[row][self.col + 2] in [0, None]):
                kingside_rook = board[row][7]
                if (isinstance(kingside_rook, Rook) and
                        not kingside_rook.has_moved and
                        not self.is_attacked(board, row, self.col + 1) and
                        not self.is_attacked(board, row, self.col + 2)):
                    legal_moves.append(Move((self.row, self.col), (row,self.col + 2)))

            # Queenside castling
            if (self.col - 2 >= 0 and
                    board[row][self.col - 1] in [0, None] and
                    board[row][self.col - 2] in [0, None] and
                    board[row][self.col - 3] in [0, None]):
                queenside_rook = board[row][0]
                if (isinstance(queenside_rook, Rook) and
                        not queenside_rook.has_moved and
                        not self.is_attacked(board, row, self.col - 1) and
                        not self.is_attacked(board, row, self.col - 2)):
                    legal_moves.append(Move((self.row, self.col), (row,self.col - 2)))

        return {
            'legal_moves': legal_moves,
            'attacks': attacks
        }

    def is_check(self, board):
        if self.is_attacked(board, self.row, self.col) == True:
            return True

