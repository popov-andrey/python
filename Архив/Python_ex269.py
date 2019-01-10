class Card:
    suits = ['пики', 'черви', 'буби', 'треф']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'даму', 'валета', 'короля', 'туза']

    def __init__(self, v, s):
        """suit и value - целые числа"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + ' ' + self.suits[self.suit]
        return v


card = Card(3, 2)

print(card)
