#  Write a generator that generates prime numbers in a specified range.

def check_prime():
    for number in range(1, 101):
        for n in range(2, number):
            if number % n == 0:
                break
        else:
            yield number


primes = check_prime()
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
