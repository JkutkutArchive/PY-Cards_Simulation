import sys
sys.path.append('.')

from poker import Poker
from Classes.card.pokerCard import PokerCard
from Classes.playerHand import PlayerHand

if __name__ == '__main__':
    print("Poker testing")

    cards = []
    spectedScore = []
    players = []

    cards.append([ # High card
        PokerCard(2, 0),
        PokerCard(1, 1),
        PokerCard(4, 2),
        PokerCard(10, 2),
        PokerCard(7, 3)
    ])
    spectedScore.append(14)

    cards.append([ # Pair
        PokerCard(1, 0),
        PokerCard(3, 1),
        PokerCard(3, 2),
        PokerCard(10, 2),
        PokerCard(7, 3)
    ])
    spectedScore.append(103)

    cards.append([ # Pair by joker
        PokerCard(2, 0),
        PokerCard(3, 1),
        PokerCard(0, 2),
        PokerCard(10, 2),
        PokerCard(7, 3)
    ])
    spectedScore.append(110)

    cards.append([ # 2 pair
        PokerCard(1, 0),
        PokerCard(3, 1),
        PokerCard(3, 2),
        PokerCard(1, 2),
        PokerCard(7, 3)
    ])
    spectedScore.append(1017)

    cards.append([ # Tree of a kind
        PokerCard(1, 0),
        PokerCard(3, 1),
        PokerCard(3, 2),
        PokerCard(10, 2),
        PokerCard(3, 3)
    ])
    spectedScore.append(10003)

    cards.append([ # Tree of a kind by joker
        PokerCard(1, 0),
        PokerCard(3, 1),
        PokerCard(0, 2),
        PokerCard(10, 2),
        PokerCard(3, 3)
    ])
    spectedScore.append(10003)

    # STRAIGHT
    cards.append([ # Straight
        PokerCard(1, 0),
        PokerCard(4, 1),
        PokerCard(2, 2),
        PokerCard(3, 2),
        PokerCard(5, 3)
    ])
    spectedScore.append(100014)

    cards.append([ # Straight 2
        PokerCard(4, 0),
        PokerCard(6, 1),
        PokerCard(5, 2),
        PokerCard(7, 2),
        PokerCard(8, 3)
    ])
    spectedScore.append(100008)

    cards.append([ # Straight 3
        PokerCard(13, 0),
        PokerCard(12, 1),
        PokerCard(1, 2),
        PokerCard(2, 2),
        PokerCard(3, 3)
    ])
    spectedScore.append(100014)

    cards.append([ # Straight 4 by joker
        PokerCard(13, 0),
        PokerCard(0, 1),
        PokerCard(1, 2),
        PokerCard(2, 2),
        PokerCard(3, 3)
    ])
    spectedScore.append(100014)

    cards.append([ # Straight 5 by joker
        PokerCard(13, 0),
        PokerCard(12, 1),
        PokerCard(1, 2),
        PokerCard(0, 2),
        PokerCard(3, 3)
    ])
    spectedScore.append(100014)



    cards.append([ # Flush
        PokerCard(1, 1),
        PokerCard(7, 1),
        PokerCard(10, 1),
        PokerCard(6, 1),
        PokerCard(3, 1)
    ])
    spectedScore.append(1000014)

    cards.append([ # Flush by joker + pair
        PokerCard(1, 1),
        PokerCard(0, 3),
        PokerCard(10, 1),
        PokerCard(6, 1),
        PokerCard(3, 1)
    ])
    spectedScore.append(1000114)

    cards.append([ # Flush by joker + 3
        PokerCard(1, 1),
        PokerCard(0, 3),
        PokerCard(10, 1),
        PokerCard(0, 2),
        PokerCard(3, 1)
    ])
    spectedScore.append(1010014)

    cards.append([ # Flush + pair
        PokerCard(1, 1),
        PokerCard(7, 1),
        PokerCard(6, 1),
        PokerCard(6, 1),
        PokerCard(3, 1)
    ])
    spectedScore.append(1000106)

    # Full house
    cards.append([ # Full house
        PokerCard(2, 1),
        PokerCard(2, 2),
        PokerCard(2, 3),
        PokerCard(3, 1),
        PokerCard(3, 2)
    ])
    spectedScore.append(10000007)

    cards.append([ # Full house by joker
        PokerCard(2, 1),
        PokerCard(2, 2),
        PokerCard(0, 3),
        PokerCard(3, 1),
        PokerCard(3, 2)
    ])
    spectedScore.append(10000008)

    cards.append([ # Four of a kind
        PokerCard(3, 0),
        PokerCard(3, 1),
        PokerCard(3, 2),
        PokerCard(10, 2),
        PokerCard(3, 3)
    ])
    spectedScore.append(100000003)

    cards.append([ # Four of a kind by joker
        PokerCard(3, 0),
        PokerCard(0, 1),
        PokerCard(3, 2),
        PokerCard(10, 2),
        PokerCard(3, 3)
    ])
    spectedScore.append(100000003)

    cards.append([ # Straight flush
        PokerCard(5, 1),
        PokerCard(6, 1),
        PokerCard(7, 1),
        PokerCard(8, 1),
        PokerCard(9, 1)
    ])
    spectedScore.append(1000000009)

    cards.append([ # Straight flush by joker
        PokerCard(5, 1),
        PokerCard(6, 1),
        PokerCard(0, 2),
        PokerCard(8, 1),
        PokerCard(9, 1)
    ])
    spectedScore.append(1000000010)

    cards.append([ # Straight flush by 2 jokers
        PokerCard(5, 1),
        PokerCard(6, 1),
        PokerCard(0, 2),
        PokerCard(8, 1),
        PokerCard(0, 1)
    ])
    spectedScore.append(1000000009)

    cards.append([ # Royal flush
        PokerCard(1, 1),
        PokerCard(13, 1),
        PokerCard(12, 1),
        PokerCard(11, 1),
        PokerCard(10, 1)
    ])
    spectedScore.append(10000000014)

    cards.append([ # Royal flush by joker
        PokerCard(1, 1),
        PokerCard(13, 1),
        PokerCard(0, 2),
        PokerCard(11, 1),
        PokerCard(10, 1)
    ])
    spectedScore.append(10000000014)

    cards.append([ # Royal flush by joker 2
        PokerCard(0, 2),
        PokerCard(13, 1),
        PokerCard(12, 1),
        PokerCard(11, 1),
        PokerCard(10, 1)
    ])
    spectedScore.append(10000000014)

    cards.append([ # Royal flush by 2 jokers
        PokerCard(0, 2),
        PokerCard(13, 1),
        PokerCard(12, 1),
        PokerCard(0, 3),
        PokerCard(10, 1)
    ])
    spectedScore.append(10000000014)


    cards.append([ # Five of a kind by joker
        PokerCard(3, 0),
        PokerCard(3, 1),
        PokerCard(3, 2),
        PokerCard(0, 2),
        PokerCard(3, 3)
    ])
    spectedScore.append(100000000003)

    cards.append([ # Five of a kind by 2 jokers
        PokerCard(3, 0),
        PokerCard(0, 1),
        PokerCard(3, 2),
        PokerCard(0, 2),
        PokerCard(3, 3)
    ])
    spectedScore.append(100000000003)


    for i in range(len(cards)): # for each player
        players.append(PlayerHand(name=f"Player{i}"))
        for j in range(5): # for each card
            players[i].takeCard(cards[i][j])

        p = Poker.analyze(players[i])
        if p != spectedScore[i]:
            raise Exception(f"\nAt index {i}, the spectedScore do not match:\n\tSpected: {spectedScore[i]}  Calculated: {p}")

    print("Testing ended")