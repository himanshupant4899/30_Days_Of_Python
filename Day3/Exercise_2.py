#Ask the user for their name, and then greet the user, using their name as part of the greeting. The name should be in title case, and shouldn't be surrounded by any excess white space.

name_1 = input("Enter name: ")
name_2 = "Brian "

print(name_1.strip().title())
print(name_2.strip().title())