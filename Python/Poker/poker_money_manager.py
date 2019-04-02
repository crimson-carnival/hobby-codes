from os import system, name 

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is '5posix') 
    else: 
        _ = system('clear')

class Player:
    def __init__(self):
        self.name = ''
        self.purse = 0
        self.fold = False

clear()
print('\n--------Welcome to Poker money manager--------\n\nThanks to virtual money, you can enjoy this game without actually going broke!\n\n---------------Happy gambling!!---------------\n')
choice = 'y'
number_of_players = int(input("\nEnter the number of players: "))
player = [Player() for i in range(0, number_of_players)]
print()

for i in range(0, number_of_players):
    player[i].name = input("Enter name of player " + str(i+1) + ": ")

type_of_bank = int(input('\n1. Same initial bank for all players.\n2. Custom bank for each.\nChoice: '))
if type_of_bank == 1:
    initial_sum = int(input("\nInitial sum of money for each player: "))
    for i in range(0, number_of_players):
        player[i].money = initial_sum
else:
    for i in range(0, number_of_players):
        initial_sum = int(input('Bank for ' + player[i].name + ': '))
        player[i].money = initial_sum

player_turn = 0
while choice == 'y':
    for i in range(0, number_of_players):
        player[i].fold = False
    pot = 0
    print('\nInitial pot: ' + str(pot))
    current_wager = 0
    same_wager_counter = 0
    status = 0
    number_of_players_in_game = number_of_players

    while True:
        current_player_money = player[player_turn].money
        if number_of_players_in_game == 1:
            break
        if current_player_money == 0 or player[player_turn].fold:
            player_turn = (player_turn + 1) % number_of_players
            continue
        elif same_wager_counter == number_of_players_in_game:
            if status == 0:
                print('\nTime to exchange!')
                status = 1
                same_wager_counter = 0
                current_wager = 0
                dump = input('Press enter to continue ')
                continue
            else:
                print('\nShow your cards!')
                dump = input('Press enter to continue ')
                break

        print("\n" + player[player_turn].name + "'s move")
        print('Bank: ' + str(current_player_money))
        print('Current wager: ' + str(current_wager))
        move = input("Deduction (-1 to fold): ")
        if len(move) == 0:
            move = current_wager
            print('Auto deducting ' + str(move))
        else:
            move = int(move)

        if move > current_player_money:
            print('You cannot wager more than you have. Try again!')
            continue
        elif move > current_wager and move < current_wager * 2:
            print('You have raise to at least double of the ongoing bet. Try again!')
            continue
        elif move == -1:
            player[player_turn].fold = True
            number_of_players_in_game = number_of_players_in_game - 1
        elif move < current_wager:
            print('You cannot wager less than the ongoing bet. Try again!')
            continue
        else:
            player[player_turn].money = player[player_turn].money - move
            if move == current_wager:
                same_wager_counter = same_wager_counter + 1
            else:
                same_wager_counter = 1
            current_wager = move
            pot = pot + move
        player_turn = (player_turn + 1) % number_of_players
        print('Pot: ' + str(pot))
    
    print('\nPlayer codes:')
    for i in range(0, number_of_players):
        print(str(i+1) + ': ' + player[i].name)
    round_winner = int(input("\nWinner's code: "))
    player[round_winner - 1].money = player[round_winner - 1].money + pot
    
    print('\nBank:')
    for i in range(0, number_of_players):
        print(player[i].name + ': ' + str(player[i].money))
    
    choice = input('\nAnother round? (y/n): ')
    choice = choice.lower()

print('\nBye-bye!\n')