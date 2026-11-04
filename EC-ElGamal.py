p = 17
a = 2
b = 2
G = (5, 1)
n = 19

def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        numerator = (3 * x1**2 + a) % p
        denominator = (2 * y1) % p
    else:
        numerator = (y2 - y1) % p
        denominator = (x2 - x1) % p

    m = (numerator * pow(denominator, -1, p)) % p
    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_mult(k, P):
    result = None
    while k > 0:
        if k % 2:
            result = point_add(result, P)
        P = point_add(P, P)
        k //= 2
    return result

d = 7
Q = scalar_mult(d, G)

message = 10
k = 3

C1 = scalar_mult(k, G)
shared = scalar_mult(k, Q)

C2 = (message * shared[0]) % p

shared2 = scalar_mult(d, C1)
shared_inverse = pow(shared2[0], -1, p)
decrypted = (C2 * shared_inverse) % p

print("Public Key:", Q)
print("Private Key:", d)
print("Message:", message)
print("Ciphertext:", (C1, C2))
print("Decrypted:", decrypted)
