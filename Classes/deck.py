from Classes.card import Card, PokerCard, SpanishCard

class Deck:
    def __init__(self, cardType) -> None:
        if not issubclass(cardType, Card):
            raise Exception("The cardType must be a Card class.")
        if cardType.__class__ == Card:
            raise Exception("The cardType must not be the prototype, rather a children class of it.")
        
        self._cT = cardType
        self._stack = []
        for s in self.getSuits():
            for r in self.getRanks():
                self.getStack().append(cardType(r, s))
    
    # ########## GETTERS AND SETTERS ##########

    def getStack(self):
        return self._stack

    def getCardType(self):
        return self._cT

    def getSuits(self):
        return range(len(self.getCardType().SUIT))
    
    def getRanks(self):
        return range(self.getCardType().RANK["MIN"], self.getCardType().RANK["MAX"])

    def __str__(self) -> str:
        s = []
        indexing = "  "
        delimeter = ",\n"
        for c in self.getStack():
            s.append(f"{indexing}{c.__str__()}")
        print(f"[\n{delimeter.join(s)}\n]")
        
        