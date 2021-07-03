from card import Card

class cardPlayer:
    def __init__(self) -> None:
        self._name = ""
        self._hand = []

    def getHand(self) -> list:
        '''List with the cards in hand'''
        return self._hand