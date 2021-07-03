import random
from Classes.card import Card, PokerCard, SpanishCard

class Deck:
    def __init__(self, cardType) -> None:
        if not issubclass(cardType, Card):
            raise Exception("The cardType must be a Card class.")
        if cardType.__class__ == Card:
            raise Exception("The cardType must not be the prototype, rather a children class of it.")
        
        self._cT = cardType
        self._stack = []
        self.restartStack()
        
    
    # ########## GETTERS ##########

    def getStack(self):
        return self._stack

    def getCardClass(self):
        return self._cT

    def getSuits(self):
        return range(len(self.getCardClass().SUIT))
    
    def getRanks(self):
        return range(self.getCardClass().RANK["MIN"], self.getCardClass().RANK["MAX"] + 1)

    def __str__(self) -> str:
        s = []
        indexing = "  "
        delimeter = ",\n"
        for c in self.getStack():
            s.append(f"{indexing}{c.__str__()}")
        return f"[\n{delimeter.join(s)}\n]"
        
    # ########## SETTERS ##########
    def restartStack(self):
        self._stack = []
        for s in self.getSuits():
            for r in self.getRanks():
                self.getStack().append(self.getCardClass()(r, s))
    
    def restartShuffleStack(self):
        self.restartStack()
        self.shuffle()
    
    def shuffleStack(self):
        random.shuffle(self.getStack())
