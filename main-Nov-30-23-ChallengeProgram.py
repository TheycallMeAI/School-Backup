# Challenge program takes 3 numbers and finds out which one is bigger!

# Pseudo Code : INPUT take the two numbers from the user.
num1 = int(input("Please enter a integer number which is a number without a decimal : \n"))
num2 = float(input("Please enter a float number which is a number with a decimal : \n")).__round__(2)
num3 = float(input("Please enter a float number or integer : \n")).__round__(2)
# Pseudo Code : Function - check which on is bigger.
if num1 > num2:  # Check if num1 is bigger than num2
    if num1 > num3:  # check if num1 is bigger than num3
        print(num1, "is bigger than", num2, "and", num3)  # Print num1 is bigger than num3
    elif num1 == num3:  # Check if num1 and num3 have the same value
        print(num1, "and", num3, "have the same value.")  # Print num1 and num3 have the same value
    elif num1 < num3:  # Check if num3 is bigger than num2
        print(num3, "is bigger than", num1, "and", num2)

elif num1 == num2:
    print("Both the numbers have the same value.")
else:
    print(num2, "is bigger than all the numbers!")
