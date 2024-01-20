# Import necessary classes
from board import Board
from player import Player


# Define the TicTacToeGame class
class TicTacToeGame:
    def start(self):
        # Print the welcome message and game border
        border = "*" * 30
        print(border)
        welcome_message = "  Welcome to Tic Tac Toe Game  "
        print(welcome_message)
        print(border)

        # Initialize the game board and players
        board = Board()
        player = Player()  # Human player
        computer = Player(False)  # Computer player

        # Print the initial game board
        board.print_game_board()

        # Main game loop
        while True:
            # Loop for each round of the game
            while True:
                # Human player's turn
                human_move = player.get_human_move()
                board.submit_move(player, human_move)
                board.print_game_board()

                # Check for tie or win after human's move
                if board.check_is_tie():
                    print("It's a Tie! Try again.")
                    break
                elif board.check_game_over(player, human_move):
                    print("You Won!!")
                    break

                # Computer's turn
                computer_move = computer.get_computer_move()
                board.submit_move(computer, computer_move)
                board.print_game_board()

                # Check for win after computer's move
                if board.check_game_over(computer, computer_move):
                    print("Oops... Computer Won. Try again.")
                    break

            # Prompt to play again
            play_again = input(
                "Would you like to play again? Enter Y for yes or N for No: "
            ).upper()

            # Handle the player's choice
            if play_again == "N":
                print("Bye! Come back soon")
                break
            elif play_again == "Y":
                self.start_new_round(board)
            else:
                print("Invalid input, assuming you want to play again.")
                self.start_new_round(board)

    def start_new_round(self, board):
        # Start a new round of the game
        border = "*" * 13
        print(border)
        print("  New Round  ")
        print(border)
        board.reset_board()
        board.print_game_board()  # Missing parentheses to call the function


# Create a game instance and start the game
game = TicTacToeGame()
game.start()
