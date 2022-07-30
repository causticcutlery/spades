import random

#Declares the deck as a list of two char strings. Deck is based on the standard 54 card French suited playing cards with the Deuces of Hearts and Diamonds removed.
#Deck uses the Sapdes (game) ruleset of Joker Joker Deuce Ace (JJDA). Other variations might be Ace-high or Joker Joker Deuce Deuce.
#First char represents suit: S - Spades, H - Hearts, C - Clubs, D - Diamonds
#Second char represnts value: B - big joker, L - little joker, Ace, King, Queen, Jack, Ten, and 9-2. Note: 2 of Spades is the third joker (S2). 2C is low.
deck = ['SB', 'SL', 'S2', 'SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5', 'S4', 'S3', 'HA', 'HK', 'HQ', 'HJ', 'HT', 'H9', 'H8', 'H7', 'H6', 'H5', 'H4', 'H3', 'CA', 'CK', 'CQ', 'CJ', 'CT', 'C9', 'C8', 'C7', 'C6', 'C5', 'C4', 'C3', 'C2', 'DA', 'DK', 'DQ', 'DJ', 'DT', 'D9', 'D8', 'D7', 'D6', 'D5', 'D4', 'D3']

#Function to calculate the value of a hand
#Value is calculated on subjective values
#TODO: create a more objective rating system based on the chance a card takes a book
def count_value(hand):
  value=0
  
  countSpades = (len([card for card in hand if card[0]=="S"]))
  countHearts = (len([card for card in hand if card[0]=="H"]))
  countClubs = (len([card for card in hand if card[0]=="C"]))
  countDiamonds = (len([card for card in hand if card[0]=="D"]))
  countSuits = [['S','H','C','D'],[countSpades,countHearts,countClubs,countDiamonds]]
  
  for card in hand:
    #High spades are worth the most points
    if(card == "SB"):
      value+=6
    elif(card == "SL"):
      value+=5
    elif(card == "S2"):
      value+=4
    elif(card == "SA"):
      value+=3
    elif(card == "SK"):
      value+=2
    elif(card == "SQ"):
      value+=2
    #Accounts for the fact that high spades are worth less if it is the only one
    #This is due to the inability to protect a spade from being drawn out by a higher spade
    if(countSpades==1 and card != "SB"):
      value-=2
      
    #Value of an H/C/D A is normally worth 4
    #Value goes down by 1 for every additional card in the same suit over 3
    #This is because the more of a suit a hand has, the more likely it is for another player to cut with spades
    elif(card[1] == "A"):
      value+= 4-(countSuits[1][countSuits[0].index(card[0])]-3)
      '''
      if(card[0]=="H" and countHearts < 5):
        value+=3
      elif(card[0]=="C" and countHearts < 5):
        value+=3
      elif(card[0]=="D" and countHearts < 5):
        value+=3
      else:
        value+=2
      if(card[0]=="H" and countHearts < 5):
        value+=3
      elif(card[0]=="C" and countHearts < 5):
        value+=3
      elif(card[0]=="D" and countHearts < 5):
        value+=3
      else:
        value+=2
      if(card[0]=="H" and countClubs < 5):
        value+=3
      elif(card[0]=="C" and countClubs < 5):
        value+=3
      elif(card[0]=="D" and countClubs < 5):
        value+=3
      else:
        value+=2 
      '''
    #Value of an H/C/D K is normally worth 3
    #Value goes down by 1 for every additional card in the same suit over 2
    elif(card[1] == "K"):
      value+= 3-(countSuits[1][countSuits[0].index(card[0])]-2)
    #Value of an H/C/D Q is normally worth 2
    #Value goes down by 1 for every additional card in the same suit over 1
    elif(card[1] == "Q"):      
      value+= 2-(countSuits[1][countSuits[0].index(card[0])]-1)  
    
    #Hands that are void of H,C,D are worth 3 more if there are spades in the hand
    #Value increase is reduced by 1 for each card of that suit, zeroing off at 3 or more of a suit
    #This is due to the likelihood of cutting that suit with spades
    if(countHearts < 3 or countClubs < 3 or countDiamonds < 3):
      if(countSpades >= (3 - countHearts)):
        value += (3 - countHearts)
      else:
        value += (countSpades+1)
      if(countSpades >= (3 - countClubs)):
        value += (3 - countClubs)
      else:
        value += (countSpades+1)        
      if(countSpades >= (3 - countDiamonds)):
        value += (3 - countDiamonds)
      else:
        value += (countSpades+1)        
      
    #If a hand is dealt no spades, the player can call a miseal
    if(countSpades == 0):
      misdeal = True
      
      
      
      
      
      
      
      
      
      
      
      
      
      
    
