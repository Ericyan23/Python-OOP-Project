import random
import tkinter as tk


class Die:
    def roll(self):
        return random.randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.die = Die()

    def roll_die(self):
        return self.die.roll()


class DiceGameApp:
    def __init__(self, master):
        self.master = master
        master.title("Dice Rolling Game")

        self.label = tk.Label(master, text="Welcome to the Dice Rolling Game!")
        self.label.pack()

        self.player1_name_entry = tk.Entry(master)
        self.player1_name_entry.pack()
        self.player1_name_entry.insert(0, "Player 1 Name")

        self.player2_name_entry = tk.Entry(master)
        self.player2_name_entry.pack()
        self.player2_name_entry.insert(0, "Player 2 Name")

        self.roll_button = tk.Button(master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.player1 = None
        self.player2 = None

    def roll_dice(self):
        if not self.player1 or not self.player2:
            player1_name = self.player1_name_entry.get()
            player2_name = self.player2_name_entry.get()
            self.player1 = Player(player1_name)
            self.player2 = Player(player2_name)

        player1_roll = self.player1.roll_die()
        player2_roll = self.player2.roll_die()

        result = f"{self.player1.name} rolled {player1_roll}\n{self.player2.name} rolled {player2_roll}\n"
        if player1_roll > player2_roll:
            result += f"{self.player1.name} wins!"
        elif player2_roll > player1_roll:
            result += f"{self.player2.name} wins!"
        else:
            result += "It's a tie!"

        self.result_label.config(text=result)


root = tk.Tk()
app = DiceGameApp(root)
root.mainloop()
