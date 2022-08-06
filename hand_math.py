#Function to calculate the value of a hand based on the full context of the hand
#Value is calculated on subjective values
#TODO: create a more objective rating system based on the chance a card takes a book
def count_value(hand):
    value=0
    misdeal = False
    countedNil = False

    #Tally up the count of each suit to save in a list that is used through this function
    countSuits = count_suits(hand)

    for card in hand:
        #High spades are worth the most points because they are likely to take books
        #Accounts for the fact that high spades are worth less if it is the only one spade in the hand
        #This is due to the inability to protect a spade from being drawn out by a higher spade 
        if(card.abbreviation == "BS"):
            value+=6
        elif(card.abbreviation == "LS"):
            if(countSuits[1][countSuits[0].index('Spades')] == 1):
                value+=3
            else:
                value+=5
        elif(card.abbreviation == "2S"):
            if(countSuits[1][countSuits[0].index('Spades')] == 1):
                value+=2
            else:
                value+=4
        elif(card.abbreviation == "AS"):
            if(countSuits[1][countSuits[0].index('Spades')] == 1):
                value+=1
            else:
                value+=3
        elif(card.abbreviation == "KS"):
            if(countSuits[1][countSuits[0].index('Spades')] == 1):
                value+=0
            else:
                value+=2
        elif(card.abbreviation == "QS"):
            if(countSuits[1][countSuits[0].index('Spades')] == 1):
                value+=0
            else:
                value+=2

          
        #Value of an A H/C/D  is normally worth 4, almost always book
        #Value changes based on the amount of cards in that suit
        #This is because the more of a suit a hand has, the more likely it is for another player to cut with spades
        elif(card.face == "Ace"):
            if(countSuits[1][card.suitValue] <= 3):
                value+=4
            elif(countSuits[1][card.suitValue] == 4):
                value+=2
            else:
                value+=0
            
        #Value of an K H/C/D is normally worth 3, most often a book
        #Value changes based on the amount of cards in that suit
        elif(card.face == "King"):
            if(countSuits[1][card.suitValue] == 1):
                value+=0
            elif(countSuits[1][card.suitValue] <= 3):
                value+=3
            elif(countSuits[1][card.suitValue] == 4):
                value+=2
            else:
                value+=0
                
        #Value of an Q H/C/D is normally worth 2, sometimes a book
        #Value changes based on the amount of cards in that suit
        elif(card.face == "Queen"):
            if(countSuits[1][card.suitValue] <= 2):
                value+=0
            if(countSuits[1][card.suitValue] == 3):
                value+=1
            else:
                value+=0
                
    #Hands that are void of H,C,D are worth 3 more if there are spades in the hand
    #Value increase is reduced by 1 for each card of that suit, zeroing off at 3 or more of a suit
    #This is due to the likelihood of cutting that suit with spades
    for i in range(0,5):
        if(countSuits[0][i] == ' ' or countSuits[0][i] == 'Spades'):
            continue
        elif(countSuits[1][i] == 0):
            if(countSuits[1][countSuits[0].index('Spades')] >= 1):
                value += 4 
                countSuits[1][countSuits[0].index('Spades')]-=1
            elif(countSuits[1][countSuits[0].index('Spades')] >= 2):
                value += 6
                countSuits[1][countSuits[0].index('Spades')]-=2
            elif(countSuits[1][countSuits[0].index('Spades')] >= 3):
                value += 7 
                countSuits[1][countSuits[0].index('Spades')]-=3
        elif(countSuits[1][i] == 1):
            if(countSuits[1][countSuits[0].index('Spades')] >= 1):
                value += 3 
                countSuits[1][countSuits[0].index('Spades')]-=1
            elif(countSuits[1][countSuits[0].index('Spades')] >= 2):
                value += 1
                countSuits[1][countSuits[0].index('Spades')]-=2
        elif(countSuits[1][i] == 2):
            if(countSuits[1][countSuits[0].index('Spades')] >= 1):
                value += 1 
                countSuits[1][countSuits[0].index('Spades')]-=1

    #If a hand is dealt no spades, the player can call a miseal
    if(countSuits[1][countSuits[0].index('Spades')] == 0):
        misdeal = True
    
    #Calculates the chance a player can go nil
    nilChance = calculate_nil_percentage(hand, countSuits)
    
    #If nil is more likely, then return 20*nil chance as the hand value
    #nilValue is a subjective value equal to how much a sucessful nil is worth
    nilValue=20
    if(nilValue*nilChance[0] > value):
        countedNil = True
    else:
        countedNil = False

    return [value, nilChance[0], nilChance[1], misdeal, countedNil]
  
