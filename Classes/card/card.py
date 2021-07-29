class Card:
    SUIT = {}
    SUITNAME = []
    RANK = {}
    RANKNAME = {}

    def __init__(self, rank, suit) -> None:
        if not Card.isValidCardClass(self.__class__):
            raise Exception("The class Card can not be initialized, it is a prototype for the rest of the classes.")
        
        # Check arguments
        if not self.isValidRank(rank):
            raise Exception(f"Not valid rank. It must be {self.RANK['MIN']} <= rank <= {self.RANK['MIN']}")
        
        if not self.isValidSuit(suit):
            raise Exception(f"Not valid suit. It must be {', '.join([i for i in self.SUIT.keys()])}.\n Therefore, 0 <= suit <= {len(self.SUIT)}")
        
        # Store them (valid)
        self._rank = rank
        self._suit = suit

    # ########## GETTERS AND SETTERS ##########

    def getRank(self) -> int:
        return self._rank

    def getSuit(self) -> int:
        return self._suit

    def getRankName(self) -> str:
        if self.getRank() in self.RANKNAME:
            return self.RANKNAME[self.getRank()]
        return self.getRank()
    
    def getSuitName(self) -> str:
        return self.SUITNAME[self.getSuit()]

    def __str__(self) -> str:
        return f"{self.getRankName()} of {self.getSuitName()}"

    # ########## CHECKERS ##########
    def isValidRank(self, rank) -> bool:
        '''If the rank given is a valid integer with a correct value.'''
        return isinstance(rank, int) and rank >= self.RANK["MIN"] and rank <= self.RANK["MAX"]
    
    def isValidSuit(self, suit) -> bool:
        '''If the suit given is a valid one. It must be the integer equivalent.'''
        return isinstance(suit, int) and suit >= 0 and suit <= len(self.SUIT)
    
    @classmethod
    def isValidCardClass(cls, cardClass):
        '''Check if the class entered as an argument is a valid Card class.'''
        return issubclass(cardClass, Card) and cardClass != Card

    @classmethod
    def isValidCard(cls, card):
        '''Check if the instance entered as an argument is a valid Card.'''
        return isinstance(card, Card) and card.__class__ != Card