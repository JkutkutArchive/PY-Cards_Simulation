import random
from Classes.colorOutput import *
from Classes.card.pokerCard import PokerCard
from Classes.playerHand import PlayerHand
from Classes.deck import Deck

class Poker:
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
        while i < 5:
            # print(f"{ranks[i - 1]} == {ranks[i]}")
            if ranks[i - 1] == ranks[i]:
                l = 2
                while i + 1 < 5 and ranks[i] == ranks[i + 1]:
                    l += 1
                    i += 1
                print(f"  Pair of {i}'s -> {l}")

            i += 1
        
        print(f"the greatest card is the {hc.__str__()}")
        print(ranks)

        return "\n\n"