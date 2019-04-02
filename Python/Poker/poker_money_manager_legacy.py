# Legacy version does not implement using objects

from os import system, name 

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

clear()
print('\n--------Welcome to Poker money manager--------\n\nThanks to virtual money, you can enjoy this game without actually going broke!\n\n---------------Happy gambling!!---------------\n')
choice = 'y'
number_of_players = int(input("\nEnter the number of players: "))
player_name = []
print()

for i in range(0, number_of_players):
    player_name.append(input("Enter name of player " + str(i+1) + ": "))

type_of_bank = int(input('\n1. Same initial bank for all players.\n2. Custom bank for each.\nChoice: '))
if type_of_bank == 1:
    initial_sum = int(input("\nInitial sum of money for each player: "))
    player_money = [initial_sum for i in range(0, number_of_players)]
else:
    player_money = []
    for i in range(0, number_of_players):
        bank = int(input('Bank for ' + player_name[i] + ': '))
        player_money.append(bank)

player_turn = 0
while choice == 'y':
    fold = [False for i in range(0, number_of_players)]
    pot = 0
    print('\nInitial pot: ' + str(pot))
    current_wager = 0
    same_wager_counter = 0
    status = 0
    number_of_players_in_game = number_of_players

    while True:
        current_player_money = player_money[player_turn]
        if current_player_money == 0 or fold[player_turn]:
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

        print("\n" + player_name[player_turn] + "'s move")
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
            fold[player_turn] = True
            number_of_players_in_game = number_of_players_in_game - 1
        elif move < current_wager:
            print('You cannot wager less than the ongoing bet. Try again!')
            continue
        else:
            player_money[player_turn] = player_money[player_turn] - move
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
        print(str(i+1) + ': ' + player_name[i])
    round_winner = int(input("\nWinner's code: "))
    player_money[round_winner - 1] = player_money[round_winner - 1] + pot
    
    print('\nBank:')
    for i in range(0, number_of_players):
        print(player_name[i] + ': ' + str(player_money[i]))
    
    choice = input('\nAnother round? (y/n): ')
    choice = choice.lower()

print('\nBye-bye!\n')