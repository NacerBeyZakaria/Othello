import pygame
from othello.constants import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, WHITE
from othello.board import Board
from othello.logic import Logic
from ai import get_ai_move
from minmax import get_minmax_move

pygame.init()
pygame.font.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Othello')


def main(game_mode="human"):
 
    run = True
    clock = pygame.time.Clock()
    board = Board()
    board.draw_initial_pieces()
    logic = Logic(board)
    endgame = False

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                if 300 <= x <= 420 and 615 <= y <= 675:
                    board.__init__()
                    board.draw_initial_pieces()
                    logic.current_turn = BLACK
                    endgame = False
                
                elif 450 <= x <= 570 and 615 <= y <= 675:
                    return  
                
                elif not endgame and y <= 600:
                    
                    if game_mode == "human" or logic.current_turn == BLACK:
                        row = y // SQUARE_SIZE
                        col = x // SQUARE_SIZE
                        logic.make_move(row, col)

        
        if game_mode == "ai" and not endgame and logic.current_turn == WHITE:
            valid_moves = logic.get_valid_moves(WHITE)
            ai_move = get_ai_move(valid_moves)
            if ai_move:
                row , col = ai_move
                logic.make_move(row,col)

        if game_mode =="minmax" and not endgame and logic.current_turn == WHITE:
            ai_move = get_minmax_move(board , logic ,WHITE, max_depth=2)
            if ai_move:
                row , col = ai_move
                logic.make_move(row , col)
                
        
        if not endgame:
            valid_moves = logic.get_valid_moves(logic.current_turn)
            if not valid_moves:
                logic.switch_turn()
                valid_moves = logic.get_valid_moves(logic.current_turn)
                if not valid_moves or board.is_board_full():
                    endgame = True
                    valid_moves = []
        else:
            valid_moves = []

        
        board.draw(WIN)
        
        
        pygame.draw.rect(WIN, (0, 0, 0), (0, 600, 600, 100))
        
        
        board.draw_valid_moves(WIN, valid_moves)

        
        font = pygame.font.Font(None, 28)
        small_font = pygame.font.Font(None, 24)
        
        
        black_score, white_score = board.get_scores()
        
        
        score_text = font.render(f"Black: {black_score}  White: {white_score}", True, (255, 255, 255))
        WIN.blit(score_text, (20, 615))

        
        if not endgame:
            
            turn_text = font.render(f"Turn: {'Black' if logic.current_turn == BLACK else 'White'}", True, WHITE)
            WIN.blit(turn_text, (20, 650))
        else:
            
            if black_score > white_score:
                winner = "Black Wins!"
                winner_color = (255, 255, 100)
            elif white_score > black_score:
                winner = "White Wins!"
                winner_color = (255, 255, 100)
            else:
                winner = "It's a Draw!"
                winner_color = (200, 200, 200)
            
            winner_text = font.render(winner, True, winner_color)
            WIN.blit(winner_text, (20, 650))

        
        restart_rect = pygame.Rect(300, 615, 120, 60)
        mouse_pos = pygame.mouse.get_pos()
        restart_hover = restart_rect.collidepoint(mouse_pos)
        
        
        restart_color = (100, 200, 255) if restart_hover else (40, 150, 200)
        
        
        pygame.draw.rect(WIN, restart_color, restart_rect, border_radius=10)
        pygame.draw.rect(WIN, (20, 90, 120), restart_rect, width=2, border_radius=10)
        
        restart_text = small_font.render("Restart", True, (0, 0, 0))
        restart_text_rect = restart_text.get_rect(center=restart_rect.center)
        WIN.blit(restart_text, restart_text_rect)

        
        menu_rect = pygame.Rect(450, 615, 120, 60)
        menu_hover = menu_rect.collidepoint(mouse_pos)
        
        
        menu_color = (255, 100, 100) if menu_hover else (200, 60, 60)
        
        
        pygame.draw.rect(WIN, menu_color, menu_rect, border_radius=10)
        pygame.draw.rect(WIN, (150, 30, 30), menu_rect, width=2, border_radius=10)
        
        menu_text = small_font.render("Menu", True, (255, 255, 255))
        menu_text_rect = menu_text.get_rect(center=menu_rect.center)
        WIN.blit(menu_text, menu_text_rect)

        
        pygame.display.update()


if __name__ == "__main__":
    main("humain")  
