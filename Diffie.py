p = 23
g = 5

a = 6
b = 15

A = pow(g, a, p)
B = pow(g, b, p)

KA = pow(B, a, p)
KB = pow(A, b, p)

print("Alice Private Key:", a)
print("Bob Private Key:", b)
print("Alice Public Key:", A)
print("Bob Public Key:", B)
print("Alice Shared Secret:", KA)
print("Bob Shared Secret:", KB)
print("Match:", KA == KB)
