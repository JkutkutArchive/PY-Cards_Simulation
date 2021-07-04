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

    sota = game.game()

    for step in sota: # For each step of the game
        # print(step)
        pass # Do it

    print("Game results:")
    for i in range(len(game.gameStats["scoreBoard"])-1, -1, -1):
        userName = game.gameStats["scoreBoard"][i].getName()
        fastRecordIndex = game.gameStats["scoreBoard"][i].index
        print(f"  - {userName} -> {game.gameStats['iAmThefastest'][fastRecordIndex]}")
    
    # print(game.gameStats["iAmThefastest"])
