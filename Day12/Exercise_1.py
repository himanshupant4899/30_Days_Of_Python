#1) Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.

# When orders matters for an operation, the first argument should be treated as the left operand, and the second argument should be treated as the right operand. For example, if the user passes in 6 and 2 to subtract, the result should be 4, not -4.

# You should also make sure that the user can’t pass in 0 as the second argument for divide. If the user provides 0, you should print a warning instead of calculating their division.


def add(x, y):
    print(x + y)


def subtract(x, y):
    print(x - y)


def multiply(x, y):
    print(x * y)


def divide(x, y):
    if y == 0:
        print("Warning: Invalid Input")
    else:
        print(x / y)


add(9, 6)
multiply(17, 5)
subtract(12, 6)
divide(28, 7)
