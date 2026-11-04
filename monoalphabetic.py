import random
import string

alphabet = string.ascii_uppercase
key = list(alphabet)
random.shuffle(key)
key = "".join(key)

text = input("Enter text: ").upper()
cipher = ""

for ch in text:
    if ch in alphabet:
        cipher += key[alphabet.index(ch)]
    else:
        cipher += ch

print("Substitution key:", key)
print("Cipher:", cipher)
