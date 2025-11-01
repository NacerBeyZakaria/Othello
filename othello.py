import tkinter as tk
import random
import math
import copy

BOARD_SIZE = 8

class StartMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Othello - Mode Selection")

        self.frame = tk.Frame(root, bg="darkgreen")
        self.frame.pack(fill="both", expand=True)

        title = tk.Label(self.frame, text="OTHELLO (Reversi)", font=("Arial", 24, "bold"), bg="darkgreen", fg="white")
        title.pack(pady=40)

        tk.Label(self.frame, text="Choose Game Mode:", font=("Arial", 16), bg="darkgreen", fg="white").pack(pady=10)

        tk.Button(self.frame, text="🧍 1 vs 1 Human", font=("Arial", 14), width=20, bg="#2e8b57", fg="white",
                  command=self.start_human).pack(pady=10)

        tk.Button(self.frame, text="🤖 1 vs AI (Easy)", font=("Arial", 14), width=20, bg="#4682b4", fg="white",
                  command=lambda: self.start_ai("easy")).pack(pady=5)

        tk.Button(self.frame, text="🤖 1 vs AI (Medium)", font=("Arial", 14), width=20, bg="#4169e1", fg="white",
                  command=lambda: self.start_ai("medium")).pack(pady=5)

        tk.Button(self.frame, text="🤖 1 vs AI (Hard)", font=("Arial", 14), width=20, bg="#00008b", fg="white",
                  command=lambda: self.start_ai("hard")).pack(pady=5)

    def start_human(self):
        self.frame.destroy()
        OthelloGame(self.root, mode="human")

    def start_ai(self, difficulty):
        self.frame.destroy()
        OthelloGame(self.root, mode="ai", difficulty=difficulty)


