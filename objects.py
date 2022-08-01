#Card is a class that is assigned the following attributes: 
    #a face value (for math functions)
    #a face (text of card face)
    #a suit value (for math functions)
    #a suit (spades, hearts, etc)
    #a abbreviation (4S, KA, etc.)
class Card:
    def __init__(self, faceValue, face, suitValue, suit, abbreviation):
        self.faceValue = faceValue
        self.face = face
        self.suitValue = suitValue
        self.suit = suit
        self.abbreviation = abbreviation

    def card_abbreviation(self):
        return(self.abbreviation)

#Player is a class that is assgned the following attributes:
    #a numerical value used to determine turn order
    #a position name (north, east, south, west)
    #a hand consisting of 13 cards
class Player:
    def __init__(self, value, position, hand):
        self.value = value
        self.position = position
        self.hand = hand

    def hand_contents(self):
        hand = []
        for card in self.hand:
            hand.append(card.card_abbreviation())
        return (hand)        