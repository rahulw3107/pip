def factors(n):
    result = set()
    p = 2
    while p * p <= n:
        if n % p == 0:
            result.add(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result.add(n)
    return result

def primitive_root(p):
    phi = p - 1
    for g in range(2, p):
        ok = True
        for factor in factors(phi):
            if pow(g, phi // factor, p) == 1:
                ok = False
                break
        if ok:
            return g
    return None

p = int(input("Enter prime p: "))
print("Primitive root:", primitive_root(p))
