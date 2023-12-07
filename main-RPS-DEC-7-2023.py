#####################
## Created By: Ved ##
#####################
# START #

# Import Module
import random
import time

# Assign characters
rock = "rock"
paper = "paper"
scissor = "scissor"
choice = [rock, paper, scissor]
score = 0
user_run = input("Do you want to play the game? -> ")
run = False
if user_run == "yes".lower():
    run = True
else:
    print("Have a great Day!")
    quit()
# User Input Game Character
user_character = input("Type in a the Rock, Paper, or Scissor -> ")

if user_character == "Rock".lower():
    user_character = rock
elif user_character == "Paper".lower():
    user_character = paper
elif user_character == "Scissor".lower():
    user_character = scissor
else:
    print("ERROR, UNKNOWN COMMAND ENTERED!")
    user_character = input("Type in a the Rock, Paper, or Scissor -> ")
# Computer Character
computer_choice = random.choice(choice)


# Main Game

def main_game():
    global score
    score = 0
    if user_character == paper and computer_choice == paper:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("Game is Tied!", computer_choice, "=", user_character)
        score = 0

    elif user_character == rock and computer_choice == rock:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("Game is Tied!", computer_choice, "=", user_character)
        score = 0

    elif user_character == scissor and computer_choice == scissor:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("Game is Tied!", computer_choice, "=", user_character)
        score = 0

    # User win condition
    elif user_character == rock and computer_choice == scissor:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("You win!", user_character, "beats", computer_choice)
        score = score + 1

    elif user_character == paper and computer_choice == rock:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("You win!", user_character, "covers", computer_choice)
        score = score + 1

    elif user_character == scissor and computer_choice == paper:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("You win!", user_character, "cuts", computer_choice)
        score = score + 1




    # User Lose Condition ---------------------------------------
    elif user_character == paper and computer_choice == scissor:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("You lose!", computer_choice, "cuts", user_character)
        score = score - 1


    elif computer_choice == rock and user_character == scissor:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("You Lose!", computer_choice, "beats", user_character)
        score = score - 1

    elif computer_choice == paper and user_character == rock:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("You Lose!", computer_choice, "covers", user_character)
        score = score - 1

    elif computer_choice == scissor and user_character == paper:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("You Lose!", computer_choice, "cuts", user_character)
        score = score - 1

    elif user_character == rock and computer_choice == paper:
        print("The Computer chose:", computer_choice)
        time.sleep(0.5)
        print("You Lose!", computer_choice, "covers", user_character)
        score = score - 1


# Main game loop
run = True
while run is True:
    main_game()
    interplays = input("Do you want to play again? -> ")
    if interplays == "yes".strip():
        user_character = input("Type in a the Rock, Paper, or Scissor -> ")
        if user_character == "Rock".lower():
            user_character = rock
        elif user_character == "Paper".lower():
            user_character = paper
        elif user_character == "Scissor".lower():
            user_character = scissor
        main_game()
    else:
        print("Your score ->", score)
        quit()
quit()