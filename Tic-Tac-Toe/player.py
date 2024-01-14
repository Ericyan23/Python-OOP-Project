import random

from move import Move


class Player:
    human_marker = "X"
    computer_marker = "O"

    def __init__(self, is_human=True):
        self._is_human = is_human

        if self.is_human:
            self._marker = Player.human_marker
        else:
            self._marker = Player.computer_marker

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        while True:
            user_input = int(input("Please enter integer 1-9:"))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter valid integer between 1 and 9!")
        return move

    def get_computer_move(self):
        computer_move = random.randint(1, 9)
        move = Move(computer_move)
        print(f"Computer move(1-9): {move.value}")
        return move


player = Player(False)

print(player.is_human, player.marker)

move = player.get_move().value

print(move)


