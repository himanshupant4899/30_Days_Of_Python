#  Use filter to remove all negative numbers from the following range: range(-5, 11). Print the remaining numbers to
#  the console.
output = filter(lambda number: number > 0, range(-5, 11))
print(*output, sep=",")