def team():
    #TODO Create a function to take into consideration the team aspect
    return 0
    
#Function to calculate the chance a hand can sucessfully go nil
#Some portions of this function are based on math, such as the chance your partner can cover your highest spade
#Other portions are based on feeling and are subjective
def calculate_nil_percentage(hand, countSuits):
    
    #Nil chance starts off at 100% and is modified based on hand contents
    chance = 1.0
    sumFaceValue = 0
    
    #Void is when a hand has none of a suit
    #In nil, being void on hearts, diamonds, or clubs is extremely useful
    #Being void can mean that having a high non-spade is no longer as dangerous
    voidSuit = False
    if(countSuits[1][1] == 0 or countSuits[1][2] == 0 or countSuits[1][3] == 0):
        voidSuit = True
        
    for card in hand:
        sumFaceValue += card.faceValue
    averageFaceValue = sumFaceValue / 13
    
    #Starts with initial percentages based on the spades
    #Percentages pulled from Monty VanDover's "The Complete Book of Spades" section on "Probabilities of Distribution."
    if(has_card(hand,"BS")):
        chance *= 0.0
    elif(has_card(hand,"LS") and has_card(hand,"2S")):
        chance *= 0.0
    elif(has_card(hand,"2S") and has_card(hand,"AS") and has_card(hand,"KS")):
        chance *= 0.0        
    elif(has_card(hand,"LS")):
        chance *= 0.33
    elif(has_card(hand,"2S")):
        chance *= 0.56
    elif(has_card(hand,"AS")):
        chance *= 0.70
    elif(has_card(hand,"KS")):
        chance *= 0.81
    elif(has_card(hand,"QS")):
        chance *= 0.88
    elif(has_card(hand,"2S") and has_card(hand,"AS")):
        chance *= 0.11
    elif((has_card(hand,"2S") and has_card(hand,"KS")) or (has_card(hand,"AS") and has_card(hand,"KS"))):
        chance *= 0.11
    elif((has_card(hand,"AS") and has_card(hand,"QS")) or (has_card(hand,"KS") and has_card(hand,"QS"))):
        chance *= 0.41
    elif((has_card(hand,"KS") and has_card(hand,"JS")) or (has_card(hand,"QS") and has_card(hand,"JS"))):
        chance *= 0.55       
    elif((has_card(hand,"AS") and has_card(hand,"KS") and has_card(hand,"JS")) or (has_card(hand,"KS") and has_card(hand,"QS") and has_card(hand,"JS"))):
        chance *= 0.10
    elif((has_card(hand,"KS") and has_card(hand,"QS") and has_card(hand,"TS")) or (has_card(hand,"QS") and has_card(hand,"JS") and has_card(hand,"TS"))):
        chance *= 0.20
    elif((has_card(hand,"QS") and has_card(hand,"JS") and has_card(hand,"9S")) or (has_card(hand,"JS") and has_card(hand,"TS") and has_card(hand,"9S"))):
        chance *= 0.31           
    
    #Similar to the above spades statistics. There exists scenarios outside of what is being accounted for here
    #Therefore these statistics are not 100% accurate, but should be close enough
    if(has_card(hand,"AH") and countSuits[1][countSuits[0].index('Hearts')] == 1 and not voidSuit): 
        chance *= 0.0     
    if(has_card(hand,"AC") and countSuits[1][countSuits[0].index('Clubs')] == 1 and not voidSuit):
        chance *= 0.0       
    if(has_card(hand,"AD") and countSuits[1][countSuits[0].index('Diamonds')] == 1 and not voidSuit):
        chance *= 0.0
    if(has_card(hand,"KH") and countSuits[1][countSuits[0].index('Hearts')] == 1 and not voidSuit):
        chance *= 0.33        
    if(has_card(hand,"KC") and countSuits[1][countSuits[0].index('Clubs')] == 1 and not voidSuit):
        chance *= 0.33        
    if(has_card(hand,"KD") and countSuits[1][countSuits[0].index('Diamonds')] == 1 and not voidSuit):
        chance *= 0.33         
    
    #Adjusts nil chance based on the amount of spades in a hand
    #TODO make this more math by determining stats of spades distribution
    if(countSuits[1][countSuits[0].index('Spades')] >= 8):
        chance *= 0.0
    elif(countSuits[1][countSuits[0].index('Spades')] >= 6):
        chance *= 0.2
    elif(countSuits[1][countSuits[0].index('Spades')] >= 4):
        chance *= 0.6
    elif(countSuits[1][countSuits[0].index('Spades')] >= 2):
        chance *= 0.8
    elif(countSuits[1][countSuits[0].index('Spades')] == 0):
        chance *= 1.20
    
    #Uses the distribution of face value sums to adjust the nil bet accordingly
    #TODO tighen up the percentages, while based on mathematical figures, they are not implemented mathematically
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
    
    #Cuts off any nil over 100%
    if(chance > 1):
        chance = 1
    
    return [chance, averageFaceValue]

