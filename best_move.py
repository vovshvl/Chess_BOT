from engine import *

desirability_pawn_black =bytes ([
    0, 0, 0, 0, 0, 0, 0, 0,
    15, 15, 15, 20, 20, 15, 15, 15,
    18, 18, 20, 25, 25, 20, 18, 18,
    22, 22, 25, 30, 30, 25, 22, 22,
    23, 23, 26, 32, 32, 26, 23, 23,
    24, 24, 28, 35, 35, 28, 24, 24,
    40, 40, 45, 45, 45, 45, 40, 40,
    90,  90, 90, 90, 90, 90,  90, 90
])
desirability_rook_black =bytes ( [
    50, 50, 52, 54, 54, 52, 50, 50,
    52, 54, 56, 58, 58, 56, 54, 52,
    52, 54, 56, 58, 58, 56, 54, 52,
    53, 55, 57, 55, 55, 57, 55, 53,
    53, 55, 57, 55, 55, 57, 55, 53,
    52, 54, 56, 58, 58, 56, 54, 52,
    52, 52, 52, 52, 52, 52, 52, 52,
    50, 50, 50, 50, 50, 50, 50, 50
])
desirability_queen_black = bytes ( [
    88, 88, 89, 90, 90, 89, 88, 88,
    88, 90, 92, 94, 94, 92, 90, 88,
    89, 92, 95, 100, 100, 95, 92, 89,
    90, 94, 100, 105, 105, 100, 94, 90,
    90, 94, 100, 105, 105, 100, 94, 90,
    89, 92, 95, 100, 100, 95, 92, 89,
    88, 90, 92, 94, 94, 92, 90, 88,
    88, 88, 89, 90, 90, 89, 88, 88
])
desirability_king_black = bytes ([
    118, 127, 118, 117, 117, 124, 118, 118,
    116, 117, 118, 110, 110, 118, 117, 116,
    115, 116, 117, 118, 118, 117, 116, 115,
    114, 115, 116, 117, 117, 116, 115, 114,
    113, 114, 115, 116, 116, 115, 114, 113,
    112, 113, 114, 115, 115, 114, 113, 112,
    111, 112, 113, 114, 114, 113, 112, 111,
    110, 111, 112, 113, 113, 112, 111, 110
])
desirability_bishop_black = bytes ([
    20, 22, 25, 30, 30, 25, 22, 20,
    22, 26, 30, 35, 35, 30, 26, 22,
    25, 30, 35, 40, 40, 35, 30, 25,
    30, 35, 40, 50, 50, 40, 35, 30,
    30, 35, 40, 50, 50, 40, 35, 30,
    25, 30, 35, 40, 40, 35, 30, 25,
    22, 26, 30, 35, 35, 30, 26, 22,
    20, 22, 25, 30, 30, 25, 22, 20
])
desirability_knight_black = bytes ([
    15, 20, 25, 30, 30, 25, 20, 15,
    20, 30, 35, 40, 40, 35, 30, 20,
    25, 35, 45, 50, 50, 45, 35, 25,
    30, 40, 50, 55, 55, 50, 40, 30,
    30, 40, 50, 55, 55, 50, 40, 30,
    25, 35, 45, 50, 50, 45, 35, 25,
    20, 30, 35, 40, 40, 35, 30, 20,
    15, 20, 25, 30, 30, 25, 20, 15
])
desirability_pawn_white = bytes ([
    90, 90, 90, 90, 90, 90, 90, 90,
    40, 40, 45, 45, 45, 45, 40, 40,
    24, 24, 28, 35, 35, 28, 24, 24,
    23, 23, 26, 32, 32, 26, 23, 23,
    22, 22, 25, 30, 30, 25, 22, 22,
    18, 18, 20, 25, 25, 20, 18, 18,
    15, 15, 15, 20, 20, 15, 15, 15,
    0, 0, 0, 0, 0, 0, 0, 0])
desirability_rook_white = bytes ([
    50, 50, 50, 50, 50, 50, 50, 50,
    52, 52, 52, 52, 52, 52, 52, 52,
    52, 54, 56, 58, 58, 56, 54, 52,
    53, 55, 57, 60, 60, 57, 55, 53,
    53, 55, 57, 60, 60, 57, 55, 53,
    52, 54, 56, 58, 58, 56, 54, 52,
    52, 54, 56, 58, 58, 56, 54, 52,
    50, 50, 52, 54, 54, 52, 50, 50])
desirability_queen_white = bytes ([
    88, 88, 89, 90, 90, 89, 88, 88,
    88, 90, 92, 94, 94, 92, 90, 88,
    89, 92, 95, 100, 100, 95, 92, 89,
    90, 94, 100, 105, 105, 100, 94, 90,
    90, 94, 100, 105, 105, 100, 94, 90,
    89, 92, 95, 100, 100, 95, 92, 89,
    88, 90, 92, 94, 94, 92, 90, 88,
    88, 88, 89, 90, 90, 89, 88, 88])
desirability_king_white =bytes ( [
    110, 111, 112, 113, 113, 112, 111, 110,
    111, 112, 113, 114, 114, 113, 112, 111,
    112, 113, 114, 115, 115, 114, 113, 112,
    113, 114, 115, 116, 116, 115, 114, 113,
    114, 115, 116, 117, 117, 116, 115, 114,
    115, 116, 117, 118, 118, 117, 116, 115,
    116, 117, 118, 110, 110, 118, 117, 116,
    118, 118, 125, 117, 117, 118, 127, 118])
