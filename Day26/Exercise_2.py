# Use a defaultdict to store a count for each character that appears in a given string. Print the most common character
# in this dictionary.

from collections import defaultdict

s = "Himanshu"
letter_count = defaultdict(int)

for character in s:
    letter_count[character] += 1

max_appearance = max(letter_count, key=lambda key: letter_count[key])

print(max_appearance)
