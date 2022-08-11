# Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for each iteration, passing in each dictionary. You should end up with each series printed in the appropriate format.


def print_show_info(series):
    for item in series:
        print(
            f"{item['title']} ({item['initial_release']}) - {item['seasons']} season"
        )


series = [
    {
        "title": "Breaking Bad",
        "seasons": 5,
        "initial_release": 2008
    },
    {
        "title": "Fargo",
        "seasons": 4,
        "initial_release": 2014
    },
    {
        "title": "Firefly",
        "seasons": 1,
        "initial_release": 2002
    },
    {
        "title": "Rick and Morty",
        "seasons": 4,
        "initial_release": 2013
    },
    {
        "title": "True Detective",
        "seasons": 3,
        "initial_release": 2014
    },
    {
        "title": "Westworld",
        "seasons": 3,
        "initial_release": 2016
    },
]

print_show_info(series)
