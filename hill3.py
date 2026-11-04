def encrypt(text, key):
    text = "".join(ch for ch in text.upper() if ch.isalpha())
    while len(text) % 3:
        text += "X"

    result = ""

    for i in range(0, len(text), 3):
        vector = [ord(text[i + j]) - 65 for j in range(3)]

        for row in range(3):
            value = sum(key[row][col] * vector[col] for col in range(3)) % 26
            result += chr(value + 65)

    return result

key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
text = input("Enter plaintext: ")
print("Cipher:", encrypt(text, key))
