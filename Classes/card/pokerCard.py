from .card import Card

class PokerCard(Card):
    SUIT = {
        "CLUBS": 0,
        "DIAMONDS": 1,
        "HEARTS": 2,
        "SPADES": 3
    }
    SUITNAME = ["Clubs", "Diamonds", "Hearts", "Spades"]
    RANK = {
        "MIN": 0, # 0 = Joker
        "MAX": 13
    }
    RANKNAME = {
        0: "Poker",
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King",
    }