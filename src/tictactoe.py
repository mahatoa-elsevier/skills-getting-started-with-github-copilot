# Tic Tac Toe game demonstrating different GitHub Copilot modes
#
# In this file we use comments to trigger various GitHub Copilot modes:
#  - `// copilot: suggest` for inline suggestions
#  - `// copilot: autocomplete` for full line completions
#  - `# copilot: debug` to hint at debugging assistance
#
# The game itself is a simple command-line Tic Tac Toe written in Python.

import sys

BOARD = [" "] * 9

WIN_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def print_board():
    print(f" {BOARD[0]} | {BOARD[1]} | {BOARD[2]} ")
    print("---+---+---")
    print(f" {BOARD[3]} | {BOARD[4]} | {BOARD[5]} ")
    print("---+---+---")
    print(f" {BOARD[6]} | {BOARD[7]} | {BOARD[8]} ")


def check_winner():
    for combo in WIN_COMBINATIONS:
        a, b, c = combo
        if BOARD[a] == BOARD[b] == BOARD[c] and BOARD[a] != " ":
            return BOARD[a]
    return None


def is_board_full():
    return all(space != " " for space in BOARD)


def make_move(position, player):
    if BOARD[position] == " ":
        BOARD[position] = player
        return True
    return False


def get_player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter a move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please try again.")
                continue
            if not make_move(move, player):
                print("That space is already taken. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a number between 1 and 9.")


def main():
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        get_player_move(current_player)
        print_board()
        winner = check_winner()
        if winner:
            print(f"Player {winner} wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
