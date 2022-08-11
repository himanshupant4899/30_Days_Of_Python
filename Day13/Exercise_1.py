#Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.


def exponent(base, power):
    return base**power


base = input("Enter base: ")
power = input("Enter power: ")

print(exponent(int(base), int(power)))
