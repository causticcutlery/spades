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
    global misdeal 
    misdeal = False
    countedNil = False
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
            if((countSuits[1][countSuits[0].index(card[0])]) <= 3):
                value+=4
            elif((countSuits[1][countSuits[0].index(card[0])]) == 4):
                value+=2
            else:
                value+=0
            
        #Value of an H/C/D K is normally worth 3
        #Value changes based on the amount of cards in that suit
        elif(card[1] == "K"):
            if((countSuits[1][countSuits[0].index(card[0])]) == 1):
                value+=0
            elif((countSuits[1][countSuits[0].index(card[0])]) <= 3):
                value+=3
            elif((countSuits[1][countSuits[0].index(card[0])]) == 4):
                value+=2
            else:
                value+=0
                
        #Value of an H/C/D Q is normally worth 2
        #Value changes based on the amount of cards in that suit
        elif(card[1] == "Q"):
            if((countSuits[1][countSuits[0].index(card[0])]) <= 2):
                value+=0
            if((countSuits[1][countSuits[0].index(card[0])]) == 3):
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
    
    nilChance = calculate_nil_percentage(hand)
    
    #If nil is more likely, then return 20*nil chance as the hand value
    if(20*nilChance[0] > value):
        countedNil = True
    else:
        countedNil = False
    return [value, 20*nilChance[0],countedNil]
      
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
    
    #TODO sort based on deck list
    playerNorth.sort()
    playerEast.sort()
    playerSouth.sort()
    playerWest.sort()
      
    return [playerNorth, playerEast, playerSouth, playerWest]
  
def count_books(hand):
    #TODO
    return 0
  
def team():
    #TODO
    return 0
    
def calculate_nil_percentage(hand):
    #TODO
    
    
    voidSuit = False
    chance = 1.0
    sumFaceValue = 0
    countSpades = (len([card for card in hand if card[0]=="S"]))
    countHearts = (len([card for card in hand if card[0]=="H"]))
    countClubs = (len([card for card in hand if card[0]=="C"]))
    countDiamonds = (len([card for card in hand if card[0]=="D"]))
    countSuits = [['S','H','C','D'],[countSpades,countHearts,countClubs,countDiamonds]]
    if(countHearts == 0 or countClubs == 0 or countDiamonds == 0):
        voidSuit = True
        
    for card in hand:
        if(card == "SB"):
            sumFaceValue += 17       
        elif(card == "SL"):
            sumFaceValue += 16        
        elif(card == "S2"):
            sumFaceValue += 15        
        elif(card[1] == "A"):
            sumFaceValue += 14
        elif(card[1] == "K"):
            sumFaceValue += 13        
        elif(card[1] == "Q"):
            sumFaceValue += 12   
        elif(card[1] == "J"):
            sumFaceValue += 11   
        elif(card[1] == "T"):
            sumFaceValue += 10   
        elif(card[1] == "9"):
            sumFaceValue += 9   
        elif(card[1] == "8"):
            sumFaceValue += 8   
        elif(card[1] == "7"):
            sumFaceValue += 7   
        elif(card[1] == "6"):
            sumFaceValue += 6   
        elif(card[1] == "5"):
            sumFaceValue += 5   
        elif(card[1] == "4"):
            sumFaceValue += 4   
        elif(card[1] == "3"):
            sumFaceValue += 3   
        elif(card == "C2"):
            sumFaceValue += 2   
            
        averageFaceValue = sumFaceValue / 13
    
    #Starts with initial percentages based on the spades
    #Percentages pulled from Monty VanDover's "The Complete Book of Spades" section on "Probabilities of Distribution."
    if("SB" in hand):
        chance *= 0.0
    if("SL" in hand and "S2" in hand):
        chance *= 0.0
    if("S2" in hand and "SA" in hand and "SK" in hand):
        chance *= 0.0        
    if("SL" in hand):
        chance *= 0.33
    if("S2" in hand):
        chance *= 0.56
    if("SA" in hand):
        chance *= 0.70
    if("SK" in hand):
        chance *= 0.81
    if("SQ" in hand):
        chance *= 0.88
    if("S2" in hand and "SA" in hand):
        chance *= 0.11
    if(("S2" in hand and "SK" in hand) or ("SA" in hand and "SK" in hand)):
        chance *= 0.11
    if(("SA" in hand and "SQ" in hand) or ("SK" in hand and "SQ" in hand)):
        chance *= 0.41
    if(("SK" in hand and "SJ" in hand) or ("SQ" in hand and "SJ" in hand)):
        chance *= 0.55       
    if(("SA" in hand and "SK" in hand and "SJ" in hand) or ("SK" in hand and "SQ" in hand and "SJ" in hand)):
        chance *= 0.10
    if(("SK" in hand and "SQ" in hand and "ST" in hand) or ("SQ" in hand and "SJ" in hand and "ST" in hand)):
        chance *= 0.20
    if(("SQ" in hand and "SJ" in hand and "S9" in hand) or ("SJ" in hand and "ST" in hand and "S9" in hand)):
        chance *= 0.31           
   
    if("HA" in hand and countHearts == 1 and not voidSuit): 
        chance *= 0.0     
    if("CA" in hand and countClubs == 1 and not voidSuit):
        chance *= 0.0       
    if("DA" in hand and countDiamonds == 1 and not voidSuit):
        chance *= 0.0
    if("HK" in hand and countHearts == 1 and not voidSuit):
        chance *= 0.33        
    if("CK" in hand and countClubs == 1 and not voidSuit):
        chance *= 0.33        
    if("DK" in hand and countDiamonds == 1 and not voidSuit):
        chance *= 0.33         
    
    #todo make this more math
    if(countSpades >= 8):
        chance *= 0.0
    elif(countSpades >= 6):
        chance *= 0.2
    elif(countSpades >= 4):
        chance *= 0.6
    elif(countSpades >= 2):
        chance *= 0.8
    elif(countSpades == 0):
        chance *= 1.20
    #todo calculate average face Value
    
    std = 14
    mean = 113
    if(sumFaceValue < (mean-(std*3))):
        chance = 1.6
    elif(sumFaceValue < (mean-(std*2))):
        chance *= 1.4
    elif(sumFaceValue < (mean-(std*1))):
        chance *= 1.2
    elif(sumFaceValue < (mean)):
        chance *= 1.0
    elif(sumFaceValue < (mean+(std*1))):    
        chance *= 0.8
    elif(sumFaceValue < (mean+(std*2))):
        chance *= 0.6
    elif(sumFaceValue < (mean+(std*3))):
        chance *= 0.4
    else:
        chance *= 0.0
    
    if(chance > 1):
        chance = 1
    
    return [chance, sumFaceValue, averageFaceValue]


