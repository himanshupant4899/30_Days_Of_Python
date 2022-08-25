# Imagine you have a list called books, which several functions in your application interact with. Write a decorator
# which causes your functions to run only if books is not empty.
from functools import wraps

books = []


def check_empty(func):
    @wraps
    def inner(*args, **kwargs):
        if books:
            return func(*args, **kwargs)

    return inner
