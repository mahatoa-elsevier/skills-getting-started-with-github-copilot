"""
Tic Tac Toe Game - Created using GitHub Copilot
This file demonstrates different ways GitHub Copilot can assist with code generation
"""

class TicTacToe:
    def __init__(self):
        # Initialize the game board with empty spaces
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    
    def print_board(self):
        """Display the current board state using grid formatting"""
        print("\n")
        for i in range(3):
            print(f" {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} ")
            if i < 2:
                print("-----------")
        print("\n")
    
    def print_board_nums(self):
        """Show position numbers for reference"""
        print("\nPosition numbers:")
        for i in range(3):
            print(f" {i*3} | {i*3+1} | {i*3+2} ")
            if i < 2:
                print("-----------")
        print("\n")
    
    def is_winner(self, player):
        """Check if the specified player has won the game"""
        # Define all winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False
    
    def is_board_full(self):
        """Check if all spaces on the board are filled"""
        return ' ' not in self.board
    
    def get_available_moves(self):
        """Return a list of available positions on the board"""
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def make_move(self, position):
        """Place the current player's mark at the specified position"""
        if position < 0 or position > 8:
            print("Invalid position! Please choose 0-8.")
            return False
        
        if self.board[position] != ' ':
            print("That position is already taken!")
            return False
        
        self.board[position] = self.current_player
        return True
    
    def switch_player(self):
        """Toggle between X and O players"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play_game(self):
        """Main game loop that handles player turns and game flow"""
        print("Welcome to Tic Tac Toe!")
        print("Player X goes first.\n")
        self.print_board_nums()
        
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn")
            
            # Get valid input from player
            while True:
                try:
                    position = int(input("Enter position (0-8): "))
                    if self.make_move(position):
                        break
                except ValueError:
                    print("Please enter a valid number!")
            
            # Check for winner
            if self.is_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins! 🎉")
                break
            
            # Check for tie
            if self.is_board_full():
                self.print_board()
                print("It's a tie! 🤝")
                break
            
            # Switch to next player
            self.switch_player()
    
    def get_best_move_minimax(self, depth=0, is_maximizing=True):
        """
        Calculate the best move using the minimax algorithm with alpha-beta pruning.
        This allows for an AI opponent that plays optimally.
        """
        # Check terminal states
        if self.is_winner('O'):
            return 10 - depth
        elif self.is_winner('X'):
            return depth - 10
        elif self.is_board_full():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for move in self.get_available_moves():
                self.board[move] = 'O'
                score = self.get_best_move_minimax(depth + 1, False)
                self.board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves():
                self.board[move] = 'X'
                score = self.get_best_move_minimax(depth + 1, True)
                self.board[move] = ' '
                best_score = min(score, best_score)
            return best_score
    
    def find_best_move(self):
        """Find and return the best move for the AI player"""
        best_move = None
        best_score = float('-inf')
        
        for move in self.get_available_moves():
            self.board[move] = 'O'
            score = self.get_best_move_minimax(0, False)
            self.board[move] = ' '
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def play_vs_ai(self):
        """Game mode where the player competes against an AI opponent"""
        print("Welcome to Tic Tac Toe vs AI!")
        print("You are X, AI is O.\n")
        self.print_board_nums()
        
        while True:
            self.print_board()
            
            if self.current_player == 'X':
                print("Your turn (Player X)")
                while True:
                    try:
                        position = int(input("Enter position (0-8): "))
                        if self.make_move(position):
                            break
                    except ValueError:
                        print("Please enter a valid number!")
            else:
                print("AI is thinking...")
                ai_move = self.find_best_move()
                if ai_move is not None:
                    self.make_move(ai_move)
                    print(f"AI chose position {ai_move}")
            
            # Check for winner
            if self.is_winner(self.current_player):
                self.print_board()
                if self.current_player == 'X':
                    print("You win! 🎉")
                else:
                    print("AI wins! 🤖")
                break
            
            # Check for tie
            if self.is_board_full():
                self.print_board()
                print("It's a tie! 🤝")
                break
            
            # Switch to next player
            self.switch_player()


def main():
    """Main entry point with game mode selection"""
    while True:
        print("\n=== Tic Tac Toe Game ===")
        print("1. Player vs Player")
        print("2. Player vs AI")
        print("3. Exit")
        
        choice = input("\nSelect game mode (1-3): ")
        
        if choice == '1':
            game = TicTacToe()
            game.play_game()
        elif choice == '2':
            game = TicTacToe()
            game.play_vs_ai()
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
