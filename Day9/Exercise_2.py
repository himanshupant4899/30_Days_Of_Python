#Unpack the following tuple into 4 variables:
("John Smith", 11743, ("Computer Science", "Mathematics"))
#The data represents a student's name, their student id number, and their major and minor disciplines in that order.
name, id, (major, minor) = ("John Smith", 11743, ("Computer Science",
                                                  "Mathematics"))
print(name)
print(id)
print(major)
print(minor)

#3) Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list containing three items, and a tuples containing four items.
lst = ["himanshu", 25, "devops"]
tup = ("name", "age", "stream", "contact")
new_lst = zip(tup, lst)
print(list(new_lst))
