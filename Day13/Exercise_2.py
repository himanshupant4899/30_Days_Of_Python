# Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.

def process_string(str):
    return str.strip().lower()


print(process_string("   PyThon  "))


# Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. The data should be in the following format:

#                   ("Tom Hardy", "English", 42)  # name, nationality, age

def process_tuple(info):
    dict = {"name": info[0],
            "nationality": info[1],
            "age": info[2]}
    return dict


print(process_tuple(("Tom Hardy", "English", 42)))


#  Write a function that takes in a single number and returns True or False depending on whether or not the number is prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.

def prime_checker(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


print(prime_checker(27))


