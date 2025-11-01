import pygame
from .constants import *
from .piece import *

DIRECTIONS = [
    (-1,-1),(-1,0),(-1,1),(0,1),
    (0,-1),(1,0),(1,1),(1,-1)
]

class Logic:
    def __init__(self,board):
        self.board = board
        self.current_turn = BLACK

    def get_valid_moves(self,color):
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_valid_move(row,col,color):
                    moves.append((row,col))
        return moves

    def is_valid_move(self,row,col,color):
        if self.board.board[row][col] is not None:
                return False

        opponent = WHITE if color == BLACK else BLACK
        valid =False

        for dr,dc in DIRECTIONS:
            r,c = row +dr , col +dc
            found_opponent = False

            while 0<= r < ROWS and 0<= c< COLS:
                piece = self.board.board[r][c]
                if piece is None:
                    break
                if piece.color == opponent:
                    found_opponent = True
                    r = r+ dr
                    c = c+dc
                elif piece.color == color:
                    if found_opponent :
                        valid = True
                    break
                else :
                    break
        return valid
    def make_move(self,row,col) :
        if not self.is_valid_move(row,col,self.current_turn):
            return False
        self.board.board[row][col] = Piece(row,col,self.current_turn)
        self.flip_pieces(row,col)
        self.switch_turn()
        return True

    def flip_pieces(self,row,col):
        opponent = WHITE if self.current_turn == BLACK else BLACK
        for dr , dc in DIRECTIONS:
            flip = []
            r,c = row +dr , col +dc
            while 0<= r <ROWS and 0 <= c < COLS :
                piece = self.board.board[r][c]
                if piece is None:
                    break
                if piece.color == opponent:
                    flip.append(piece)
                    r = r + dr
                    c = c + dc      
                elif piece.color == self.current_turn:
                    for p in flip: 
                        p.color = self.current_turn
                    break
                else:
                    break
    def switch_turn(self):
        self.current_turn = WHITE if self.current_turn == BLACK else BLACK                
                                       