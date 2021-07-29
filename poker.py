import random
from Classes.colorOutput import *
from Classes.card import PokerCard
from Classes.cardPlayer import CardPlayer
from Classes.deck import Deck

class Poker:
    def __init__(self) -> None:
        pass

    @classmethod
    def analyze(cls, hand) -> str:
        if not isinstance(hand, CardPlayer):
            raise Exception("The hand given is not valid")
        
        hc = hand.seeCard(0)
        print(hc)
        print(hand)