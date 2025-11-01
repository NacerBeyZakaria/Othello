import random

def get_ai_move(valid_moves):
    if not valid_moves:
        return None
    return random.choice(valid_moves)