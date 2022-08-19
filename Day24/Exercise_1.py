# Ask the user for an integer between 1 and 10 (inclusive). If the number they give is outside of the specified range,
# raise a ValueError and inform them that their choice was invalid.

num = int(input("Enter a number in range 1 to 10: "))

if num not in range(1, 11):
    raise ValueError("Invalid input")


# Below you'll find a divide function. Write exception handling so that we catch ZeroDivisionError exceptions,
# TypeError exceptions, and other kinds of ArithmeticError.

def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as ze:
        print(ze)
    except TypeError as te:
        print(te)
    except ArithmeticError as ae:
        print(ae)


divide(5,7)

