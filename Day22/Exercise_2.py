# Imagine you have 3 employees and it's been agreed that the employees will take it in turns to lock up the shop at
# night. This means that for employees A, B, and C, employee A will close the shop on day 1, then B will close the shop
# on day 2, C will close the shop on day 3, and then we start the cycle again with employee A.

# Write a program to create a schedule that lists which of your employees will lock up the shop on a given day over a
# 30 day period. You should list the day number, the employee name, and the day of the week. You can choose any employee
# to lock the shop on day 1, and you can also choose which day of the week day 1 corresponds to.

from itertools import cycle

employees = cycle(['A', 'B', 'C'])
days = cycle(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

for day_number in range(1,31):
    print(f"DAY {day_number}-{next(days)} : {next(employees)}")
