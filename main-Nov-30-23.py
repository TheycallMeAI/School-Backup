# This program takes 2 numbers and finds out which on is bigger!
# Challenge program takes 3 numbers and finds out which one is bigger!

# Pseudo Code : INPUT take the two numbers from the user.
num1 = int(input("Please enter a integer number or a number without a decimal : \n"))
num2 = float(input("Please enter a float number or a number with a decimal : \n")).__round__(2)
# Pseudo Code : Function - check which on is bigger.
if num1 > num2:
    print(num1, "is bigger than", num2, "!")
elif num1 == num2:
    print("Both the numbers have the same value.")
else:
    print(num2, "is bigger than", num1, "!")