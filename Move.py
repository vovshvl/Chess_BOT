class Move:
    def __init__(self, from_square, to_square, piece_moved, piece_captured=None, promotion=None, castling=None, en_passant_captured_square=None):
        self.from_square = from_square    # (row, col)
        self.to_square = to_square
        self.piece_moved = piece_moved
        self.piece_captured = piece_captured
        self.promotion = promotion
        self.castling = castling
        self.en_passant_captured_square = en_passant_captured_square

    def __repr__(self): # for debugging
        rep = f"{self.piece_moved} from {self.from_square} to {self.to_square}"
        if self.piece_captured:
            rep += f" (captures {self.piece_captured})"
        if self.promotion:
            rep += f" (promotes to {self.promotion})"
        if self.castling:
            rep += f" (castling {self.castling})"
        if self.en_passant_captured_square:
            rep += f" (en passant capture at {self.en_passant_captured_square})"
        return rep