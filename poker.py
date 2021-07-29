import random
from Classes.colorOutput import *
from Classes.card.pokerCard import PokerCard
from Classes.playerHand import PlayerHand
from Classes.deck import Deck

class Poker:
    HANDS = {
        "Royal Flush":     100000000,
        "Straight Flush":  10000000,
        "Four of a kind":  1000000,
        "Full house":      100000,
        "Flush":           10000,
        "Straight":        10000,
        "Three of a kind": 1000,
        "Two pair":        100,
        "Pair":            10,
        "High card":       0
    }

    def __init__(self) -> None:
        pass

    @classmethod
    def analyze(cls, hand) -> str:
        if not isinstance(hand, PlayerHand):
            raise Exception("The hand given is not valid")

        print(f"Checking:\n{hand.__str__()}")
        
        hc = hand.seeCard(0)
        ranks = []
        
        for c in hand.getHand():
            if c.compare(hc) > 0: # update highest card
                hc = c
            
            ranks.append(c.getRank())
        
        # Sort array using insertion sort
        for i in range(1, 5):
            val = ranks[i]
            j = i-1
            while j >=0 and val > ranks[j] :
                    ranks[j+1] = ranks[j]
                    j -= 1
            ranks[j+1] = val
        
        i = 1
        pairs = []
        while i < 5: # Check the array
            if ranks[i - 1] == ranks[i]:
                l = 2
                while i + 1 < 5 and ranks[i] == ranks[i + 1]:
                    l += 1
                    i += 1
                # print(f"  Pair of {i}'s -> {l}")

                pairs.append({"rank": ranks[i], "amount": l})
            i += 1
        
        # print(f"The greatest card is the {hc.__str__()}")
        print(ranks)
        print(pairs)

        if len(pairs) == 1: # if pair, 3 of a kind or 4 of a kind
            return "\n\n"
        elif len(pairs) == 2: # 2 pair or full house
            extraP = pairs[0]["rank"] + pairs[1]["rank"]

            return "\n\n"
        else: # (royal or straight or --) flush, straight or high card
            return "\n\n"