class Card:
    SPECIAL_CARD = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit, value):
        self._value = value
        self._suit = suit

    @property
    def value(self):
        return self._value

    @property
    def suit(self):
        return self._suit

    def is_special(self):
        return self._value >= 11

    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        card_symbol = self._suit.symbols

        if self.is_special():
            card_desprice = Card.SPECIAL_CARD[card_value]
            print(f"{card_desprice} of {card_suit} {card_symbol}")
        else:
            print(f"{card_value} of {card_suit} {card_symbol}")
