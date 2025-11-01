import pygame
from othello.constants import WIDTH, HEIGHT, BLACK, WHITE

pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Othello - Menu')


def draw_menu(win):
    
    win.fill((30, 30, 30))  
    
    
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("OTHELLO", True, (50, 200, 200))
    title_rect = title_text.get_rect(center=(WIDTH // 2, 150))
    win.blit(title_text, title_rect)
    
    button_font = pygame.font.Font(None, 36)
    
    
    human_button = pygame.Rect(WIDTH // 2 - 150, 300, 300, 60)
    mouse_pos = pygame.mouse.get_pos()
    human_hover = human_button.collidepoint(mouse_pos)
    human_color = (80, 200, 255) if human_hover else (60, 150, 200)
    
    pygame.draw.rect(win, human_color, human_button, border_radius=10)
    pygame.draw.rect(win, (40, 120, 160), human_button, width=3, border_radius=10)
    
    human_text = button_font.render("1v1 Human", True, BLACK)
    human_text_rect = human_text.get_rect(center=human_button.center)
    win.blit(human_text, human_text_rect)
    
    
    ai_button = pygame.Rect(WIDTH // 2 - 150, 400, 300, 60)
    ai_hover = ai_button.collidepoint(mouse_pos)
    ai_color = (80, 255, 150) if ai_hover else (60, 200, 120)
    
    pygame.draw.rect(win, ai_color, ai_button, border_radius=10)
    pygame.draw.rect(win, (40, 160, 80), ai_button, width=3, border_radius=10)
    
    ai_text = button_font.render("1v1 AI (random)", True, BLACK)
    ai_text_rect = ai_text.get_rect(center=ai_button.center)
    win.blit(ai_text, ai_text_rect)

    minmax_button = pygame.Rect(WIDTH // 2 - 150, 500 , 300,60)
    minmax_hover = minmax_button.collidepoint(mouse_pos)
    minmax_color = (81 , 4 ,1) if minmax_hover else (196 , 44 , 33)

    pygame.draw.rect(win , minmax_color, minmax_button, border_radius=10)
    pygame.draw.rect(win , (120, 0, 24),minmax_button ,width=3, border_radius=10)

    minmax_text = button_font.render("1v1 AI (MinMax)", True,BLACK)
    minmax_text_rect = minmax_text.get_rect(center= minmax_button.center)
    win.blit(minmax_text,minmax_text_rect)
    
    
    instruction_font = pygame.font.Font(None, 24)
    instruction_text = instruction_font.render("Click to select game mode", True, (150, 150, 150))
    instruction_rect = instruction_text.get_rect(center=(WIDTH // 2, 625))
    win.blit(instruction_text, instruction_rect)
    
    return human_button, ai_button , minmax_button


def show_menu():
    
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        
        human_button, ai_button, minmax_button = draw_menu(WIN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                if human_button.collidepoint(x, y):
                    return "human"  
                
                if ai_button.collidepoint(x, y):
                    return "ai"  
                
                if minmax_button.collidepoint(x,y):
                    return "minmax"
        
        pygame.display.update()
    
    return None


if __name__ == "__main__":
    mode = show_menu()
    print(f"Selected mode: {mode}")
    pygame.quit()
