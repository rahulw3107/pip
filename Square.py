def square_multiply(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))
m = int(input("Enter modulus: "))
print("Result:", square_multiply(a, b, m))
