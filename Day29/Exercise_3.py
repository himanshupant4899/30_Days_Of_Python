# Write a decorator called printer which causes any decorated function to print their return values. If the return
# value of a given function is None, printer should do nothing.
from functools import wraps


def printer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        response = func(*args, **kwargs)

        if response is not None:
            print(response)

    return inner
