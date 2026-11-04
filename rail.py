text = input("Enter text: ")
rails = int(input("Enter number of rails: "))

rows = [""] * rails
row = 0
direction = 1

for ch in text:
    rows[row] += ch

    if row == 0:
        direction = 1
    elif row == rails - 1:
        direction = -1

    row += direction

cipher = "".join(rows)
print("Cipher:", cipher)
