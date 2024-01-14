class Move:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def is_valid(self):
        if 1 <= self._value <= 9:
            return True
        else:
            return False

    def find_row(self):
        if self._value in (1, 2, 3):
            return 0
        elif self._value in (4, 5, 6):
            return 1
        else:
            return 2

    def find_colum(self):
        if self._value in (1, 4, 7):
            return 0
        elif self._value in (2, 5, 8):
            return 1
        else:
            return 2
