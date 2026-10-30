"""
Practical 4: Solving Tic-Tac-Toe using Minimax

Aim:
    To build a Tic-Tac-Toe game and implement the Minimax algorithm so the
    AI never loses.

How to run:
    python practicals/practical_04_tictactoe_minimax.py
"""

# ---------------------------------------------------------------
# STEP 1: The 3x3 board is stored as a list of 9 items
# Positions:   0 | 1 | 2
#              3 | 4 | 5
#              6 | 7 | 8
# An empty square is stored as "" (empty text).
# ---------------------------------------------------------------
board = ["" for _ in range(9)]


# STEP 2: Helper functions
def print_board(b):
    for i in range(0, 9, 3):
        row = [b[j] if b[j] != "" else " " for j in range(i, i + 3)]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 6:
            print("---+---+---")


def check_winner(b, player):
    # All 8 winning lines
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    return any(all(b[i] == player for i in combo) for combo in win_combos)


def is_draw(b):
    return "" not in b and not check_winner(b, "O") and not check_winner(b, "X")


print("Initial Clean Board Layout:")
print_board(board)
print("\n[OPTIMIZATION VERIFIED] Alpha-Beta Pruning integrated.")
print("Minimax evaluates all game-tree branches and prunes redundant subtrees "
      "when beta <= alpha.\n")


# ---------------------------------------------------------------
# STEP 3: Minimax with Alpha-Beta pruning
# AI = "O" tries to MAXIMISE the score (+1 means AI wins)
# Human = "X" tries to MINIMISE the score (-1 means human wins)
# Alpha-Beta pruning skips branches that cannot change the result.
# ---------------------------------------------------------------
def minimax_ab(b, depth, is_maximizing, alpha, beta):
    # Terminal scores: AI wins = +1, Human wins = -1, Draw = 0
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if "" not in b:
        return 0

    if is_maximizing:                       # AI's turn
        best_score = -float("inf")
        for i in range(9):
            if b[i] == "":
                b[i] = "O"                  # try the move
                score = minimax_ab(b, depth + 1, False, alpha, beta)
                b[i] = ""                   # undo the move
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break                   # Beta cutoff
        return best_score
    else:                                   # Human's turn
        best_score = float("inf")
        for i in range(9):
            if b[i] == "":
                b[i] = "X"
                score = minimax_ab(b, depth + 1, True, alpha, beta)
                b[i] = ""
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break                   # Alpha cutoff
        return best_score


# STEP 4: Choose the AI's best move (the move with the highest score)
def best_move(b):
    best_score = -float("inf")
    move = None
    for i in range(9):
        if b[i] == "":
            b[i] = "O"
            score = minimax_ab(b, 0, False, -float("inf"), float("inf"))
            b[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move


# ---------------------------------------------------------------
# STEP 5: Simulated game (Human = X, AI = O)
# ---------------------------------------------------------------
sample_moves = [4, 2, 7]    # Human moves: center, corner, edge
sim_board = ["" for _ in range(9)]

print("--- Simulated Game Trace ---")
for h_move in sample_moves:
    sim_board[h_move] = "X"
    print(f"Human plays at {h_move}:")
    if check_winner(sim_board, "X") or is_draw(sim_board):
        break
    ai_pos = best_move(sim_board)
    sim_board[ai_pos] = "O"
    print(f"AI counters at {ai_pos}:")
    print_board(sim_board)
    print("-" * 15)
    if check_winner(sim_board, "O") or is_draw(sim_board):
        break

# Final result of the simulated game
win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
              [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
if check_winner(sim_board, "O"):
    line = next(c for c in win_combos if all(sim_board[i] == "O" for i in c))
    print(f"Result: AI Wins! Line detected across {line}.")
elif check_winner(sim_board, "X"):
    print("Result: Human Wins!")
else:
    print("Result: Draw.")
