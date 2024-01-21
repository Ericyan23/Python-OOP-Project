class WarCardGame:
    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    def start_battle(self, cards_from_war=None):
        print("\n== Let's Start Battle ==\n")

        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        # Check if both players have drawn a card
        if player_card and computer_card:
            print("You card:")
            player_card.show()

            print("\nComputer Card:")
            computer_card.show()

            winner = self.get_round_winner(player_card, computer_card)
            cards_won = self.get_card_won(player_card, computer_card, cards_from_war)

            if winner == WarCardGame.PLAYER:
                print("You won the round!")
                self.add_card_to_character(self._player, cards_won)
            elif winner == WarCardGame.COMPUTER:
                print("Computer won this round.")
                self.add_card_to_character(self._computer, cards_won)
            else:
                print("It's a Tie!")
                self.start_war(cards_won)

            return winner
        else:
            # Handle the scenario where one or both players cannot draw a card
            if not player_card or not computer_card:
                print(
                    "One of the players cannot draw a card. Checking for game over..."
                )
                game_over = self.check_game_over()
                if game_over:
                    return (
                        None  # Or handle the game over scenario as per your game design
                    )
                else:
                    print("Game continues...")
                    # Optionally, you can add logic here for what happens when the game continues

    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif computer_card.value > player_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_card_won(self, player_card, computer_card, previous_cards):
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]

    def add_card_to_character(self, character, list_of_cards):
        for card in list_of_cards:
            character.add_card(card)

    def start_war(self, cards_from_battle):
        # Check if players have enough cards for a war
        if self._player.deck.size < 3:
            print("Player does not have enough cards for war. Player loses!")
            return WarCardGame.COMPUTER
        if self._computer.deck.size < 3:
            print("Computer does not have enough cards for war. Computer loses!")
            return WarCardGame.PLAYER
        else:
            # Proceed with war if both players have enough cards
            player_cards = []
            computer_cards = []
            for i in range(3):
                if self._player.deck.size > 0:
                    player_card = self._player.draw_card()
                    player_cards.append(player_card)
                if self._computer.deck.size > 0:
                    computer_card = self._computer.draw_card()
                    computer_cards.append(computer_card)

            # Hide the first two cards of each player
            print("Six hidden cards: XXX XXX")
            self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print("========================")
            print("|   G A M E  O V E R   |")
            print("========================")
            print("Computer Won. Try again")
            return True
        elif self._computer.has_empty_deck():
            print("========================")
            print("|   G A M E  O V E R   |")
            print("========================")
            print(f"congratulations! {self._player.name} Won!!")
        else:
            return False

    def print_stats(self):
        print("\n---")
        print(f"You have {self._player.deck.size} cards on your deck")
        print(f"The computer have {self._computer.deck.size} on its deck")
        print("----")

    def print_welcome_message(self):
        print("=========================")
        print("|     War Card Game     |")
        print("=========================")
