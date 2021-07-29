from Classes.card import Card

class PlayerHand:
    def __init__(self, name="") -> None:
        self._name = name
        self._hand = []


    # ########## GETTERS ##########

    def getHand(self) -> list:
        '''Return List with the cards in hand.'''
        return self._hand
    
    def seeCard(self, index):
        '''Returns the card at the given index.'''
        return self.getHand()[index]

    def getName(self) -> str:
        '''Returns the name of the player.'''
        return self._name
    
    def __str__(self) -> str:
        '''Returns string with the name and the cards of the player.'''
        cards = ',\n  '.join([c.__str__() for c in self.getHand()])
        return f"- {self.getName()}:\n[ {cards}\n]"

    # ########## SETTERS ##########

    def takeCard(self, card):
        '''Adds the card to the hand.'''
        if not Card.isValidCard(card):
            raise Exception("The card is not valid")
        self.getHand().append(card)

    def useCard(self, index=0):
        '''Returns the removed card at the given index.'''
        if not isinstance(index, int) or index < 0 or index >= len(self.getHand()):
            raise Exception("The index is not a valid index.")
        
        return self.getHand().pop(index)