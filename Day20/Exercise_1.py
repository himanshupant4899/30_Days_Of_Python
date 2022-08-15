# Use map to call the strip method on each string in the following list:
import operator
from operator import methodcaller

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",
    "    Couldn't put Humpty together again."
]

# Print the lines of the nursery rhyme on different lines in the console.
# Remember that you can use the operator module and the methodcaller function instead of a lambda expression if
# you want to.


# output = map(lambda line: line.strip(), humpty_dumpty )

output = map(methodcaller("strip"), humpty_dumpty)
print(*output, sep="\n")
