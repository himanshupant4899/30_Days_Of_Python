#1) Create an empty set and assign it to a variable.

demo_set = set()

#2) Add three items to your empty set using either several add calls, or a single call to update.

demo_set.update(["Jayden", "Alexis", "Dani"])

#3) Create a second set which includes at least one common element with the first set.
another_set = {"Valentina", "Applegate", "Alexis"}

#4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
print(demo_set.union(another_set))
print(demo_set.symmetric_difference(another_set))
print(demo_set.intersection(another_set))

#5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.
#If you want an extra challenge, also tell the user if their number was too high or too low.
numbers = range(13, 93)

while True:
    num = int(input("Enter Number: "))
    if num in numbers:
        print("Number is within specified range.")
        break
    elif num > numbers[-1]:
        print("Entered number is too high.")
    else:
        print("Entered number is too low.")
