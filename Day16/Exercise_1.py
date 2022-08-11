#Use the sort method to put the following list in alphabetical order with regards to the students' names:
students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

#sorted_data = sorted(students, key=lambda student: student.get("name"))
#print(sorted_data)

students.sort(key=lambda student: student.get("name"))
print(students)

#Convert the following function to a lambda expression and assign it to a variable called exp.
#               def exponentiate(base, exponent):
#                  return base ** exponent

exp = lambda base, exponent : base ** exponent

#Print the function you created using a lambda expression
print(exp)

#print(exp(4,4))