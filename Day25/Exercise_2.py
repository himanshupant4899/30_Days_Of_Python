# Write a function to determine whether or not a string contains exclusively ASCII letters (a to z in either upper or
# lowercase).
import string


def is_ascii_string(text):
    for letter in text:
        if letter not in string.ascii_letters:
            return False
    else:
        return True


name = "DummyName"
print(is_ascii_string(name))
