#Create a short program that prompts the user for a list of grades separated by commas. Split the string into
# individual grades and use a list comprehension to convert each string to an integer. You should use a try
# statement to inform the user when the values they entered cannot be converted.
grades = input("Enter grades separated by comma: ").split(',')

try:
    grades = [int(grade) for grade in grades]
except ValueError:
    print("Values entered cannot be converted to string")