#Function use to determine if a hand contains a certain card
#Searches by the card's abbreviation, e.g., "SB, AH, TC"
def has_card(hand, cardToCheck):
    for card in hand:
        if(card.abbreviation == cardToCheck):
            return True
    return False

#Function to tally up the count of each suit to save in a list that is used in other calculations
def count_suits(hand):
    countSpades = (len([card for card in hand if card.suit=="Spades"]))
    countHearts = (len([card for card in hand if card.suit=="Hearts"]))
    countClubs = (len([card for card in hand if card.suit=="Clubs"]))
    countDiamonds = (len([card for card in hand if card.suit=="Diamonds"]))
    countSuits = [[' ', 'Diamonds','Clubs','Hearts','Spades'],[13, countDiamonds, countClubs, countHearts, countSpades]]

    return countSuits

#Function to count the books in a hand
#Logic is very similar to what is used in count_value
def count_books(hand):
    books=0
    countSuits = count_suits(hand)
    
    for card in hand:
        #High spades are worth the most points because they are likely to take books
        #Accounts for the fact that high spades are worth less if it is the only one spade in the hand
        #This is due to the inability to protect a spade from being drawn out by a higher spade 
        if(card.abbreviation == "BS"):
            books+=1
        elif(card.abbreviation == "LS"):
            if(countSuits[1][countSuits[0].index('Spades')] == 1):
                books+=0.5
            else:
                books+=1
                countSuits[1][4]-=1
        elif(card.abbreviation == "2S"):
            if(countSuits[1][countSuits[0].index('Spades')] == 1):
                books+=0.5
            else:
                books+=1
                countSuits[1][countSuits[0].index('Spades')]-=1
        
        #A H/C/D  is  almost always book
        #Value changes based on the amount of cards in that suit
        #This is because the more of a suit a hand has, the more likely it is for another player to cut with spades
        if(card.face == "Ace"):
            if(countSuits[1][card.suitValue] <= 4):
                books+=1
            elif(countSuits[1][card.suitValue] == 5):
                books+=0.5
            else:
                books+=0
            
        #K H/C/D is most often a book
        #Value changes based on the amount of cards in that suit
        if(card.face == "King"):
            if(countSuits[1][card.suitValue] == 1):
                books+=0
            elif(countSuits[1][card.suitValue] <= 3):
                books+=1
            elif(countSuits[1][card.suitValue] == 4):
                books+=0.5
            else:
                books+=0

    #Hands that are void of H,C,D are likely to take books by cutting
    for i in range(0,5):
        if(countSuits[0][i] == ' ' or countSuits[0][i] == 'Spades'):
            continue
        elif(countSuits[1][i] == 0):
            if(countSuits[1][countSuits[0].index('Spades')] >= 1):
                books+=1
                countSuits[1][countSuits[0].index('Spades')]-=1
            elif(countSuits[1][countSuits[0].index('Spades')] >= 2):
                books+=2
                countSuits[1][countSuits[0].index('Spades')]-=2
            elif(countSuits[1][countSuits[0].index('Spades')] >= 3):
                books+=3
                countSuits[1][countSuits[0].index('Spades')]-=3
        elif(countSuits[1][i] == 1):
            if(countSuits[1][countSuits[0].index('Spades')] >= 1):
                books+=1
                countSuits[1][countSuits[0].index('Spades')]-=1
            elif(countSuits[1][countSuits[0].index('Spades')] >= 2):
                books+=2
                countSuits[1][countSuits[0].index('Spades')]-=2
        elif(countSuits[1][i] == 2):
            if(countSuits[1][countSuits[0].index('Spades')] >= 1):
                books+=1 
                countSuits[1][countSuits[0].index('Spades')]-=1

    return round(books)