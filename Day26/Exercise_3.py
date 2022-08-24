
# Use the mul function in the operator module to create a partial called double that always provides 2 as the first
# argument.
from functools import partial
from operator import mul

double = partial(mul, 2)

# Create a read function using a partial that opens a file in read ("r") mode.


read = partial(open, mode="r")
