from Classes.card import Card, PokerCard, SpanishCard
from Classes.deck import Deck
from sotaP import SotaP

if __name__ == '__main__':
    # print("main")
    # a = PokerCard(2, 2)
    # print(a)
    # a = PokerCard(0, 3)
    # print(a)

    # d = Deck(PokerCard)
    # d = Deck(SpanishCard)
    # d.shuffleStack()
    # print(d)

    game = SotaP(4)
    game.printPlayers()
