#1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.

answer = 17

while True:
    num = int(input("Enter a number: "))
    if num > answer:
        print("Your guess was too high")
    elif num < answer:
        print("Your guess was too low")
    else:
        print("Bingo! You guessed it right..")
        break