class OthelloGame:
    def __init__(self, root, mode="human", difficulty="easy"):
        self.root = root
        self.mode = mode
        self.difficulty = difficulty

        self.root.title(f"Othello - Mode: {mode.capitalize()} ({difficulty if mode=='ai' else ''})")

        self.cell_size = 50
        self.board_size_px = self.cell_size * BOARD_SIZE
        self.margin = 30

        canvas_size = self.board_size_px + self.margin * 2
        self.canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="darkgreen")
        self.canvas.pack()

        self.score_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=5)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=5)

        self.initialize_board()
        self.current_player = 1
        self.game_over = False

        self.canvas.bind("<Button-1>", self.handle_click)
        self.draw_board()

    def initialize_board(self):
        self.board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.board[3][3] = 2
        self.board[4][4] = 2
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.game_over = False

    def restart_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        StartMenu(self.root)

    def draw_board(self):
        self.canvas.delete("all")

        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                x0 = self.margin + j * self.cell_size
                y0 = self.margin + i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black")

                if self.board[i][j] == 1:
                    self.canvas.create_oval(x0+5, y0+5, x1-5, y1-5, fill="black")
                elif self.board[i][j] == 2:
                    self.canvas.create_oval(x0+5, y0+5, x1-5, y1-5, fill="white")

        for i in range(BOARD_SIZE):
            self.canvas.create_text(self.margin // 2, self.margin + i * self.cell_size + self.cell_size // 2,
                                    text=str(i+1), fill="white", font=("Arial", 12, "bold"))
            self.canvas.create_text(self.margin + self.board_size_px + self.margin // 2,
                                    self.margin + i * self.cell_size + self.cell_size // 2,
                                    text=str(i+1), fill="white", font=("Arial", 12, "bold"))
        for j in range(BOARD_SIZE):
            letter = chr(ord('A') + j)
            self.canvas.create_text(self.margin + j * self.cell_size + self.cell_size // 2, self.margin // 2,
                                    text=letter, fill="white", font=("Arial", 12, "bold"))
            self.canvas.create_text(self.margin + j * self.cell_size + self.cell_size // 2,
                                    self.margin + self.board_size_px + self.margin // 2,
                                    text=letter, fill="white", font=("Arial", 12, "bold"))

        if not self.game_over:
            for (r, c) in self.valid_moves(self.current_player):
                x0 = self.margin + c * self.cell_size + self.cell_size // 2 - 5
                y0 = self.margin + r * self.cell_size + self.cell_size // 2 - 5
                x1 = self.margin + c * self.cell_size + self.cell_size // 2 + 5
                y1 = self.margin + r * self.cell_size + self.cell_size // 2 + 5
                self.canvas.create_oval(x0, y0, x1, y1, fill="yellow")

        black_score, white_score = self.count_pieces()
        if self.game_over:
            if black_score > white_score:
                msg = f"⚫ Black wins! ({black_score} - {white_score})"
            elif white_score > black_score:
                msg = f"⚪ White wins! ({white_score} - {black_score})"
            else:
                msg = f"🤝 Draw! ({black_score} - {white_score})"
            self.score_label.config(text=msg)
        else:
            turn = "⚫ Black" if self.current_player == 1 else "⚪ White"
            self.score_label.config(text=f"⚫ Black: {black_score}   ⚪ White: {white_score}   | Turn: {turn}")

    def handle_click(self, event):
        if self.game_over:
            return

        col = (event.x - self.margin) // self.cell_size
        row = (event.y - self.margin) // self.cell_size
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            if (row, col) in self.valid_moves(self.current_player):
                self.make_move(row, col)
                self.current_player = 3 - self.current_player
                self.draw_board()

                if not self.valid_moves(self.current_player):
                    self.current_player = 3 - self.current_player
                    if not self.valid_moves(self.current_player):
                        self.game_over = True
                    self.draw_board()

                if self.mode == "ai" and self.current_player == 2 and not self.game_over:
                    self.root.after(300, self.ai_move)

    # -----------------------------------------------------------------
    # AI logic using Negamax + Alpha-Beta pruning
    # -----------------------------------------------------------------
    def ai_move(self):
        moves = self.valid_moves(2)
        if not moves:
            self.current_player = 1
            if not self.valid_moves(1):
                self.game_over = True
            self.draw_board()
            return

        if self.difficulty == "easy":
            move = random.choice(moves)
        else:
            depth = 3 if self.difficulty == "medium" else 5
            move, _ = self.best_move(copy.deepcopy(self.board), 2, depth)

        self.make_move(move[0], move[1])
        self.current_player = 1
        self.draw_board()

        if not self.valid_moves(1) and not self.game_over:
            self.root.after(300, self.ai_move)

    def best_move(self, board, player, depth):
        best_score = -math.inf
        best_move = None
        for move in self.valid_moves_on_board(board, player):
            new_board = copy.deepcopy(board)
            self.make_move_on_board(new_board, move[0], move[1], player)
            score = -self.negamax(new_board, depth-1, -math.inf, math.inf, 3-player)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move, best_score

    def negamax(self, board, depth, alpha, beta, player):
        if depth == 0 or self.is_game_over_board(board):
            return self.evaluate_board(board, player)

        max_eval = -math.inf
        moves = self.valid_moves_on_board(board, player)
        if not moves:
            return -self.negamax(board, depth-1, -beta, -alpha, 3-player)

        for move in moves:
            new_board = copy.deepcopy(board)
            self.make_move_on_board(new_board, move[0], move[1], player)
            eval = -self.negamax(new_board, depth-1, -beta, -alpha, 3-player)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return max_eval

    def evaluate_board(self, board, player):
        opponent = 3 - player
        score = 0

        corners = [(0,0),(0,7),(7,0),(7,7)]
        for (r,c) in corners:
            if board[r][c] == player:
                score += 25
            elif board[r][c] == opponent:
                score -= 25

        # Disc difference
        score += sum(1 if cell == player else -1 if cell == opponent else 0
                     for row in board for cell in row)

        # Mobility (number of possible moves)
        player_moves = len(self.valid_moves_on_board(board, player))
        opp_moves = len(self.valid_moves_on_board(board, opponent))
        score += 2 * (player_moves - opp_moves)

        return score

    # -----------------------------------------------------------------
    # Utilities for AI board simulation
    # -----------------------------------------------------------------
    def valid_moves_on_board(self, board, player):
        moves = []
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if board[r][c] == 0 and self.can_flip_on_board(board, r, c, player):
                    moves.append((r, c))
        return moves

    def can_flip_on_board(self, board, row, col, player):
        opponent = 3 - player
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            found = False
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == opponent:
                found = True
                r += dr; c += dc
            if found and 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                return True
        return False

    def make_move_on_board(self, board, row, col, player):
        board[row][col] = player
        opponent = 3 - player
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for dr, dc in directions:
            flips = []
            r, c = row+dr, col+dc
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == opponent:
                flips.append((r,c))
                r += dr; c += dc
            if flips and 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                for rr, cc in flips:
                    board[rr][cc] = player

    def is_game_over_board(self, board):
        return not self.valid_moves_on_board(board, 1) and not self.valid_moves_on_board(board, 2)

    # -----------------------------------------------------------------
    # Normal game functions (human moves)
    # -----------------------------------------------------------------
    def valid_moves(self, player):
        moves = []
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.board[r][c] == 0 and self.can_flip(r, c, player):
                    moves.append((r, c))
        return moves

    def can_flip(self, row, col, player):
        opponent = 3 - player
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            found_opponent = False
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == opponent:
                found_opponent = True
                r += dr; c += dc
            if found_opponent and 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == player:
                return True
        return False

    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        opponent = 3 - self.current_player
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for dr, dc in directions:
            pieces_to_flip = []
            r, c = row+dr, col+dc
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == opponent:
                pieces_to_flip.append((r,c))
                r += dr; c += dc
            if pieces_to_flip and 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == self.current_player:
                for rr, cc in pieces_to_flip:
                    self.board[rr][cc] = self.current_player

    def count_pieces(self):
        black = sum(row.count(1) for row in self.board)
        white = sum(row.count(2) for row in self.board)
        return black, white


if __name__ == "__main__":
    root = tk.Tk()
    StartMenu(root)
    root.mainloop()
