text = input("Enter plaintext: ").upper()
key = input("Enter keyword: ").upper()

plain = "".join(ch for ch in text if ch.isalpha())
stream = key + plain
stream = stream[:len(plain)]

cipher = ""
for i in range(len(plain)):
    x = (ord(plain[i]) - 65 + ord(stream[i]) - 65) % 26
    cipher += chr(x + 65)

print("Cipher:", cipher)
