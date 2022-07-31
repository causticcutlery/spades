from dealer import *
from hand_math import *
import csv

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

#Declares the deck as a list of two char strings. 
#Deck is based on the standard 54 card French suited playing cards with the Deuces of Hearts and Diamonds removed.
#Deck uses the Spades (game) ruleset of Joker Joker Deuce Ace (JJDA). Other variations might be Ace-high or Joker Joker Deuce Deuce.
deck = [Card(17, 'Big', 4, 'Spades', 'BS'),  Card(16, 'Little', 4, 'Spades', 'LS'),  Card(15, 'Deuce', 4, 'Spades', 'DS'),  Card(14, 'Ace', 4, 'Spades', 'AS'),  Card(13, 'King', 4, 'Spades', 'KS'),  Card(12, 'Queen', 4, 'Spades', 'QS'),  Card(11, 'Jack', 4, 'Spades', 'JS'),  Card(10, 'Ten', 4, 'Spades', 'TS'),  Card(9, 'Nine', 4, 'Spades', '9S'),  Card(8, 'Eight', 4, 'Spades', '8S'),  Card(7, 'Seven', 4, 'Spades', '7S'),  Card(6, 'Six', 4, 'Spades', '6S'),  Card(5, 'Five', 4, 'Spades', '5S'),  Card(4, 'Four', 4, 'Spades', '4S'),  Card(3, 'Three', 4, 'Spades', '3S'),  Card(14, 'Ace', 3, 'Hearts', 'AH'),  Card(13, 'King', 3, 'Hearts', 'KH'),  Card(12, 'Queen', 3, 'Hearts', 'QH'),  Card(11, 'Jack', 3, 'Hearts', 'JH'),  Card(10, 'Ten', 3, 'Hearts', 'TH'),  Card(9, 'Nine', 3, 'Hearts', '9H'),  Card(8, 'Eight', 3, 'Hearts', '8H'),  Card(7, 'Seven', 3, 'Hearts', '7H'),  Card(6, 'Six', 3, 'Hearts', '6H'),  Card(5, 'Five', 3, 'Hearts', '5H'),  Card(4, 'Four', 3, 'Hearts', '4H'),  Card(3, 'Three', 3, 'Hearts', '3H'),  Card(14, 'Ace', 2, 'Clubs', 'AC'),  Card(13, 'King', 2, 'Clubs', 'KC'),  Card(12, 'Queen', 2, 'Clubs', 'QC'),  Card(11, 'Jack', 2, 'Clubs', 'JC'),  Card(10, 'Ten', 2, 'Clubs', 'TC'),  Card(9, 'Nine', 2, 'Clubs', '9C'),  Card(8, 'Eight', 2, 'Clubs', '8C'),  Card(7, 'Seven', 2, 'Clubs', '7C'),  Card(6, 'Six', 2, 'Clubs', '6C'),  Card(5, 'Five', 2, 'Clubs', '5C'),  Card(4, 'Four', 2, 'Clubs', '4C'),  Card(3, 'Three', 2, 'Clubs', '3C'),  Card(2, 'Deuce', 2, 'Clubs', '2C'),  Card(14, 'Ace', 1, 'Diamonds', 'AD'),  Card(13, 'King', 1, 'Diamonds', 'KD'),  Card(12, 'Queen', 1, 'Diamonds', 'QD'),  Card(11, 'Jack', 1, 'Diamonds', 'JD'),  Card(10, 'Ten', 1, 'Diamonds', 'TD'),  Card(9, 'Nine', 1, 'Diamonds', '9D'),  Card(8, 'Eight', 1, 'Diamonds', '8D'),  Card(7, 'Seven', 1, 'Diamonds', '7D'),  Card(6, 'Six', 1, 'Diamonds', '6D'),  Card(5, 'Five', 1, 'Diamonds', '5D'),  Card(4, 'Four', 1, 'Diamonds', '4D'),  Card(3, 'Three', 1, 'Diamonds', '3D')]

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

#List of the four players of the game
players = [Player(0, "north", None), Player(1, "east", None), Player(2, "south", None), Player(3, "west", None)]

#Calls deal_cards from dealer.py to deal cards into four piles     
#Then calls assign_cards from dealer.py to assigns each pile to a player
players = assign_cards(players, deal_cards(deck))

#Creates a CSV file calculating stats from dealt hands
#Will simulate a number of games equal to the value of iterations
#CSV will contain the following values:
    #game: what game number the row belongs to
    #player: what position the player is in
    #hand: the hand dealt to the player
    #value: the value of the players hand, which includes context of their whole hand
    #average face value: the average face value of their hand based only on numerical value
    #nil chance: the chance that the player can go nil
    #misdeal: if the player was dealt no spades, misdeal is true
    #nil: if the player is better off going nil, nil is true
iterations = 1000
header = ["game","player","hand","value","average face value","nil chance","misdeal","nil"]
with open('data/data.csv', 'w', encoding='UTF8', newline='') as f:    
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range (iterations):
        print("Calculating game\t" + str(i) + "\tof\t" + str(iterations) + "\t. Percentage done: " + str(round((i/iterations),2)))
        players = assign_cards(players, deal_cards(deck))
        for player in players:
            value = count_value(player.hand)
            writer.writerow([i, player.position, ' '.join(player.hand_contents()), value[0], round(value[1],2), round(value[2],2), value[3], value[4]])
      
      
    
