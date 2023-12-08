# Password Generator Created by VibinV
# Pseudo Code : Assign the letter of alphabet to the variable char
# Ask the user what is the length of the password.
# Choose a random letter
# Add it to the variable password
# Print the password
import pyfiglet
import random

text = pyfiglet.figlet_format(text='VibinVk The Coder!', font='isometric1')
print(text)

# Assign the ABC's
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*-=_+(/){}|:?,.;[]"
length = int(input("Type the length of your password (integer only!!!) : "))
password = ""
# Make a Choice
for i in range(length):
    password = password + random.choice(char)

print(password)
