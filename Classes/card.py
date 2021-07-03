class Card:
    SUIT = {}
    RANK = {}

    def __init__(self, rank, suit) -> None:
        if self.__class__ == Card: # If constructor called from this class
            raise Exception("The class Card can not be initialized, it is a prototype for the rest of the classes.")
        
        # Check arguments
        if not self.isValidRank(rank):
            raise Exception(f"Not valid rank. It must be {self.RANK['MIN']} <= rank <= {self.RANK['MIN']}")
        
        if not self.isValidSuit(suit):
            raise Exception(f"Not valid suit. It must be {', '.join([i for i in self.SUIT.keys()])}.\n Therefore, 0 <= suit <= {len(self.SUIT)}")
        
        # Store them (valid)
        self.rank = rank
        self.suit = suit

    def isValidRank(self, rank) -> bool:
        '''If the rank given is a valid integer with a correct value.'''
        return isinstance(rank, int) and rank >= self.RANK["MIN"] and rank <= self.RANK["MAX"]
    
    def isValidSuit(self, suit) -> bool:
        '''If the suit given is a valid one. It must be the integer equivalent.'''
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
