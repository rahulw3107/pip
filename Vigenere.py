text = input("Enter text: ").upper()
key = input("Enter key: ").upper()
result = ""
j = 0

for ch in text:
    if ch.isalpha():
        x = (ord(ch) - ord('A') + ord(key[j % len(key)]) - ord('A')) % 26
        result += chr(x + ord('A'))
        j += 1
    else:
        result += ch

print("Cipher:", result)
