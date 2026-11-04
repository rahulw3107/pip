import hashlib

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

message = "HELLO"
H = int(hashlib.sha256(message.encode()).hexdigest(), 16)

k = 3
R = scalar_mult(k, G)
r = R[0] % n
k_inverse = pow(k, -1, n)
s = (k_inverse * (H + d * r)) % n

signature = (r, s)

w = pow(s, -1, n)
u1 = (H * w) % n
u2 = (r * w) % n

P1 = scalar_mult(u1, G)
P2 = scalar_mult(u2, Q)
X = point_add(P1, P2)

verified = (X is not None and X[0] % n == r)

print("Public Key:", Q)
print("Private Key:", d)
print("Message:", message)
print("Signature:", signature)
print("Verified:", verified)
