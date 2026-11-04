import math

p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)
e = 7
d = pow(e, -1, phi)

public_key = (e, n)
private_key = (d, n)

message = 9
cipher = pow(message, e, n)
decrypted = pow(cipher, d, n)

print("Public Key:", public_key)
print("Private Key:", private_key)
print("Message:", message)
print("Ciphertext:", cipher)
print("Decrypted:", decrypted)
