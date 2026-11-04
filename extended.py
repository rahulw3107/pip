def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

a = int(input("Enter a: "))
m = int(input("Enter modulus: "))
print("Modular inverse:", mod_inverse(a, m))
