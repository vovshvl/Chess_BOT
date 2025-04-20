import random
import timeit
from board import *
from engine import *

desirability_pawn = [10 for _ in range(64)]
desirability_rook = [50 for _ in range(64)]
desirability_queen = [90 for _ in range(64)]
desirability_king = [120 for _ in range(64)]
desirability_bishop = [30 for _ in range(64)]
desirability_knight = [30 for _ in range(64)]


class DesirabilityMap:
    def __init__(self, data=None):
        self.data = bytearray(data if data else [0] * 64)

    def get(self, row, col):
        """Get desirability score at (rank, file), where rank 0 = rank 1 in chess"""
        return self.data[row * 8 + col]

    def set(self, row, col, value):
        self.data[row * 8  + col] = min(max(value, 0), 127)

    def print_map(self):
        for row in range(7, -1, -1):  # print from rank 8 down to 1
            row = [f"{self.get(row, col):3}" for col in range(8)]
            print(" ".join(row))


# Create the map

board = initialise_board()
# Show the full map as a grid
print("Desirability Heatmap:")






def evaluate_piece_at(row, col, board,map):
    base_score = 1
    desirability_bonus = map.get(row, col)
    Piece= board[row][col]
    if Piece.is_attacked ==True and Piece.is_defended == False:
        return base_score -99
    possible_attacks_from_new_pos = Piece.legal_moves(board)['attacks']

    return base_score * desirability_bonus

def evaluate_board(board):
    board_score_white=0
    board_score_black = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == 0 or board[row][col] is None:
                continue
            if board[row][col] !=0 or board[row][col] is not None:
                Piece = board[row][col]
                if Piece.value>0:
                    match Piece.value:
                        case 1:
                            map = DesirabilityMap(desirability_pawn)
                        case 2:
                            map = DesirabilityMap(desirability_knight)
                        case 3:
                            map = DesirabilityMap(desirability_bishop)
                        case 4:
                            map = DesirabilityMap(desirability_rook)
                        case 5:
                            map = DesirabilityMap(desirability_queen)
                        case 6:
                            map = DesirabilityMap(desirability_king)
                    board_score_white += evaluate_piece_at(row, col, board, map)
                else:
                    match Piece.value:
                        case -1:
                            map = DesirabilityMap(desirability_pawn)
                        case -2:
                            map = DesirabilityMap(desirability_knight)
                        case -3:
                            map = DesirabilityMap(desirability_bishop)
                        case -4:
                            map = DesirabilityMap(desirability_rook)
                        case -5:
                            map = DesirabilityMap(desirability_queen)
                        case -6:
                            map = DesirabilityMap(desirability_king)
                    board_score_black+=evaluate_piece_at(row, col, board, map)
    return board_score_white, board_score_black
def all_moves(board):
    all_moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece in (None, 0):
                continue  # Skip empty squares

            result = piece.legal_moves(board)

            if isinstance(result, dict) and isinstance(result.get('legal_moves'), list):
                all_moves.extend(result['legal_moves'])
            else:
                print(f"Warning: piece at ({row}, {col}) returned malformed legal_moves")
    return all_moves
print(all_moves(board))

def minmax(board, all_moves, depth, alpha, beta, max_player):
    #Alpha–beta pruning
    if max_player == True:
        max_eval = -float('inf')
        for move in all_moves:
            new_board = move(board, move[0], move[1])
            eval = minmax(board, all_moves, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval




print(evaluate_board(board))

duration = timeit.timeit(lambda: evaluate_board(board), number=64000)
print(f"Time for 1,000,000 asks: {duration:.4f} seconds")
