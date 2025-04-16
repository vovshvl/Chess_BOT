from engine import King
from engine import Queen
from engine import Bishop
from engine import Knight
from engine import Rook


class Board():
    def __init__(self):
        king_b = King(-6, 0, 4)
        king_w = King(6, 7, 4)

        rook_b = Rook(-4, 0, 0)
        rook_b_2 = Rook(-4, 0, 7)
        rook_w = Rook(4, 0, 0)
        rook_w_2 = Rook(4, 0, 7)
        self.list = []
        self.list.append(rook_b)
        for i in range(6):
            self.list.append(0)


    def print_board(self):
        print("  0 1 2 3 4 5 6 7")
        print("-----------------")
        for r in range(8):
            print(f"{r}|", end="")
            for c in range(8):
                piece = self.list[r]
                if piece:
                    print(f"{piece.value} ", end="")
                else:
                    print(". ", end="")
            print()
        print("-----------------")
