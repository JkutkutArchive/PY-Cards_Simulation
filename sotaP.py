from Classes.deck import Deck
from Classes.card import Card, SpanishCard
from Classes.cardPlayer import CardPlayer
from Classes.deck import Deck

class SotaP:
    def __init__(self, nPlayers) -> None:
        if not isinstance(nPlayers, int) or nPlayers < 1:
            raise Exception("Number of players invalid")
        
        self._players = [] # Create player list
        for i in range(nPlayers):
            self.getPlayers().append(CardPlayer(f"Player{i+1}"))

        deck = Deck(SpanishCard)
        # deck.shuffleStack()

        # Give all cards to the players
        index = 0
        while len(deck.getStack()) > 0: # While there're cards left to give
            self.getPlayers()[index].takeCard(deck.takeCard()) # Give card to player
            index = (index + 1) % nPlayers # Select next player


        self._tableStack = []


    
    # ########## GETTERS ##########
    
    def getPlayers(self) -> list:
        '''Returns a list with the players in the game'''
        return self._players


    def printPlayers(self):
        '''Prints the current status of the players'''
        for i in range(len(self.getPlayers())):
            print(self.getPlayers()[i])

    def getTableStack(self):
        '''Return a list of all the cards on the "table".'''
        return self._tableStack


    # ########## SETTERS ##########

    def giveTableCardsTo(self, playerIndex):
        if not isinstance(playerIndex) or playerIndex < 0 or playerIndex >= len(self.getPlayers()):
            raise Exception("The index of the player is not valid")
        while len(self.getTableStack()) > 0: # Give all cards to the player
            self.getPlayers()[playerIndex].takeCard(self.getTableStack().pop())
