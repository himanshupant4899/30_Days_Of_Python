#Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.


def check_palindrome(word):
    lst_initial_word = list(word.lower().replace(" ", ""))
    lst_reverse_word = list(word.lower().replace(" ", ""))
    lst_reverse_word.reverse()

    if lst_initial_word == lst_reverse_word:
        print("Palindrome")
    else:
        print("Not Palindrome")


initial_word = "was it a car or a cat I saw"
check_palindrome(initial_word)
