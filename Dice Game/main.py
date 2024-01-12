import random


class Die:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


class Player:
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def roll_die(self):
        self._die.roll()
        return self._die.roll()

    def increment(self):
        self._counter += 1

    def decrement(self):
        self._counter -= 1


class Game:
    def __init__(self, player1, palyer2):
        self._player1 = player1
        self._player2 = palyer2
        self.player1_name = "Player1"
        self.player2_name = "player2"

    def play(self):
        print("============================")
        print("Wellcome to Roll Die Game 🎲!")
        print("============================")
        self.player1_name = str(input("Please enter Player1's name:"))
        self.player2_name = str(input("Please enter Player2's name:"))
        while True:
            self.paly_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def paly_round(self):
        # Welcome
        print(" \n------- New Round ------- ")

        # Roll Die
        player1_value = self._player1.roll_die()
        player2_value = self._player2.roll_die()

        # Show player1 value
        input(f"please any key to show {self.player1_name} die")
        print(f"{self.player1_name}'s die: {player1_value}")

        # Show player2 value
        input(f"\nplease any key to show {self.player2_name} die")
        print(f"{self.player2_name}'s die: {player2_value}\n")

        # Determine Winner and Loser
        if player1_value > player2_value:
            print(f"{self.player1_name} Won🏅!!!")
            self.update_counter(winner=self._player1, loser=self._player2)
        elif player1_value < player2_value:
            print(f"{self.player2_name} Won🏅!!!")
            self.update_counter(winner=self._player2, loser=self._player1)
        else:
            print("It's a tie!")

        # Show Counter
        self.show_counter()

    def update_counter(self, winner, loser):
        winner.decrement()
        loser.increment()

    def show_counter(self):
        print(f"\n{self.player1_name}'s Counter: {self._player1.counter}")
        print(f"{self.player2_name}'s Counter: {self._player2.counter}")

    def check_game_over(self):
        if self._player1.counter == 0:
            self.show_game_over(self.player1_name)
            return True
        elif self._player2.counter == 0:
            self.show_game_over(self.player2_name)
            return
        else:
            return False  # No one won yet

    def show_game_over(self, winner):
        print("\n==============")
        print(" G A M E  O V E R !")
        print("==============")
        print(f"{winner} won the game! ")
        print("==============")


die1 = Die()
die2 = Die()

player1 = Player(die1)
player2 = Player(die2)

game = Game(player1, player2)

game.play()
