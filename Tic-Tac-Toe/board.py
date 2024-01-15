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

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_colum()
        value = self.game_board[row][col]
        if value == Board.empty_cell:
            self.game_board[row][col] = player.marker
        else:
            print("This position is already taken. Please enter another one")

    def check_game_over(self, player, last_move):
        return (
            (self.check_row(player, last_move))
            or (self.check_col(player, last_move))
            or (self.check_diagonal(player))
            or (self.check_antidiagonal(player))
        )

    def check_row(self, player, last_move):
        row = last_move.get_row()
        return self.game_board[row].count(player.marker) == 3

    def check_col(self, player, last_move):
        col = last_move.get_colum()
        marker_count = 0

        for i in range(3):
            if self.game_board[i][col] == player.marker:
                marker_count += 1

        return marker_count == 3

    def check_diagonal(self, player):
        marker_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                marker_count += 1
        return marker_count == 3

    def check_antidiagonal(self, player):
        marker_count = 0
        for i in range(3):
            if self.game_board[i][2 - i] == player.marker:
                marker_count += 1
        return marker_count == 3

    def check_is_tie(self):
        empty_counter = 0
        for row in self.game_board:
            empty_counter += row.count(Board.empty_cell)
        return empty_counter == 0

    def reset_board(self):
        self.game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
