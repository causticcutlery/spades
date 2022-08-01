import random
from objects import Card, Player

#Function to deal cards into four seperate piles
#Will deal cards one hand at a time, a traditional dealing method
#Then sorts the hands, grouped by suits
def deal_cards(deck):
    hands = [[],[],[],[]]
    
    shuffle_deck(deck)
    
    for i in range (len(deck)):
        if(i%4 == 0):
          hands[i%4].append(deck[i])
        elif(i%4 == 1):
          hands[i%4].append(deck[i])
        elif(i%4 == 2):
          hands[i%4].append(deck[i])
        elif(i%4 == 3):
          hands[i%4].append(deck[i])      

    for hand in hands:
        hand = hand.sort(key=lambda x: (-x.suitValue, -x.faceValue))
      
    return(hands)

#Function to create a list of Card objects
#Deck is based on the standard 54 card French suited playing cards with the Deuces of Hearts and Diamonds removed.
#Deck uses the Spades (game) ruleset of Joker Joker Deuce Ace (JJDA). Other variations might be Ace-high or Joker Joker Deuce Deuce.
#Other variations are not supported, but are added here as a proof of concept
#TODO: Initiate the deck with a for loop
def create_deck(ruleset):
  if(ruleset == "JJDA"):
    deck = [Card(17, 'Big', 4, 'Spades', 'BS'),  Card(16, 'Little', 4, 'Spades', 'LS'),  Card(15, 'Deuce', 4, 'Spades', 'DS'),  Card(14, 'Ace', 4, 'Spades', 'AS'),  Card(13, 'King', 4, 'Spades', 'KS'),  Card(12, 'Queen', 4, 'Spades', 'QS'),  Card(11, 'Jack', 4, 'Spades', 'JS'),  Card(10, 'Ten', 4, 'Spades', 'TS'),  Card(9, 'Nine', 4, 'Spades', '9S'),  Card(8, 'Eight', 4, 'Spades', '8S'),  Card(7, 'Seven', 4, 'Spades', '7S'),  Card(6, 'Six', 4, 'Spades', '6S'),  Card(5, 'Five', 4, 'Spades', '5S'),  Card(4, 'Four', 4, 'Spades', '4S'),  Card(3, 'Three', 4, 'Spades', '3S'),  Card(14, 'Ace', 3, 'Hearts', 'AH'),  Card(13, 'King', 3, 'Hearts', 'KH'),  Card(12, 'Queen', 3, 'Hearts', 'QH'),  Card(11, 'Jack', 3, 'Hearts', 'JH'),  Card(10, 'Ten', 3, 'Hearts', 'TH'),  Card(9, 'Nine', 3, 'Hearts', '9H'),  Card(8, 'Eight', 3, 'Hearts', '8H'),  Card(7, 'Seven', 3, 'Hearts', '7H'),  Card(6, 'Six', 3, 'Hearts', '6H'),  Card(5, 'Five', 3, 'Hearts', '5H'),  Card(4, 'Four', 3, 'Hearts', '4H'),  Card(3, 'Three', 3, 'Hearts', '3H'),  Card(14, 'Ace', 2, 'Clubs', 'AC'),  Card(13, 'King', 2, 'Clubs', 'KC'),  Card(12, 'Queen', 2, 'Clubs', 'QC'),  Card(11, 'Jack', 2, 'Clubs', 'JC'),  Card(10, 'Ten', 2, 'Clubs', 'TC'),  Card(9, 'Nine', 2, 'Clubs', '9C'),  Card(8, 'Eight', 2, 'Clubs', '8C'),  Card(7, 'Seven', 2, 'Clubs', '7C'),  Card(6, 'Six', 2, 'Clubs', '6C'),  Card(5, 'Five', 2, 'Clubs', '5C'),  Card(4, 'Four', 2, 'Clubs', '4C'),  Card(3, 'Three', 2, 'Clubs', '3C'),  Card(2, 'Deuce', 2, 'Clubs', '2C'),  Card(14, 'Ace', 1, 'Diamonds', 'AD'),  Card(13, 'King', 1, 'Diamonds', 'KD'),  Card(12, 'Queen', 1, 'Diamonds', 'QD'),  Card(11, 'Jack', 1, 'Diamonds', 'JD'),  Card(10, 'Ten', 1, 'Diamonds', 'TD'),  Card(9, 'Nine', 1, 'Diamonds', '9D'),  Card(8, 'Eight', 1, 'Diamonds', '8D'),  Card(7, 'Seven', 1, 'Diamonds', '7D'),  Card(6, 'Six', 1, 'Diamonds', '6D'),  Card(5, 'Five', 1, 'Diamonds', '5D'),  Card(4, 'Four', 1, 'Diamonds', '4D'),  Card(3, 'Three', 1, 'Diamonds', '3D')]
  elif(ruleset == "JJDD"):
    deck = [Card(18, 'Big', 4, 'Spades', 'BS'),  Card(17, 'Little', 4, 'Spades', 'LS'),  Card(16, 'Deuce', 4, 'Diamonds', 'DD'),  Card(15, 'Deuce', 4, 'Spades', 'DS'), Card(14, 'Ace', 4, 'Spades', 'AS'),  Card(13, 'King', 4, 'Spades', 'KS'),  Card(12, 'Queen', 4, 'Spades', 'QS'),  Card(11, 'Jack', 4, 'Spades', 'JS'),  Card(10, 'Ten', 4, 'Spades', 'TS'),  Card(9, 'Nine', 4, 'Spades', '9S'),  Card(8, 'Eight', 4, 'Spades', '8S'),  Card(7, 'Seven', 4, 'Spades', '7S'),  Card(6, 'Six', 4, 'Spades', '6S'),  Card(5, 'Five', 4, 'Spades', '5S'),  Card(4, 'Four', 4, 'Spades', '4S'),  Card(3, 'Three', 4, 'Spades', '3S'),  Card(14, 'Ace', 3, 'Hearts', 'AH'),  Card(13, 'King', 3, 'Hearts', 'KH'),  Card(12, 'Queen', 3, 'Hearts', 'QH'),  Card(11, 'Jack', 3, 'Hearts', 'JH'),  Card(10, 'Ten', 3, 'Hearts', 'TH'),  Card(9, 'Nine', 3, 'Hearts', '9H'),  Card(8, 'Eight', 3, 'Hearts', '8H'),  Card(7, 'Seven', 3, 'Hearts', '7H'),  Card(6, 'Six', 3, 'Hearts', '6H'),  Card(5, 'Five', 3, 'Hearts', '5H'),  Card(4, 'Four', 3, 'Hearts', '4H'),  Card(3, 'Three', 3, 'Hearts', '3H'),  Card(14, 'Ace', 2, 'Clubs', 'AC'),  Card(13, 'King', 2, 'Clubs', 'KC'),  Card(12, 'Queen', 2, 'Clubs', 'QC'),  Card(11, 'Jack', 2, 'Clubs', 'JC'),  Card(10, 'Ten', 2, 'Clubs', 'TC'),  Card(9, 'Nine', 2, 'Clubs', '9C'),  Card(8, 'Eight', 2, 'Clubs', '8C'),  Card(7, 'Seven', 2, 'Clubs', '7C'),  Card(6, 'Six', 2, 'Clubs', '6C'),  Card(5, 'Five', 2, 'Clubs', '5C'),  Card(4, 'Four', 2, 'Clubs', '4C'),  Card(3, 'Three', 2, 'Clubs', '3C'),  Card(14, 'Ace', 1, 'Diamonds', 'AD'),  Card(13, 'King', 1, 'Diamonds', 'KD'),  Card(12, 'Queen', 1, 'Diamonds', 'QD'),  Card(11, 'Jack', 1, 'Diamonds', 'JD'),  Card(10, 'Ten', 1, 'Diamonds', 'TD'),  Card(9, 'Nine', 1, 'Diamonds', '9D'),  Card(8, 'Eight', 1, 'Diamonds', '8D'),  Card(7, 'Seven', 1, 'Diamonds', '7D'),  Card(6, 'Six', 1, 'Diamonds', '6D'),  Card(5, 'Five', 1, 'Diamonds', '5D'),  Card(4, 'Four', 1, 'Diamonds', '4D'),  Card(3, 'Three', 1, 'Diamonds', '3D')]
  elif(ruleset == "A-High"):
    deck = [Card(14, 'Ace', 4, 'Spades', 'AS'),  Card(13, 'King', 4, 'Spades', 'KS'),  Card(12, 'Queen', 4, 'Spades', 'QS'),  Card(11, 'Jack', 4, 'Spades', 'JS'),  Card(10, 'Ten', 4, 'Spades', 'TS'),  Card(9, 'Nine', 4, 'Spades', '9S'),  Card(8, 'Eight', 4, 'Spades', '8S'),  Card(7, 'Seven', 4, 'Spades', '7S'),  Card(6, 'Six', 4, 'Spades', '6S'),  Card(5, 'Five', 4, 'Spades', '5S'),  Card(4, 'Four', 4, 'Spades', '4S'),  Card(3, 'Three', 4, 'Spades', '3S'), Card(2, 'Deuce', 4, 'Spades', '2S'),  Card(14, 'Ace', 3, 'Hearts', 'AH'),  Card(13, 'King', 3, 'Hearts', 'KH'),  Card(12, 'Queen', 3, 'Hearts', 'QH'),  Card(11, 'Jack', 3, 'Hearts', 'JH'),  Card(10, 'Ten', 3, 'Hearts', 'TH'),  Card(9, 'Nine', 3, 'Hearts', '9H'),  Card(8, 'Eight', 3, 'Hearts', '8H'),  Card(7, 'Seven', 3, 'Hearts', '7H'),  Card(6, 'Six', 3, 'Hearts', '6H'),  Card(5, 'Five', 3, 'Hearts', '5H'),  Card(4, 'Four', 3, 'Hearts', '4H'),  Card(3, 'Three', 3, 'Hearts', '3H'), Card(2, 'Deuce', 3, 'Hearts', '2S'), Card(14, 'Ace', 2, 'Clubs', 'AC'),  Card(13, 'King', 2, 'Clubs', 'KC'),  Card(12, 'Queen', 2, 'Clubs', 'QC'),  Card(11, 'Jack', 2, 'Clubs', 'JC'),  Card(10, 'Ten', 2, 'Clubs', 'TC'),  Card(9, 'Nine', 2, 'Clubs', '9C'),  Card(8, 'Eight', 2, 'Clubs', '8C'),  Card(7, 'Seven', 2, 'Clubs', '7C'),  Card(6, 'Six', 2, 'Clubs', '6C'),  Card(5, 'Five', 2, 'Clubs', '5C'),  Card(4, 'Four', 2, 'Clubs', '4C'),  Card(3, 'Three', 2, 'Clubs', '3C'), Card(2, 'Deuce', 2, 'Clubs', '2S'),  Card(14, 'Ace', 1, 'Diamonds', 'AD'),  Card(13, 'King', 1, 'Diamonds', 'KD'),  Card(12, 'Queen', 1, 'Diamonds', 'QD'),  Card(11, 'Jack', 1, 'Diamonds', 'JD'),  Card(10, 'Ten', 1, 'Diamonds', 'TD'),  Card(9, 'Nine', 1, 'Diamonds', '9D'),  Card(8, 'Eight', 1, 'Diamonds', '8D'),  Card(7, 'Seven', 1, 'Diamonds', '7D'),  Card(6, 'Six', 1, 'Diamonds', '6D'),  Card(5, 'Five', 1, 'Diamonds', '5D'),  Card(4, 'Four', 1, 'Diamonds', '4D'),  Card(3, 'Three', 1, 'Diamonds', '3D'), Card(2, 'Deuce', 1, 'Diamonds', '2S')]
  return deck

#Spades is played with four players, two of each play on a team
#Teammates sit across from each other, 
  #the even players are one team (north, south)
  #the odd players are the second team (east,west)
def create_players():
  players = [Player(0, "north", None), Player(1, "east", None), Player(2, "south", None), Player(3, "west", None)]
  return players

#Sorts the hand using random library
#TODO: Possibly add different shuffle techniques
#TODO: Possibly add cheating mechanics
def shuffle_deck(deck):
    random.shuffle(deck)

    return(deck)

#Function to assign the dealt cards to a list of 4 players
#Takes an input of players, typically with empty hands and returns them with hands of dealt cards
def assign_cards(players, deck):
    hands = deal_cards(deck)
    
    for i in range (len(players)):
        players[i].hand = hands[i]
    
    return(players)

