from card import Card


class Deck:
    def __init__(self, cards: list):

        self.cards = cards

    def get_value_of_deck(self):
        cost = 0

        for card in self.cards:
            try:
                cost += card.cost
            except TypeError:
                pass

        return cost