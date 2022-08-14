# You have a file named data.txt with this content: "There is some data here!"
# Open it for reading using Python, but make sure to use a try block to catch an exception that arises if the file
# doesn't exist. Once you've verified your solution works with an actual file, delete the file and see if your
# try block is able to handle it.
# When files don't exist when you try to open them, the exception raised is FileNotFoundError.
try:
    with open("data.txt", "r") as content:
        print(content.read())
except FileNotFoundError:
    print("File doesn't exists")
