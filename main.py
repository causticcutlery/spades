from dealer import create_deck, assign_cards, create_players
from hand_math import count_value, count_books
from spades import simulate_round
import csv
import sys

#Creates a CSV file calculating stats from dealt hands
#Will simulate a number of games equal to the value of iterations
#CSV will contain the following values:
    #game: what game number the row belongs to
    #player: what position the player is in
    #hand: the hand dealt to the player
    #value: the value of the players hand, which includes context of their whole hand
    #books counted: the number of books the player counted on walking
    #average face value: the average face value of their hand based only on numerical value
    #nil chance: the chance that the player can go nil
    #misdeal: if the player was dealt no spades, misdeal is true
    #nil: if the player is better off going nil, nil is true
#TODO: Multithread this shit
def fill_csv(players, deck, iterations):
    header = ["game","player","hand","individual books counted","team books counted","total books counted","value","nil chance","average face value","misdeal","nil"]
    with open('data/data.csv', 'w', encoding='UTF8', newline='') as f:    
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range (iterations):
            if((i+1)%1000==0):
                print("Calculating game\t" + str(i+1) + "\tof\t" + str(iterations) + "\t. Percentage done: " + str(round((i/iterations),2)))
            players = assign_cards(players, deck)
            
            #count books
            books = []
            for player in players:
                books.append(count_books(player.hand))
            teamBooks = [(books[0]+books[2]),(books[1]+books[3])]
            totalBooks = sum(books)
            
            #count value and nil chances
            for j in range(0,4):
                value = count_value(players[j].hand)
                writer.writerow([i, players[j].position, ' '.join(players[j].hand_contents()), books[j], teamBooks[j%2], totalBooks, value[0], round(value[1]), round(value[2],2), value[3], value[4]])
    return 0            

def main():    
    #Create the deck, a list of card objects
    deck = create_deck("JJDA")

    #Creates the players for the game, which start with empty hands
    players = create_players()

    #Shuffles, deals, and assigns cards to players
    players = assign_cards(players, deck)

    for i in range(1,len(sys.argv)):
        #--help to display help screen
        #TODO: Make help screen
        if sys.argv[i] in ("--h", "--help"):
            f = open("readme.md", "r")
            print(f.read())
            break
        #--csv to generate a csv with the provided amount of rows
        elif sys.argv[i] in ("--c", "--csv"):
            try:
                fill_csv(players, deck, int(sys.argv[i+1]))
            except ValueError as err:
                print("Invalid input, provide a number")
                print("Error: " + str(err))
            except Exception as err:
                print("You broke something\n" + str(err))
                raise err
            break
        #--deck to specify which deck variation will be used
        #TODO: this
        elif sys.argv[i] in ("--d", "--deck"):
            if(sys.argv[i+1]=="JJDA"):
                deck = create_deck("JJDA")
            elif(sys.argv[i+1]=="JJDD"):
                deck = create_deck("JJDD")
            elif(sys.argv[i+1]=="A-High"):
                deck = create_deck("A-High")
            for card in deck:
                print(card.card_abbreviation())
            break
        #--game to simulate a game
        elif sys.argv[i] in ("--g", "--game"):
            print("Game TBD\n")
            simulate_round(players)
            break
        else:
            print("Argument not found. Try --help")
            break

    
    
if __name__ == "__main__":
    print(sys.argv)
    main()

