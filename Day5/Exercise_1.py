# Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.

x = 5
y = 5

print(f'id of x: {id(x)}')
print(f'id of y: {id(y)}')

print(id(x) == id(y))
print(id(x) is id(y))
print(x is y)

# Try to use the is operator or the id function to investigate the difference between this:

#                     numbers = [1, 2, 3, 4]
#                     new_numbers = numbers + [5]
#And this:

#                     numbers = [1, 2, 3, 4]
#                     numbers.append(5)
#Are new_numbers and numbers the same thing? What about numbers before and after we append 5?

print("********************* Statement-2 *****************")
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(id(numbers) is id(new_numbers))

numbers.append(5)
print(id(numbers) is id(new_numbers))
print(numbers == new_numbers)

# Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.

num = int(input("Enter Number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
