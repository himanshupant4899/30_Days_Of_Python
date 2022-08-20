
# Write a function that prompts the user for their name and then greets them. You should process the string by removing
# any whitespace and converting the string to title case.

# If after processing the string you're left with an empty string, the function should replace the empty string with
# "World" in the output.

name = input("Enter your name: ").strip().title() or "World"
print(f'Hello, {name}')




