# Make a decorator which calls a given function twice. You can assume the functions don't return anything important,
# but they may take arguments.

from functools import wraps

n = 2


def outer_function(func):
    @wraps(func)
    def inner(*args, **kwargs):
        for i in range(n):
            func(*args, **kwargs)

    return inner
