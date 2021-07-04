import random
from Classes.card import Card, PokerCard, SpanishCard

class Deck:
    def __init__(self, cardType, suffle=True) -> None:
        if not Card.isValidCardClass(cardType):
            raise Exception("The card type selected is not valid")
        
        self._cT = cardType
        self._stack = []
        self.restartStack()

        if suffle:
            self.shuffleStack()
        
    
    # ########## GETTERS ##########

    def getStack(self) -> list:
        '''Returns a list with the current cards avalible on the stack.'''
        return self._stack

    def getCardClass(self):
        '''Class choosen for the deck'''
        return self._cT

    def getSuits(self) -> iter:
        '''Iterator with all the suits indices valid for the card type choosen'''
        return range(len(self.getCardClass().SUIT))
    
    def getRanks(self) -> iter:
        '''Iterator with all the rank indices valid for the card type choosen'''
        return range(self.getCardClass().RANK["MIN"], self.getCardClass().RANK["MAX"] + 1)

    def __str__(self) -> str:
        s = []
        indexing = "  "
        delimeter = ",\n"
        for c in self.getStack():
            s.append(f"{indexing}{c.__str__()}")
        return f"[\n{delimeter.join(s)}\n]"
        
    
    # ########## SETTERS ##########

    def takeCard(self, index=0) -> Card:
        '''Removes and returns a card from the stack. If empty, None is returned.'''
        if not isinstance(index, int) or index < 0 or index >= len(self.getStack()):
            raise Exception("The index is not valid.")
        if len(self.getStack()) == 0:
            return None
        return self.getStack().pop(index)


    def restartStack(self) -> None:
        '''Generates a new ordered stack of cards.'''
        self._stack = []
        for s in self.getSuits():
            for r in self.getRanks():
                self.getStack().append(self.getCardClass()(r, s))
    
    def restartShuffleStack(self) -> None:
        '''Generates a new random stack of cards.'''
        self.restartStack()
        self.shuffle()
    
    def shuffleStack(self) -> None:
        '''Shuffles the current stack of cards'''
        random.shuffle(self.getStack())
