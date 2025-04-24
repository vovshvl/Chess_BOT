from best_move import move_leads_to_check
class Move:
    def __init__(self, from_square, to_square, piece_captured=None, promotion=None, castling_king=None, castling_queen = None, en_passant_captured_square=None, check=None):
        self.from_square = from_square    # (row, col)
        self.to_square = to_square
        self.piece_captured = piece_captured
        self.promotion = promotion
        self.castling_king = castling_king
        self.castling_queen = castling_queen
        self.en_passant_captured_square = en_passant_captured_square
        self.check = check
        self.move_score = 0

    def get_from_square(self):
        return self.from_square
    def get_to_square(self):
        return self.to_square

    def give_move_score(self):
        if self.check is not None:
            self.move_score += 1000
        if self.piece_captured is not None:
            self.move_score += 100
