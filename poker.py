import random
from Classes.colorOutput import *
from Classes.card import PokerCard
from Classes.playerHand import PlayerHand
from Classes.deck import Deck

class Poker:
    def __init__(self) -> None:
        pass

    @classmethod
    def analyze(cls, hand) -> str:
        if not isinstance(hand, PlayerHand):
            raise Exception("The hand given is not valid")
        
        hc = hand.seeCard(0)
        
        for c in hand.getHand():
            
            pass