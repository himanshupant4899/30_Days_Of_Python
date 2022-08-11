# Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show.

# The print_show_info function should print the information stored in the dictionary, in a nice way.


def print_show_info(show):
    print(
        show.get("title") + " (" + str(show.get("initial_release")) + ") - " +
        str(show.get("seasons")) + " seasons")


tv_show = {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008}

print_show_info(tv_show)
