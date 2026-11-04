p = 17
a = 2
b = 2
G = (5, 1)

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

dA = 5
dB = 7

QA = scalar_mult(dA, G)
QB = scalar_mult(dB, G)

SA = scalar_mult(dA, QB)
SB = scalar_mult(dB, QA)

print("Alice Public Key:", QA)
print("Bob Public Key:", QB)
print("Alice Shared Secret:", SA)
print("Bob Shared Secret:", SB)
print("Match:", SA == SB)