print("hand,round,value,nilchance,tooknil,player,misdeal,nil,sum,avg")
  
for i in range(10000): 
    dealtCards = deal_hand(deck)
    playerNorth = dealtCards[0]
    playerEast = dealtCards[1]
    playerSouth = dealtCards[2]
    playerWest = dealtCards[3]
     
    ''' 
    print("Hand: " + ', '.join(playerNorth) + " | Value: " + str(count_value(playerNorth)))
    print("//////////////")
    print("Hand: " + ', '.join(playerEast) + " | Value: " + str(count_value(playerEast)))
    print("//////////////")
    print("Hand: " + ', '.join(playerSouth) + " | Value: " + str(count_value(playerSouth)))
    print("//////////////")
    print("Hand: " + ', '.join(playerWest) + " | Value: " + str(count_value(playerWest)))
    print("============================================================")
    '''

    print(' '.join(playerNorth) + ', ' + str(i) + ', ' + str(count_value(playerNorth)[0]) + ', ' + str(count_value(playerNorth)[1]) + ', ' + str(count_value(playerNorth)[2]) + ', north' + ', ' + str(misdeal) + ', ' + str(calculate_nil_percentage(playerNorth)[0]) + ', ' + str(calculate_nil_percentage(playerNorth)[1]) + ', ' + str(calculate_nil_percentage(playerNorth)[2]))
    print(' '.join(playerEast) + ', ' + str(i) + ', ' + str(count_value(playerEast)[0]) + ', ' + str(count_value(playerNorth)[1]) + ', ' + str(count_value(playerNorth)[2]) + ', east' + ', ' + str(misdeal) + ', ' + str(calculate_nil_percentage(playerEast)[0]) + ', ' + str(calculate_nil_percentage(playerEast)[1]) + ', ' + str(calculate_nil_percentage(playerEast)[2]))
    print(' '.join(playerSouth) + ', ' + str(i) + ', ' + str(count_value(playerSouth)[0]) + ', ' + str(count_value(playerNorth)[1]) + ', ' + str(count_value(playerNorth)[2]) + ', south' + ', ' + str(misdeal) + ', ' + str(calculate_nil_percentage(playerSouth)[0]) + ', ' + str(calculate_nil_percentage(playerSouth)[1]) + ', ' + str(calculate_nil_percentage(playerSouth)[2]))
    print(' '.join(playerWest) + ', ' + str(i) + ', ' + str(count_value(playerWest)[0]) + ', ' + str(count_value(playerNorth)[1]) + ', ' + str(count_value(playerNorth)[2]) + ', west' + ', ' + str(misdeal) + ', ' + str(calculate_nil_percentage(playerWest)[0]) + ', ' + str(calculate_nil_percentage(playerWest)[1]) + ', ' + str(calculate_nil_percentage(playerWest)[2]))

    
      
      
      
    
