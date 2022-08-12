#Using * unpacking and range, print the numbers 1 to 20, separated by commas.
#You will have to provide an argument for print function's sep parameter for this exercise.

print(*range(1, 21), sep=',')

#Modify your code so that each number prints on a different line.
#You can only use a single print call.

print(*range(1,21), sep= '\n')