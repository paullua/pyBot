#############################################################
# This is PyBot! A simple chat bot programmed in Python.
#
# Author: Paul Land
#############################################################

# For time.sleep()
import time

# For random number game
from random import randint

# This function displays PyBot's messages!
# It also takes the seconds to pause between messages.
def pybot(message, seconds):
    print("PyBot: " + message)
    time.sleep(seconds)

# This function gets and returns input from the user/student
def student():
    return input("User:  ")

print("\n\tStarting chat")
print("----------------------------------------------------------------------")
time.sleep(5)

# PyBot's standard greeting
pybot("Hello! I'm PyBot!", 2)
pybot("What's your name?", 0)

# Get the user's name
student_name = student()

# Puts name in title case
student_name = student_name.title()

# PyBot greets the student by name!
pybot("Hi " + student_name + ", it's good to meet you!", 2)


pybot("So, " + student_name + ", are you excited to learn about coding?", 0)

# counter to track which response to use in the loop
count = 0

excited = False

# Keep asking if the student is excited to learn
while not excited:
    is_excited = student()
    if is_excited == "YES!":
        excited = True
        pybot("Alright! That's the enthusiam we're looking for!", 3)
    elif (is_excited.lower() == "no" or is_excited.lower() == "no."
          or is_excited.lower() == "no!"):
        pybot("Whaaaaat? You aren't excited?", 2)
        pybot("Coding is exciting! It's a super power!", 2)
        pybot("Afterall, I was created with coding.", 2)
        pybot("So, for me, can you be excited to learn about coding?", 0)
    elif count == 0:
        pybot("Hmmm...it doesn't look like you're excited enough...", 2)
        pybot("Show some more EXCITEMENT!", 2)
        pybot("Are you really excited to learn about coding?", 0)
        count = count + 1
    elif count < 2:
        pybot ("Still not enough enthusiam!", 2)
        pybot("I need you to type it LOUDER!", 2)
        pybot("So, " + student_name +
              ", are you EXCITED to learn about coding?", 0)
        count = count + 1
    else:
        pybot("Okay, I'll give you a hint...the answer I'm looking for " +
              "is \"YES!\"", 2)
        pybot("So, try answering again.", 2)
        pybot("Are you excited to learn about coding?", 0)

# This section is our number guessing game.
pybot("Now that we know you are excited to learn about coding, " +
      "how about we play a game?", 5)
pybot("I'll think of a number between 1 and 100, and you try to guess it!", 5)
pybot("Okay...I'm thinking...", 4)
pybot("I'm thinking...", 2)
pybot("Alright, I've got it! What's your first guess?", 0)

# PyBot's guess
pybot_number = randint(1, 100)

correct_guess = False

# Keep guessing until the correct number is found!
while not correct_guess:
    guess = student()
    guess = int(guess)
    if guess == pybot_number:
        pybot("Hey! You got it!", 2)
        pybot("I'm very impressed.", 2)
        pybot("You're pretty smart!", 2)
        correct_guess = True
    elif guess < pybot_number:
        pybot("That number is too low", .5)
        pybot("Guess again!", 0)
    elif guess > pybot_number:
        pybot("That number is too high", .5)
        pybot("Guess again!", 0)

# PyBot's departing words
pybot("Well, it's been fun chatting with you, " + student_name, 2)
pybot("I hope to see you become a great programmer one day!", 2)
pybot("Goodbye for now!", 1)
print("----------------------------------------------------------------------")
print("\tYour chat has ended\n")
