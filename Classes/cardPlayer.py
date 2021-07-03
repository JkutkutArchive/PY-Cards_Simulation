from card import Card

class CardPlayer:
    def __init__(self, name="") -> None:
        self._name = name
        self._hand = []


    # ########## GETTERS ##########

    def getHand(self) -> list:
        '''Return List with the cards in hand.'''
        return self._hand


    # ########## SETTERS ##########

    def takeCard(self, card):
        '''Adds the card to the hand.'''
        if not Card.isValidCard(card):
            raise Exception("The card is not valid")
        self.getHand().append(card)

    def useCard(self, index):
        '''Returns the removed card at the given index.'''
        if not isinstance(index, int) or index < 0 or index < len(self.getHand):
            raise Exception("The index is not a valid index.")
        
        return self.getHand().pop(index)