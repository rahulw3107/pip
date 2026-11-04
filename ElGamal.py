p = 23
g = 5
x = 6
y = pow(g, x, p)

message = 10
k = 3

c1 = pow(g, k, p)
c2 = (message * pow(y, k, p)) % p

s = pow(c1, x, p)
s_inverse = pow(s, -1, p)
decrypted = (c2 * s_inverse) % p

print("Public Key:", (p, g, y))
print("Private Key:", x)
print("Message:", message)
print("Ciphertext:", (c1, c2))
print("Decrypted:", decrypted)
