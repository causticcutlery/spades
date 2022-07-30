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
        #Accounts for the fact that high spades are worth less if it is the only one
        #This is due to the inability to protect a spade from being drawn out by a higher spade
        if(card == "SB"):
            value+=6
        elif(card == "SL"):
            if(countSpades == 1):
                value+=3
            else:
                value+=5
        elif(card == "S2"):
            if(countSpades == 1):
                value+=2
            else:
                value+=4
        elif(card == "SA"):
            if(countSpades == 1):
                value+=1
            else:
                value+=3
        elif(card == "SK"):
            if(countSpades == 1):
                value+=0
            else:
                value+=2
        elif(card == "SQ"):
            if(countSpades == 1):
                value+=0
            else:
                value+=2

          
        #Value of an H/C/D A is normally worth 4
        #Value changes based on the amount of cards in that suit
        #This is because the more of a suit a hand has, the more likely it is for another player to cut with spades
        elif(card[1] == "A"):
            if((countSuits[1][countSuits[0].index(card[0]) <= 3):
                value+=4
            elif((countSuits[1][countSuits[0].index(card[0]) == 4):
                value+=2
            else:
                value+=0
            
        #Value of an H/C/D K is normally worth 3
        #Value changes based on the amount of cards in that suit
        elif(card[1] == "K"):
            if((countSuits[1][countSuits[0].index(card[0]) == 1):
                value+=0
            elif((countSuits[1][countSuits[0].index(card[0]) <= 3):
                value+=3
            elif((countSuits[1][countSuits[0].index(card[0]) == 4):
                value+=2
            else:
                value+=0
                
        #Value of an H/C/D Q is normally worth 2
        #Value changes based on the amount of cards in that suit
        elif(card[1] == "Q"):
            if((countSuits[1][countSuits[0].index(card[0]) <= 2):
                value+=0
            if((countSuits[1][countSuits[0].index(card[0]) == 3):
                value+=1
            else:
                value+=0
                
    #Hands that are void of H,C,D are worth 3 more if there are spades in the hand
    #Value increase is reduced by 1 for each card of that suit, zeroing off at 3 or more of a suit
    #This is due to the likelihood of cutting that suit with spades
    if(countHearts == 0):
        if(countSpades == 1):
            value += 4 
        elif(countSpades == 2):
            value += 6
        elif(countSpades == 3):
            value += 7  
    elif(countHearts == 1):
        if(countSpades == 1):
            value += 3 
        elif(countSpades == 2):
            value += 1
    elif(countHearts == 2):
        if(countSpades == 1):
            value += 1 
        
    if(countClubs == 0):
        if(countSpades == 1):
            value += 4 
        elif(countSpades == 2):
            value += 6
        elif(countSpades == 3):
            value += 7  
    elif(countClubs == 1):
        if(countSpades == 1):
            value += 3 
        elif(countSpades == 2):
            value += 1
    elif(countClubs == 2):
        if(countSpades == 1):
            value += 1 
            
    if(countDiamonds == 0):
        if(countSpades == 1):
            value += 4 
        elif(countSpades == 2):
            value += 6
        elif(countSpades == 3):
            value += 7  
    elif(countDiamonds == 1):
        if(countSpades == 1):
            value += 3 
        elif(countSpades == 2):
            value += 1
    elif(countDiamonds == 2):
        if(countSpades == 1):
            value += 1             

        #If a hand is dealt no spades, the player can call a miseal
    if(countSpades == 0):
        misdeal = True
    print(value)    
    return value
      
def deal_hand(deck):
    playerNorth = []
    playerEast = []
    playerSouth = []
    playerWest = []
    
    random.shuffle(deck)
    
    for i in range (len(deck)):
        if(i%4 == 0):
          playerNorth.append(deck[i])
        elif(i%4 == 1):
          playerEast.append(deck[i])
        elif(i%4 == 2):
          playerSouth.append(deck[i])
        elif(i%4 == 3):
          playerWest.append(deck[i])      
    
    playerNorth.sort()
    playerEast.sort()
    playerSouth.sort()
    playerWest.sort()
      
    return [playerNorth, playerEast, playerSouth, playerWest]
  
for i in range(100): 
    dealtCards = deal_hand(deck)
    playerNorth = dealtCards[0]
    playerEast = dealtCards[1]
    playerSouth = dealtCards[2]
    playerWest = dealtCards[3]
      
    print("Hand: " + ', '.join(playerNorth) + " | Value: " + str(count_value(playerNorth)))
    print("//////////////")
    print("Hand: " + ', '.join(playerEast) + " | Value: " + str(count_value(playerEast)))
    print("//////////////")
    print("Hand: " + ', '.join(playerSouth) + " | Value: " + str(count_value(playerSouth)))
    print("//////////////")
    print("Hand: " + ', '.join(playerWest) + " | Value: " + str(count_value(playerWest)))
    print("============================================================")
      
      
      
      
      
    
