import copy 
import random
from othello.constants import BLACK, WHITE
from othello.board import *

def evaluate_board(board , color):
    black_score, white_score = board.get_scores()
    if color == BLACK:
        return black_score - white_score
    else:
        return white_score - black_score
    
def get_opponent(color):
    return WHITE if color == BLACK else BLACK  

def get_minmax_move(board, logic, color, max_depth=2):
    valid_moves = logic.get_valid_moves(color)
    if not valid_moves:
        return None

    move_scores = []      
    best_score = float('-inf')
    best_moves = []

    for move in valid_moves:
        temp_board = copy.deepcopy(board)
        temp_logic = copy.deepcopy(logic)
        temp_logic.board = temp_board
        temp_logic.make_move(move[0], move[1])

        score, result_board = minmax(temp_board, temp_logic, get_opponent(color), 1, max_depth, False, color)
        black_s, white_s = result_board.get_scores()
        move_scores.append((move, score, black_s, white_s))
        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)

    
    print("Moves | Score | Counts (B-W):", " || ".join(f"{mv}:{sc} ({b}-{w})" for mv, sc, b, w in move_scores))
    best_move = random.choice(best_moves)

    bm_tuple = next((t for t in move_scores if t[0] == best_move), None)
    if bm_tuple:
        mv, sc, b, w = bm_tuple
        if color == BLACK:
            formula = f"{b} - {w}"
        else:
            formula = f"{w} - {b}"
        print(f"Best move: {mv}, Scores (black, white): ({b}, {w}) = {formula}, Result: {sc}")

    return best_move


def minmax(board, logic, color, depth, max_depth, maximizing, ai_color):
    if depth == max_depth:
        
        return evaluate_board(board, ai_color), board

    valid_moves = logic.get_valid_moves(color)
    if not valid_moves:
        return minmax(board, logic, get_opponent(color), depth+1, max_depth, not maximizing, ai_color)
    
    if maximizing:
        best_score = float('-inf')
        best_board = None
        for move in valid_moves:
            temp_board = copy.deepcopy(board)
            temp_logic = copy.deepcopy(logic)
            temp_logic.board = temp_board
            temp_logic.make_move(move[0], move[1])
            score, result_board = minmax(temp_board, temp_logic, get_opponent(color), depth+1, max_depth, False, ai_color)
            if score > best_score:
                best_score = score
                best_board = result_board
        return best_score, best_board
    else:
        best_score = float('inf')
        best_board = None
        for move in valid_moves:
            temp_board = copy.deepcopy(board)
            temp_logic = copy.deepcopy(logic)
            temp_logic.board = temp_board
            temp_logic.make_move(move[0], move[1])
            score, result_board = minmax(temp_board, temp_logic, get_opponent(color), depth+1, max_depth, True, ai_color)
            if score < best_score:
                best_score = score
                best_board = result_board
        return best_score, best_board
