def _validate_rails(rails):
    if rails < 1:
        raise ValueError("The number of rails must be at least one.")


def _rail_sequence(length, rails):
    row = 0
    direction = 1
    sequence = []
    for _ in range(length):
        sequence.append(row)
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    return sequence


def encrypt(text, rails):
    _validate_rails(rails)
    if rails == 1:
        return text
    rows = [""] * rails
    for char, row in zip(text, _rail_sequence(len(text), rails)):
        rows[row] += char
    return "".join(rows)


def decrypt(ciphertext, rails):
    _validate_rails(rails)
    if rails == 1:
        return ciphertext

    sequence = _rail_sequence(len(ciphertext), rails)
    row_lengths = [sequence.count(row) for row in range(rails)]
    rows = []
    offset = 0
    for length in row_lengths:
        rows.append(ciphertext[offset:offset + length])
        offset += length

    positions = [0] * rails
    result = []
    for row in sequence:
        result.append(rows[row][positions[row]])
        positions[row] += 1
    return "".join(result)


def main():
    mode = input("Choose encrypt or decrypt: ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        raise ValueError("Choose either encrypt or decrypt.")

    text = input("Enter plaintext: " if mode == "encrypt" else "Enter ciphertext: ")
    rails = int(input("Enter number of rails: "))
    result = encrypt(text, rails) if mode == "encrypt" else decrypt(text, rails)
    print("Cipher:" if mode == "encrypt" else "Plaintext:", result)


if __name__ == "__main__":
    main()
