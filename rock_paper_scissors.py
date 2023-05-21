import random
from colorama import Fore

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
rounds = 0
player_score = 0
computer_score = 0

while rounds <= 5:

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

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
    elif computer_move == player_move:
        print(Fore.YELLOW + "Draw!")
        continue
    else:
        print(Fore.RED + "You lose!")
        computer_score += 1
    rounds += 1
    if computer_score > player_score and rounds > 3:
        print("Computer WON the game!")
    elif player_score > computer_score and rounds > 3:
        print("You WON the GAME!")
        print("Do you want to play another round?... Type YES to continue")
        decision_to_continue_the_game = input()
        if decision_to_continue_the_game.upper() == "YES":
            rounds = 0
            continue
        else:
            print("Thank you! Have a nice day!")
            exit()
