card_number = int(input("Enter card number: ").strip())
lst_card_number = list(map(int, str(card_number)))

#Luhn formula implementation

reverse = lst_card_number[:-1]
#outputs the first (n-1) elements of the list/removes the last digit i.e. operations digit

reverse.reverse()  #reverse the list

operation = []

for n in range(0, len(reverse)):
    if n % 2 == 0:
        result = reverse[n] * 2  #double the element at even place
        if result > 9:
            result -= 9  #subtract 9 if the doubled value is greater than 9
    else:
        result = reverse[n]

    operation.append(result)  #append the resultant digit to a new list

operation.append(
    lst_card_number[-1])  #add the operations digit we removed earlier
print(operation)

sum = 0
for element in operation:
    sum += element  #sum the elements of the list

if sum % 10 == 0:
    print("Card is valid.")
else:
    print("Card invalid")
