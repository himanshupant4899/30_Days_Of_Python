# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.

#The program should store information about all of these books in a Python list.
library = []


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    data = (title, author, year)
    library.append(data)
    print("Book added to library..")


# Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.


def display_book():
    for title, author, year in library:
        print(f"{title} ({year}) written by {author}.")


# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program.
while True:
    print('''
Enter one among the following options to proceed:
-"A" to add a book.
-"D" to display the books stored.
-"Q" to quit the application.
    ''')
    action = input("Enter your choice: ").lower()

    if action == 'a':
        add_book()
    elif action == 'd':
        display_book()
    elif action == 'q':
        break
    else:
        print("Invalid Input! Please try again")
