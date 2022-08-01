import random

#Function to simulate a game, given four players with hands
#TODO: Implement game theory
def simulate_game(players):
    lead = random.choice(players)

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