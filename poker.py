from Classes.card.card import Card
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
        while i < 5: # Check the array for pairs
            if sortedHand[i - 1].getRank() == sortedHand[i].getRank():
                l = 2
                while i + 1 < 5 and sortedHand[i].getRank() == sortedHand[i + 1].getRank():
                    l += 1
                    i += 1
                pairs.append({"rank": sortedHand[i].__getRankPoint__(), "amount": l})
            i += 1


        hand = None
        points = 0
        extraP = 0 # Extra points

        if len(pairs) == 1: # if pair, 3 of a kind or 4 of a kind
            l = pairs[0]["amount"]
            extraP = pairs[0]["rank"]
            
            if l == 2:
                hand = "Pair"
            elif l == 3:
                hand = "Three of a kind"
            else: # 4
                hand = "Four of a kind"

            points = Poker.HANDS[hand]
            
        elif len(pairs) == 2: # 2 pair or full house
            extraP = pairs[0]["rank"] + pairs[1]["rank"]

            if pairs[0]["amount"] < pairs[1]["amount"]: # Full house inverted => invert array
                tmp = pairs[0]
                pairs[0] = pairs[1]
                pairs[1] = tmp
            
            if pairs[0]["amount"] == 2:
                hand = "Two pair"
            else:
                hand = "Full house"
            
            points = Poker.HANDS[hand]

        # ----------------
        # Check if (royal, straight or --) flush, straight or high card

        royal = False    # A K Q J 10
        straight = False # 2 3 4 5 6 
        flush = True    # Same suit

        print([i.__str__() for i in sortedHand])

        # Check if straight (and royal)
        # jokers = 0
        # ind = 0
        # while sortedHand[ind].__getRankPoint__() == PokerCard.RANK["MAX"] + 1:
        #     if sortedHand[ind].getRank() == PokerCard.RANK["JOKER"]:
        #         jokers += 1
        #         sortedHand.pop(0)
        #     else:
        #         ind += 1
        # print(f"Checking for straight with {jokers} jokers")

        # ind = 0
        # if sortedHand[0].getRank() == 1: # if first is Ace
        #     pass


        # if straight and False: # If straight, check if royal
        #     royal = True
        
        # Check if flush
        currentSuit = sortedHand[0].getSuit()
        for i in range(1, len(sortedHand)):
            if sortedHand[i].getSuit() != currentSuit:
                flush = False
                break
        
        if flush:
            if straight:
                if royal: # If royal flush
                    points = Poker.HANDS["Royal Flush"]
                else: # If straight flush
                    points = Poker.HANDS["Straight Flush"]
            else: # if flush
                points += Poker.HANDS["Flush"]
                print("Flush")
        
        if not any([royal, straight, flush]) and points == 0: # if high card
            points = sortedHand[0].__getRankPoint__()
        
        points += extraP

        print(f"Points: {points}")
        
        print("\n")
        return points