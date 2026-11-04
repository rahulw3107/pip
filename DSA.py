import hashlib

p = 23
q = 11
g = 4

x = 3
y = pow(g, x, p)

message = "HELLO"
H = int(hashlib.sha256(message.encode()).hexdigest(), 16)

k = 7
r = pow(g, k, p) % q
k_inverse = pow(k, -1, q)
s = (k_inverse * (H + x * r)) % q

signature = (r, s)

w = pow(s, -1, q)
u1 = (H * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

verified = (v == r)

print("Public Key:", y)
print("Private Key:", x)
print("Message:", message)
print("Signature:", signature)
print("Verified:", verified)
