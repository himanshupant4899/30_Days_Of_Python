#1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.

name = input("Enter given name and surname name: ")
full_name = name.split(" ")
given_name = full_name[0]
surname = full_name[1]

#2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.

lst = [1, 2, 3, 4, 5]
str_lst = []
for l in lst:
    str_lst.append(str(l))
print(" | ".join(str_lst))

#3) Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, extract the text from each string, without these extra quote marks, and print each quote.

quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]

for quote in quotes:
    print(quote[1:-1]
          )  #to eliminate first and last (") from each item in the list

#4) Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input, so you’re going to have to process the string before you find its length.

word = input("Enter a word: ")
print(f"length of input is: {len(word)}")
