# Pseudo Code: Get a random number and then store in variable = number
# Pseudo Code: Input a guess from the user
# Pseudo Code: User guess right finish
# Pseudo Code: If wrong ask in a while loop.
# Pseudo Code: Print a congratulation message when they guess the number

import random
user_guesses = 0
number = random.randint(1, 100)
answer = int(input("Guess the number in 8 try's ? : "))

while answer != number and user_guesses <= 7:

    if answer < number:
        user_guesses = user_guesses + 1
        answer = int(input("Guess higher! : "))

    elif answer > number:
        user_guesses = user_guesses + 1
        answer = int(input("Guess lower! : "))

if answer == number:
    print("You got the right answer!", number, "=", answer)
    print("It took you", user_guesses, "times to figure it out!")
else:
    print("Sorry! The all the guesses has been used!")