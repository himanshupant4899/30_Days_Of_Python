def read_column(number):
    column_data = []
    with open("iris.csv", "r") as iris:
        for line in iris.readlines()[1:]:
            data = line.strip().split(",")
            column_data.append(data[number])
    return column_data


def view_columns():
    with open("iris.csv", "r") as iris:
        header = list(iris.readlines()[0].strip().split(","))
    return header