desirability_bishop_white = bytes ([
    20, 22, 25, 30, 30, 25, 22, 20,
    22, 26, 30, 35, 35, 30, 26, 22,
    25, 30, 35, 40, 40, 35, 30, 25,
    30, 35, 40, 50, 50, 40, 35, 30,
    30, 35, 40, 50, 50, 40, 35, 30,
    25, 30, 35, 40, 40, 35, 30, 25,
    22, 26, 30, 35, 35, 30, 26, 22,
    20, 22, 25, 30, 30, 25, 22, 20])
desirability_knight_white =bytes ( [
    15, 20, 25, 30, 30, 25, 20, 15,
    20, 30, 35, 40, 40, 35, 30, 20,
    25, 35, 45, 50, 50, 45, 35, 25,
    30, 40, 50, 60, 60, 50, 40, 30,
    30, 40, 50, 60, 60, 50, 40, 30,
    25, 35, 45, 50, 50, 45, 35, 25,
    20, 30, 35, 40, 40, 35, 30, 20,
    15, 20, 25, 30, 30, 25, 20, 15])

def mirror_for_black(white_table):
    return sum(
        [white_table[i * 8:(i + 1) * 8] for i in reversed(range(8))],
        []
    )
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

#board = initialise_board()
# Show the full map as a grid

desirability_maps = {
    1: DesirabilityMap(desirability_pawn_white),
    2: DesirabilityMap(desirability_knight_white),
    3: DesirabilityMap(desirability_bishop_white),
    4: DesirabilityMap(desirability_rook_white),
    5: DesirabilityMap(desirability_queen_white),
    6: DesirabilityMap(desirability_king_white),
    -1: DesirabilityMap(desirability_pawn_black),
    -2: DesirabilityMap(desirability_knight_black),
    -3: DesirabilityMap(desirability_bishop_black),
    -4: DesirabilityMap(desirability_rook_black),
    -5: DesirabilityMap(desirability_queen_black),
    -6: DesirabilityMap(desirability_king_black),
}

def move_leads_to_check(board, move, king_square):
    make_move(board, move)
    if board[king_square[0]][king_square[1]].is_check(board):
        move.check = True
        undo_move(board, move)
        return True
    else:
        move.check = False
        undo_move(board, move)
        return False

def sort_moves(board, all_moves, king_square):
    for move in all_moves:
        move_leads_to_check(board, move, king_square)
        move.give_move_score()
    all_moves.sort(key=lambda move: move.move_score, reverse=True)
    return all_moves


def evaluate_piece_at(piece,row,col, board,map):
    base_score = 1
    desirability_bonus = map.get(row, col)
    if piece.value == -6:
        if piece.is_attacked(board, piece.row, piece.col):
            base_score = -1
            if piece.is_checkmate(board):
                base_score = -1000
        return base_score * desirability_bonus


    if piece.value == -6:
        if piece.has_castled == True:
            base_score += 50
        if piece.is_attacked(board,piece.row,piece.col):
            base_score = -1
            if piece.is_checkmate(board):
                base_score = -1000
        return base_score*desirability_bonus
    if piece.is_attacked(board,row,col) == True and piece.is_defended(board) == False:
        return -base_score* desirability_bonus+5
    possible_attacks_from_new_pos = piece.legal_moves(board)['attacks']

    return base_score * desirability_bonus


def evaluate_board(board):
    board_score_white = 0
    board_score_black = 0
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if not piece:
                continue
            if piece.value>0:
                    map = desirability_maps[piece.value]
                    board_score_white += evaluate_piece_at(piece,row,col, board, map)
            else:
                    map = desirability_maps[piece.value]
                    board_score_black+=evaluate_piece_at(piece,row,col, board, map)
    return board_score_white - board_score_black
#possible optimization with limiting variables to 16 pieces as there cant be more in the game
def all_moves(board, color):
    all_moves = []
    i=0
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if i==16:
                return all_moves
            if piece in (None, 0):
                continue  # Skip empty squares
            if color>0:
                if piece.value<0: 
                    break
            else:
                if piece.value>0:
                    break
            result = piece.legal_moves(board)
            i=i+1

            if isinstance(result, dict) and isinstance(result.get('legal_moves'), list):
                all_moves.extend(result['legal_moves'])
            else:
                print(f"Warning: piece at ({row}, {col}) returned malformed legal_moves")
    return all_moves

def minmax(board, moves, depth, alpha, beta, turn):
    #Alpha–beta pruning
    best_move = None

    if depth == 0 or not moves:
        return evaluate_board(board), best_move

    if turn > 0:
        max_eval = -float('inf')
        for move in moves:

            make_move(board, move)
            #if not made_move:
               # break

            if depth != 1:
                possible_moves = all_moves(board, -turn)
            else: possible_moves = []
            current_eval, _ = minmax(board, possible_moves, depth - 1, alpha, beta, -turn)

            undo_move(board, move)


            if current_eval > max_eval:
                max_eval = current_eval
                best_move = move
            alpha = max(alpha, current_eval)
            if beta <= alpha:
                break

        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move in moves:
            make_move(board, move)


            possible_moves = all_moves(board, -turn)
            current_eval, _ = minmax(board, possible_moves, depth - 1, alpha, beta, -turn)

            undo_move(board, move)



            if current_eval < min_eval:
                min_eval = current_eval
                best_move = move
            beta = min(beta, current_eval)
            if beta <= alpha:
                break
        return min_eval, best_move



