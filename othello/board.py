import pygame
from .constants import *
from .piece import *

class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        
        

    def draw_squares(self ,win) :
        pygame.draw.rect(win, GREEN, (0, 0, 600, 600))   
        for row in range(ROWS) :
            pygame.draw.line(win,DARK_GRAY,(0, row * SQUARE_SIZE),(WIDTH, row *SQUARE_SIZE),2)
            pygame.draw.line(win,DARK_GRAY,( row * SQUARE_SIZE, 0),(row *SQUARE_SIZE ,HEIGHT),2)
                # pygame.draw.rect(win, DARK_GRAY, (row * SQUARE_SIZE, col *SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                
    def draw_initial_pieces(self):
    
        self.board[3][3]  =  Piece(3,3,WHITE)
        self.board[4][4]  =  Piece(4,4,WHITE)
        self.board[3][4]  =  Piece(3,4,BLACK)
        self.board[4][3]  =  Piece(4,3,BLACK)
         

    def draw(self,win):  
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece:
                    piece.draw(win)   

    def get_scores(self):
        black_score = 0
        white_score = 0
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece:
                    if piece.color == BLACK:
                        black_score += 1
                    elif piece.color == WHITE:
                        white_score += 1
        return black_score,white_score         

    def draw_valid_moves(self, win ,moves):
        for row, col in moves:
            pygame.draw.circle(win ,YELLOW,(
                col * SQUARE_SIZE + SQUARE_SIZE // 2,
                row * SQUARE_SIZE + SQUARE_SIZE // 2),
                SQUARE_SIZE // 2 -18 ,4)         
    def is_board_full(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] is None:
                    return False
        return True                           