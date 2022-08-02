from dealer import create_deck, assign_cards, create_players
from hand_math import count_value
from spades import simulate_game
import csv
import sys



def fill_csv(players, deck, iterations):
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
    header = ["game","player","hand","value","average face value","nil chance","books counted","misdeal","nil"]
    with open('data/data.csv', 'w', encoding='UTF8', newline='') as f:    
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range (iterations):
            print("Calculating game\t" + str(i+1) + "\tof\t" + str(iterations) + "\t. Percentage done: " + str(round((i/iterations),2)))
            players = assign_cards(players, deck)
            for player in players:
                value = count_value(player.hand)
                writer.writerow([i, player.position, ' '.join(player.hand_contents()), value[0], value[1], round(value[2],2), round(value[3],2), value[4], value[5]])
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
            print("Help TBD")
        #--csv to generate a csv with the provided amount of rows
        elif sys.argv[i] in ("--c", "--csv"):
            try:
                fill_csv(players, deck, int(sys.argv[i+1])) 
            except ValueError as err:
                print("Invalid input, provide a number")
                print("Error: " + str(err))
            except Exception as err:
                print("You broke something\n" + str(err))
        #--deck to specify which deck variation will be used
        #TODO: this
        elif sys.argv[i] in ("--d", "--deck"):
            print("Deck TBD")
        #--game to simulate a game
        elif sys.argv[i] in ("--g", "--game"):
            print("Game TBD\n")
            simulate_game(players)

    
    
if __name__ == "__main__":
    print(sys.argv)
    main()

