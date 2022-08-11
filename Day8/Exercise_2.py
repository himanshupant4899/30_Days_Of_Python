#2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".

word = "Python"

for i in range(0, len(word)):
    if word[i] != 'o':
        print(word[i])
    else:
        continue
