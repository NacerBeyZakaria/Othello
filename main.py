import pygame
from menu import show_menu
from othello1 import main as start_game

pygame.init()


while True:
    
    game_mode = show_menu()

    if game_mode == "human":
        
        start_game("human")
        
    elif game_mode == "ai":
        
        start_game("ai")
        
    elif game_mode == "minmax":
        start_game("minmax")    
    else:
        
        pygame.quit()
        break
