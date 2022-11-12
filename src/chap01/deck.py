import collections

from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDesk:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position) -> Card:
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(a_card):
    rank_value = FrenchDesk.ranks.index(a_card.rank)
    return rank_value * len(suit_values) + suit_values[a_card.suit]


if __name__ == '__main__':
    deck = FrenchDesk()
    print(len(deck))
    # Reading specific cards from the deck—say, the first or the last—is easy, thanks to the __getitem__ method
    print(deck[0])
    print(deck[-1])
    # Randomly choosing a card is also easy
    print("---------------------Randomly choosing a card---------------------")
    print(choice(deck))
    print(choice(deck))
    # split the deck into two hands
    print("---------------------Split the deck into two hands---------------------")
    print(deck[:3])
    print(deck[12::13])
    # Iterating over the deck is also easy
    print("---------------------Iterating over the deck---------------------")
    for card in deck:
        print(card)
    # Containment testing
    print("---------------------Containment testing---------------------")
    print(Card('Q', 'hearts') in deck)
    print(Card('7', 'beasts') in deck)
    # Sorting the cards
    print("---------------------Sorting the cards---------------------")
    for card in sorted(deck, key=spades_high):
        print(card)
