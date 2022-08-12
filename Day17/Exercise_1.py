#Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers.
# Remember that we can use the sum function to add the values in an iterable.

def sum(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    print(f'The total is {sum}')

sum(2,4,10,20)