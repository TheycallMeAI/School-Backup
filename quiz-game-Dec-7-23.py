############
# By:Ved K #
############
import time
import pyfiglet

print("Welcome to the Quiz-masterz game show! ")
user_playing = input("Do you want to play? -> : ")
if user_playing == "no".lower().strip():
    quit()
user_name = input("What is your name? -> ")
score = 0

print("Hi,", user_name, "In this quiz game you have to answer question "
      "about computers and cars, to get 10 points you have to get \n"
      "the correct answers and if you "
      "answer the question wrong, we will take -10 points from your score! \n"
      "So be sure to answer the question right! And Good LUCK!")

def time_question():
    print("1.")
    time.sleep(0.6)
    print("2..")
    time.sleep(0.6)
    print("3...")

# Question 1: What is a CPU?
answer1 = input("Question 1 -> What is CPU : ")
if answer1 == "central processing unit".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
else:
    time_question()
    print("INCORRECT! CPU is Central Processing Unit.")
    print("Minus 10 points from", score)
    score = score - 10
    print("Your score -> ", score)

# Question 2: What is a GPU?
answer2 = input("Question 2 -> What is GPU : ")
if answer2 == "graphics processing unit".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
else:
    time_question()
    print("INCORRECT! GPU is Graphics Processing Unit or Graphics Processing Unit")
    print("Minus 10 points from", score)
    score = score - 10
    print("Your score -> ", score)

# Question 3: What is a PSU?
answer3 = input("Question 3 -> What is PSU : ")
if answer3 == "power supply unit".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
else:
    time_question()
    print("INCORRECT! PSU is Power Supply Unit.")
    print("Minus 10 points from", score)
    score = score - 10
    print("Your score -> ", score)

# Question 4: What is a RAM?
answer4 = input("Question 4 -> What is RAM : ")
if answer4 == "random access memory".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
else:
    time_question()
    print("INCORRECT! RAM is Random Access Memory.")
    print("Minus 10 points from", score)
    score = score - 10
    print("Your score -> ", score)

# Question 5: Name a type of CPU?
answer5 = input("Question 5 -> Name a type of CPU : ")
if answer5 == "amd".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
elif answer5 == "arm".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
elif answer5 == "intel".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
else:
    time_question()
    print("INCORRECT! The right answers would be : arm, intel, amd")
    print("Minus 10 points from", score)
    score = score - 10
    print("Your score -> ", score)

## Car QUESTIONS

# Question 6: Who invented the Ford car brand?
answer6 = input("Question 6 -> Who invented the Ford Car Brand? : ")
if answer6 == "henry ford".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
else:
    time_question()
    print("INCORRECT! Henry Ford created and invented the Ford Car Brand.")
    print("Minus 10 points from", score)
    score = score - 10
    print("Your score -> ", score)

# Question 7: What car did Elon Musk Create????
answer7 = input("Question 7 -> What car did Elon Musk invent? : ")
if answer7 == "tesla".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
else:
    time_question()
    print("INCORRECT! Elon Musk created the Tesla.")
    print("Minus 10 points from", score)
    score = score - 10
    print("Your score -> ", score)

# Question 8: What is MPG?
answer8 = input("Question 8 -> What is MPG : ")
if answer8 == "miles per gallon".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
else:
    time_question()
    print("INCORRECT! MPG is Miles Per Gallon.")
    print("Minus 10 points from", score)
    score = score - 10
    print("Your score -> ", score)

# Question 9: What is the fastest car in the world?
answer9 = input("Question 9 -> What is fastest car in the world? : ")
if answer9 == "Koenigsegg Jesko Absolut".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
else:
    time_question()
    print("INCORRECT! The fastest car is the Koenigsegg Jesko Absolut which goes 330 MPH.")
    print("Minus 10 points from", score)
    score = score - 10
    print("Your score -> ", score)

# Question 10: What is the most popular coding language?
answer10 = input("Question 10 -> What is the most popular coding language? : ")
if answer10 == "javascript".lower().strip():
    print('You got the question...')
    time_question()
    print("RIGHT! You get +10 points! ")
    score = score + 10
    print("Your score -> ", score)
else:
    time_question()
    print("INCORRECT! The most popular coding language is javascript.")
    print("Minus 10 points from", score)
    score = score - 10
    print("Your score -> ", score)

percentage = float((score / 10) * 10)
print("You got a ", float(percentage), "%.")
print("Thanks for playing,", user_name, "! 8)")

text = pyfiglet.figlet_format(text='VibinVk The Coder!', font='isometric1')
print(text)