num = int(input("Please enter the number 8."))  # Ask the user for an input of number 8
while num != 8:  # A while loop to check if the user has inputted the number 8
    num = int(input("That is not an 8. Please enter the number 8!"))
print("Thank you.")

answer = input("Please enter the veggie avocado: ").lower()
while answer != "avocado":
    answer = input("That's incorrect! Please enter the veggie avocado only! :").lower()
print("Thank you for enter the veggie avocado!")