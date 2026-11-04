text = input("Enter text: ")
key = int(input("Enter key: "))
result = ""

for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
    elif ch.islower():
        result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    else:
        result += ch

print("Cipher:", result)
