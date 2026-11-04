text = input("Enter plaintext: ").upper()
key = input("Enter key of same length: ").upper()

if len(text) != len(key):
    print("Key must have the same length as plaintext.")
else:
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i]) - 65 + ord(key[i]) - 65) % 26
            result += chr(x + 65)
        else:
            result += text[i]
    print("Cipher:", result)
