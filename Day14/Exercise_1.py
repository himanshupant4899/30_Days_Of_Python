#Rewrite the following piece of code using a context manager:
#                          f = open("hello_world.txt", "w")
#                          f.write("Hello, World!")
#                          f.close()

with open("hello_world.txt", "w") as f:
    f.write("Hello, World!")

#Use append mode to write "How are you?" on the second line of the hello_world.txt file above.

with open("hello_world.txt", "a") as f:
    f.write("\nHow are you?")

#Take the list of dictionaries we created from the Iris flower data set and write it to a new file in CSV format.

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

irises = []

for row in iris_data[1:]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip(
    ).split(",")

    iris_dict = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    }

    irises.append(iris_dict)

with open("new_iris.csv", "w") as f:
    for item in irises:
        f.write(
            f'\n{item["sepal_length"]}, {item["sepal_width"]}, {item["petal_length"]}, {item["petal_width"]}, {item["species"]}'
        )
