import random

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

#Sorts the hand using random library
#TODO: Possibly add different shuffle techniques
#TODO: Possibly add cheating mechanics
def shuffle_deck(deck):
    random.shuffle(deck)

    return(deck)

#Function to assign the dealt cards to a list of 4 players
def assign_cards(players, hands):
    for i in range (len(players)):
        players[i].hand = hands[i]
    
    return(players)