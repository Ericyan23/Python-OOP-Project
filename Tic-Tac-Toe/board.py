class Board:
    empty_cell = 0

    def __init__(self):
        self.game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def print_game_board(self):
        print("\nPosotion:")
        self.print_game_board_with_position()

        print("\nBoard:")
        for row in self.game_board:
            print("|", end="")
            for colum in row:
                if colum == Board.empty_cell:
                    print("   |", end="")
                else:
                    print(f" {colum} |", end="")
            print()

    def print_game_board_with_position(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")


board = Board()
board.print_game_board()
