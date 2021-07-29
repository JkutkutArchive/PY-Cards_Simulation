import random
from Classes.colorOutput import *
from Classes.card.pokerCard import PokerCard
from Classes.playerHand import PlayerHand
from Classes.deck import Deck

class Poker:
    HANDS = {
        "Royal Flush":     10000000000,
        "Straight Flush":  1000000000,
        "Four of a kind":  100000000,
        "Full house":      10000000,
        "Flush":           1000000,
        "Straight":        100000,
        "Three of a kind": 10000,
        "Two pair":        1000,
        "Pair":            100,
        "High card":       0
    }

    def __init__(self) -> None:
        pass

    @classmethod
    def analyze(cls, hand) -> str:
        if not isinstance(hand, PlayerHand):
            raise Exception("The hand given is not valid")

        print(f"Checking:\n{hand.__str__()}")
        
        
        # Sort array using insertion sort
        sortedHand = hand.getHand().copy() # Clone the array
        for i in range(1, 5):
            val = sortedHand[i]
            j = i-1
            while j >=0 and val.compare(sortedHand[j]) > 0:
                    sortedHand[j+1] = sortedHand[j]
                    j -= 1
            sortedHand[j+1] = val
        
        i = 1
        pairs = []
        while i < 5: # Check the array
            if sortedHand[i - 1].getRank() == sortedHand[i].getRank():
                l = 2
                while i + 1 < 5 and sortedHand[i].getRank() == sortedHand[i + 1].getRank():
                    l += 1
                    i += 1
                # print(f"  Pair of {i}'s -> {l}")

                pairs.append({"rank": sortedHand[i].getRank(), "amount": l})
            i += 1
        
        print(f"The greatest card is the {sortedHand[0].__str__()}")
        print(pairs)


        points = None
        extraP = 0 # Extra points

        if len(pairs) == 1: # if pair, 3 of a kind or 4 of a kind
            l = pairs[0]["amount"]
            extraP = pairs[0]["rank"]
            
            if l == 2:
                points = Poker.HANDS["Pair"]
            elif l == 3:
                points = Poker.HANDS["Three of a kind"]
            else: # 4
                points = Poker.HANDS["Four of a kind"]
            
        elif len(pairs) == 2: # 2 pair or full house
            extraP = pairs[0]["rank"] + pairs[1]["rank"]

            if pairs[0]["amount"] < pairs[1]["amount"]: # Full house inverted => invert array
                tmp = pairs[0]
                pairs[0] = pairs[1]
                pairs[1] = tmp
            
            if pairs[0]["amount"] == 2:
                points = Poker.HANDS["Two pair"]
            else:
                points = Poker.HANDS["Full house"]

        else: # (royal or straight or --) flush, straight or high card
            
            points = sortedHand[0].__getRankPoint__()
        
        points += extraP

        print(f"Points: {points}")
        return "\n\n"