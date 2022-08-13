# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
#The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
import json

def add_book():
    books = get_all_books()
    title = input("title: ").strip().lower()
    author = input("author: ").strip().lower()
    year = input("publication year: ").strip().lower()

    books.append({
        "title": title,
        "author": author,
        "year": year,
        "read": "Not read"
    })

    with open("books.json", "w") as books_list:
        json.dump(books,books_list)
    print("Book added to library..")


# Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.


def get_all_books():
    books = []
    with open("books.json", "r") as books_list:
        return json.load(books_list)


def display_books(books):
    print()
    for book in books:
        print(' {title} ({year}) written by {author} - {read}'.format(**book))
    print()


#Users should be able to search for a specific book by providing a book title.


def search_book():
    books = get_all_books()
    matching_books = []
    search_item = input("Enter a book title: ").strip().lower()

    for book in books:
        if search_item in book["title"].lower():
            matching_books.append(book)

    return matching_books


# function to delete a book


def delete_book():
    books = get_all_books()  #return list of dictionary
    matching_books = search_book()  #returns a dictionary

    if matching_books:
        books.remove(matching_books[0])

        with open("books.json", "w") as books_list:
            json.dump(books, books_list)
    else:
        print("Sorry, book doesn't exists.")


# function to mark a book as read


def mark_as_read():
    books = get_all_books()
    matching_books = search_book()

    if matching_books:
        index = books.index(matching_books[0])
        books[index]["read"] = "Read"

        with open("books.csv", "w") as books_list:
            for book in books:
                books_list.write(
                    f'{book["title"]},{book["author"]},{book["year"]},{book["read"]}\n'
                )
    else:
        print("Sorry, book doesn't exists")


# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program.

while True:
    print('''
Enter one among the following options to proceed:
-"A" to add a book.
-"D" to display the books stored.
-"Q" to quit the application.
-"S" to search for a book by name.
-"1" to delete a book.
-"2" to mark a book as read.

    ''')
    action = input("Enter your choice: ").lower()

    if action == 'a':
        add_book()
    elif action == 'd':
        data = get_all_books()
        if data:
            display_books(data)
        else:
            print("Reading list is empty")

    elif action == 's':
        matched_books = search_book()
        if matched_books:
            display_books(matched_books)
        else:
            print("No matching books found")
    elif action == '1':
        delete_book()
    elif action == '2':
        mark_as_read()
    elif action == 'q':
        break
    else:
        print("Invalid Input! Please try again")
