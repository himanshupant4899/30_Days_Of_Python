#If the number is divisible by 3, instead of saying the number, the player should say, "Fizz".

#If the number is divisible by 5, instead of saying the number, the player should say, "Buzz".

#If the number is divisible by 3and5, instead of saying the number, the player should say, "Fizz Buzz".

#If you make a mistake, you're usually eliminated from the game, and the game continues until there's only a single player remaining.

#############################The brief##################################

#For our version, we're only going to have a single player, the computer, and it's going to play the first 100 rounds of Fizz Buzz all by itself. In other words, we need to print out the first 100 items in the sequence, starting from 1.

for n in range(1, 101):
    if (n % 3 == 0) and (n % 5 == 0):
        print("Fizz Buzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)
