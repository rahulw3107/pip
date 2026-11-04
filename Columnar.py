text = input("Enter text: ").replace(" ", "")
key = input("Enter key: ")

cols = len(key)
while len(text) % cols:
    text += "X"

matrix = [text[i:i + cols] for i in range(0, len(text), cols)]
order = sorted(range(cols), key=lambda i: (key[i], i))

cipher = ""
for col in order:
    for row in matrix:
        cipher += row[col]

print("Cipher:", cipher)
