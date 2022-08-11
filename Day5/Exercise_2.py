#Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.

#If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.

hours_worked = float(input("Enter no. of hours worked for the week: "))
hourly_wage = float(input("Enter the hourly wage: "))
amount_due = 0
total = 0

if hours_worked > 40:
    print("Employee is due some additional pay.")
    amount_due = (hours_worked - 40) * (10 * hourly_wage / 100)
    print(f"Amount due for the employee: {round(amount_due,2)}")
    total = (hours_worked * hourly_wage) + amount_due
    print(f"Total amount to be paid: {round(total,2)}")
else:
    total = (hours_worked * hourly_wage)
    print(f"Total amount to be paid: {round(total,2)}")
