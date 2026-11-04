import random
import math

def euler_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def euler_test(n, k=5):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    phi = euler_phi(n)
    for _ in range(k):
        a = random.randint(2, n - 2)
        if math.gcd(a, n) != 1:
            return False
        if pow(a, phi, n) != 1:
            return False
    return True

n = int(input("Enter number: "))
print("Probably Prime" if euler_test(n) else "Composite")
