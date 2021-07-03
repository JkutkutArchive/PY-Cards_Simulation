class Card:
    SUIT = {}
    RANK = {}
    def __init__(self, rank, suit) -> None:
        if self.__class__ == Card:
            raise Exception("The class Card can not be initialized, it is a prototype for the rest of the classes.")
        if not self.isValidRank(rank):
            raise Exception(f"Not valid rank. It must be {self.RANK['MIN']} <= rank <= {self.RANK['MIN']}")
        if not self.isValidSuit(suit):
            raise Exception(f"Not valid suit. It must be {', '.join([i for i in self.SUIT.keys()])}.\n Therefore, 0 <= suit <= {len(self.SUIT)}")
        

        self.rank = rank
        self.suit = suit
        pass

    def isValidRank(self, rank):
        return isinstance(rank, int) and rank >= self.RANK["MIN"] and rank <= self.RANK["MAX"]
    def isValidSuit(self, suit):
        return isinstance(suit, int) and suit >= 0 and suit <= len(self.SUIT)

class PokerCard(Card):
    SUIT = {
        "CLUBS": 0,
        "DIAMONDS": 1,
        "HEARTS": 2,
        "SPADES": 3
    }
    RANK = {
        "MIN": 0, # 0 = Joker
        "MAX": 13
    }

class SpanishCard(Card):
    SUIT = {
        "OROS": 0,
        "COPAS": 1,
        "ESPADAS": 2,
        "BASTOS": 3
    }
    RANK = {
        "MIN": 1,
        "MAX": 12
    }
