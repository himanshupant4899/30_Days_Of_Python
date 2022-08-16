from charts import create_chart
from data_storage import read_column, view_columns

user_choice = """
Enter:
- 'c' to chart a new graph
- 'q' to quit
Your choice: """

charting_menu = """Enter the column you would like to chart: """
file_name_prompt = """Enter your desired filename: """


def handle_chart():
    column = int(input(charting_menu))
    file_name = input(file_name_prompt)
    x = read_column(-1)
    y = [float(n) for n in read_column(column)]
    create_chart(x, y, file_name.strip())


while True:
    user_selection = input(user_choice)
    if user_selection == 'q':
        break
    elif user_selection == 'c':
        print()
        for count, ele in enumerate(view_columns(), start=1):
            print(f"-{count} for {ele}")
        print()
        handle_chart()
    else:
        print("Sorry! invalid option")
