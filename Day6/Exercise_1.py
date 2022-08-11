# 1) Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: their name, the number of hours worked last week, and their hourly rate. Print how much each employee is due to be paid at the end of the week in a nice, readable format.

#                   employees = [
#                       ("Rolf Smith", 35, 8.75),
#                       ("Anne Pun", 30, 12.50),
#                       ("Charlie Lee", 50, 15.50),
#                       ("Bob Smith", 20, 7.00)
#                        ]

employees = [("Rolf Smith", 35, 8.75), ("Anne Pun", 30, 12.50),
             ("Charlie Lee", 50, 15.50), ("Bob Smith", 20, 7.00)]

total_pay = 0
n = len(employees)

for employee in employees:
    due = employee[1] * employee[2]
    print(f'Due Amount for {employee[0]} is ${due}')
    total_pay += employee[2]

# 2) For the employees above, print out those who are earning an hourly wage above average.

avg_pay = total_pay / n

for employee in employees:
    if employee[2] > avg_pay:
        print(f'{employee[0]} earns above average')
