#create a program that prints out every prime number between 1 and 100.

for dividend in range(1, 100):

    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            #not prime
            break
    else:
        #prime
        print(dividend)
