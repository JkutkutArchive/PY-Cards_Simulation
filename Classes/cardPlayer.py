from card import Card

class cardPlayer:
    def __init__(self) -> None:
        self._name = ""
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