import random
from colorama import Fore

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
rounds = 0
player_score = 0
computer_score = 0

while rounds <= 5:
    if rounds == 4 and computer_score != player_score:
        if computer_score > player_score:
            print(Fore.RED + "SORRY! You lost the game!")
            print("Do you want to play another round?... Type YES to continue or ANY other key to EXIT!")
            print()
        elif player_score > computer_score:
            print(Fore.GREEN + "You WON the GAME!")
            print(Fore.CYAN + "Do you want to play another round?... Type 'yes' to continue or ANY other key to EXIT!")
            print()
    elif rounds == 3 and computer_score == 0 or rounds == 3 and player_score == 0:
        if computer_score > player_score:
            print(Fore.RED + "SORRY! You lost the game!")
            print("Do you want to play another round?... Type YES to continue or ANY other key to EXIT!")
            print()
        elif player_score > computer_score:
            print(Fore.GREEN + "You WON the GAME!")
            print(Fore.CYAN + "Do you want to play another round?... Type 'yes' to continue or ANY other key to EXIT!")
            print()
        decision_to_continue_the_game = input()
        if decision_to_continue_the_game.upper() == "YES":
            player_score = 0
            computer_score = 0
            rounds = 0
            print(Fore.CYAN + "GREAT! Let's go for another round!")
            print()
            continue
        else:
            print(Fore.BLUE + "Thank you! Have a nice day! :)")
            exit()

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print(Fore.RED + "Invalid Choice! Please input 'r' for rock, 'p' for paper or 's' for scissors")
        print()
        continue

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_move == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(Fore.GREEN + "You win!")
        player_score += 1
        rounds += 1
        continue
    elif computer_move == player_move:
        print(Fore.YELLOW + "Draw!")
        print()
        continue
    else:
        print(Fore.RED + "You lose!")
        print()
        computer_score += 1
        rounds += 1
        continue
