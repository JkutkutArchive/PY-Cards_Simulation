from .card import Card

class PokerCard(Card):
    SUIT = {
        "CLUBS": 0,
        "DIAMONDS": 1,
        "HEARTS": 2,
        "SPADES": 3
    }
    SUITNAME = ["Clubs", "Diamonds", "Hearts", "Spades"]
    RANK = {
        "MIN": 0, # 0 = Joker
        "MAX": 13,

        "JOKER": 0,
        "JACK": 11,
        "QUEEN": 12,
        "KING": 13
    }
    RANKNAME = {
        0: "Joker",
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King",
    }


    def __getRankPoint__(self):
        '''Internal method to stablish a point system to compare ranks of cards.'''
        if self.getRank() <= 1: # If ace or joker
            return 14
        else:
            return self.getRank()

    def compare(self, pokerCard):
        '''
        Compares the ranks of 2 cards.
        
        2 of clubs & 2 of diamonds => 0

        Ace of clubs & 2 of diamonds => >1

        2 of clubs & Ace of diamonds => <1
        '''
        if not isinstance(pokerCard, PokerCard):
            raise Exception(f"The card to compare is not a valid {self.__class__.__name__()}")
        
        return self.__getRankPoint__() - pokerCard.__getRankPoint__()