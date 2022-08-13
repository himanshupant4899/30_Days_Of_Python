# Use the randint function to create a guessing game we made in day 8.  The program should generate a random
# number, and you should tell the user whether their guess was too high, or too low, until they get the right number.

import random as rd

num = rd.randint(32, 78)

while True:
    guess = int(input("Enter your guess: "))
    if guess > num:
        print("Guessed too high")
    elif guess < num:
        print("Guessed too low")
    elif guess == num:
        print("Congratulations! You guessed it right")
        break
    else:
        continue
