# Features & Functionality

- **Complete Othello Gameplay:** Experience the classic strategy board game with full rules implementation, including move validation, disc flipping, and game-over detection.
- **Human vs Human & Human vs AI:** Play locally against another person or challenge the built-in AI for a single-player experience.
- **Minimax AI (Depth = 2):** The game uses a Minimax algorithm set at search depth 2 for the AI opponent, allowing smart, strategic moves without excessive computation time.
- **Modular Code Architecture:** All logic is cleanly separated; board management, AI computation, and UI controls reside in their own files, making it easy to maintain, debug, or extend functionality.
- **Interactive GUI:** Uses a graphical user interface for smooth play. Make moves by clicking on board cells, view current scores, and get feedback for valid/invalid moves.
- **Menu System:** Includes a menu for selecting player mode (human vs human or vs AI), starting new games, and accessing game options.
- **Customizable AI Logic:** AI utilities make it easy to tweak difficulty (by changing the Minimax depth) or add new strategies, letting developers experiment or upgrade the opponent’s intelligence.
- **Game State Handling:** Utilities ensure correct turn handling, legal moves, win conditions, and scoring. The code automatically checks for available moves, passes turns when needed, and determines the winner at the end.
- **Replayability:** Play as black or white, restart games easily, and review results at game end.
- **Scalable & Extendable:** Architecture permits further enhancements, such as adding new AI agents, modifying board size, or integrating online play.
- **Pythonic Structure:** Designed to follow best practices – separate files for core logic (`othello.py`, `othello1.py`), AI (`ai.py`, `minmax.py`), and interface (`menu.py`, `main.py`), supporting professional code organization.

If you need more technical details or want further expansion on any feature/utilities, let me know!
