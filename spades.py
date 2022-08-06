import random
from hand_math import count_books 

#Function to simulate a a single round, given four players with hands
#TODO: Implement game theory
def simulate_round(players):
    lead = random.choice(players)

    print("Betting")
    print("%s has %s and bets %s." %(str(lead.position), str(players[lead.value].hand_contents()), str(count_books(players[lead.value].hand))))
    print("%s has %s and bets %s." %(str(players[(lead.value+1)%4].position), str(players[(lead.value+1)%4].hand_contents()), str(count_books(players[(lead.value+1)%4].hand))))
    print("%s has %s and bets %s." %(str(players[(lead.value+2)%4].position), str(players[(lead.value+2)%4].hand_contents()), str(count_books(players[(lead.value+2)%4].hand))))
    print("%s has %s and bets %s." %(str(players[(lead.value+3)%4].position), str(players[(lead.value+3)%4].hand_contents()), str(count_books(players[(lead.value+3)%4].hand))))
    print("")

    for i in range(0,12):
        cardsPlayed=[players[lead.value].hand[i], players[(lead.value+1)%4].hand[i], players[(lead.value+2)%4].hand[i], players[(lead.value+3)%4].hand[i]]
        highCard = determine_winner(cardsPlayed)
        print("%s leads with %s." %(str(lead.position), str(cardsPlayed[0].abbreviation)))
        print("%s responds with %s." %(str(players[(lead.value+1)%4].position), str(cardsPlayed[1].abbreviation)))
        print("%s responds with %s." %(str(players[(lead.value+2)%4].position), str(cardsPlayed[2].abbreviation)))
        print("%s responds with %s." %(str(players[(lead.value+3)%4].position), str(cardsPlayed[3].abbreviation)))
        print("%s won with the %s." %(next((x for x in players if x.hand[i] == highCard)).position, highCard.abbreviation))
        print("")

        lead = next((x for x in players if x.hand[i] == highCard))
    
    northsouthBooksTaken = 0
    eastwestBooksTaken = 0
    
    results = {"northsouthBooksTaken": northsouthBooksTaken, "eastwestBooksTaken": eastwestBooksTaken}
 
    return(results)

#Function to simulate a game, given four players with hands.
def simulate_game(players):
    #Dealer is chosen randomly
    dealer = random.choice(players)

    #The lead player is in the position to the left of the dealer
    lead = players[(dealer.value+1)%4]

    #Conditions of the game. This ruleset ends the game when a teach reaches 500 or -250.
    maxScore = 500
    minScore = -250
    gamesPlayed = 0

    northsouthScore = 0
    eastwestScore = 0

    

    #Conditions of the game.
    while (northsouthScore > maxScore or northsouthScore < minScore or eastwestScore > maxScore or eastwestScore < minScore):
        #First hand plays itself (no betting)
        if(gamesPlayed == 0):
            #Save results of round as a dict
            results = simulate_round(players)

            #Calculate scores from first game
            northsouthScore = results['northsouthBooksTaken']
            eastwestScore = results['eastwestBooksTaken']

            #Dealer rotates to the player to the left
            dealer = players[(dealer.value+1)%4]
        else:
            northsouthBet = 0
            eastwestBet = 0
            
            for player in players:
                if (player.position == "north" or player.position == "south"):
                    northsouthBet += count_books(player.hand)
                if (player.position == "east" or player.position == "west"):
                    eastwestBet += count_books(player.hand)                    

            results = simulate_round(players)
            
            #Potential good use of a "for players in team" loop, making use of a currently unused Team class
            #Counts the score based on betting made.
            #Taking less books than what was bet is called a set, and the team is deducted the bet*10
            #Taking the exact amount of what was bet is making the bet, and awards the team the bet*10
            #Taking more books than what was bet still grants the bet*10, but a single penalty per extra book
                #Accuring 10 of these penalties, or 'sandbags', results in a deduction of 100 points.
            #TODO Change bag calculation
            if(results['northsouthBooksTaken'] >= northsouthBet):
                northsouthScore += (northsouthBet*10) + (results['northsouthBooksTaken'] - northsouthBet)
            elif(results['northsouthBooksTaken'] < northsouthBet):
                northsouthScore -= (northsouthBet*10)
            


            if(results['eastwestBooksTaken'] >= eastwestBet):
                eastwestScore += (eastwestBet*10) + (results['eastwestBooksTaken'] - eastwestBet)
            elif(results['eastwestBooksTaken'] < eastwestBet):
                eastwestScore -= (eastwestBet*10)

            



#Function to determine the winning card out of the cards played
#In Spades, the highest card on the table that matches the lead suit takes the book
#Spades are trump suits, and will win over any non-spade or lower spade
def determine_winner(cardsPlayed):
    leadSuit = cardsPlayed[0].suit
    highCard = cardsPlayed[0]
    
    for card in cardsPlayed:
        if(card == highCard):
            continue
        elif(card.suit == leadSuit and card.faceValue > highCard.faceValue):
            highCard = card
        elif(card.suit == "Spades"):
            if(highCard.suit != "Spades"):
                highCard = card
            elif(highCard.suit == "Spades" and card.faceValue > highCard.faceValue):
                highCard = card


    return highCard