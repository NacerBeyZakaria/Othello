from .constants import *
import pygame

class Piece:
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.calc_pos()

    def calc_pos(self):
        
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def draw(self,win):
        radius = SQUARE_SIZE // 2  - 8
        pygame.draw.circle(win,self.color,(self.x,self.y),radius)  