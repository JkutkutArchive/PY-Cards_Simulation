from poker import Poker
from Classes.card import Card, PokerCard, SpanishCard
from Classes.deck import Deck
from Classes.playerHand import PlayerHand
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

    # game = SotaP(4)

    # sota = game.game()

    # for step in sota: # For each step of the game
    #     # print(step)
    #     pass # Do it

    # print("Game results:")
    # for i in range(len(game.gameStats["scoreBoard"])-1, -1, -1):
    #     userName = game.gameStats["scoreBoard"][i].getName()
    #     fastRecordIndex = game.gameStats["scoreBoard"][i].index
    #     print(f"  - {userName} -> {game.gameStats['iAmThefastest'][fastRecordIndex]}")
    
    # print(game.gameStats["iAmThefastest"])

    print("Poker testing")
    N = 2

    players = [PlayerHand(name=f"Player{i}") for i in range(N)]
    cards = [[] for _ in range(N)]

    cards[0] = [ # High card
        PokerCard(2, 0),
        PokerCard(1, 1),
        PokerCard(4, 2),
        PokerCard(10, 2),
        PokerCard(7, 3)
    ]
    cards[1] = [ # Pair
        PokerCard(1, 0),
        PokerCard(3, 1),
        PokerCard(3, 2),
        PokerCard(10, 2),
        PokerCard(7, 3)
    ]

    for i in range(N): # for each player
        for j in range(5): # for each card
            players[i].takeCard(cards[i][j])
    
        print(Poker.analyze(players[i]))
