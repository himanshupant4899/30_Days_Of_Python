# Use the sample function in the random module to create three lists, each containing fifteen numbers from 1 to 100
# (inclusive). Sort each of these lists into descending order (largest first), and then truncate each list so that
# only 5 items remain in each.
import random

lst = range(1, 101)

numbers = [sorted(random.sample(lst, 15)) for _ in range(3)]

for number in numbers:
    number.reverse()
    del number[5:]
    print(number)
