ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def prepare_text(text):
    letters = "".join(ch for ch in text.upper() if "A" <= ch <= "Z").replace("J", "I")
    pairs = []
    index = 0

    while index < len(letters):
        first = letters[index]
        if index + 1 == len(letters) or letters[index + 1] == first:
            filler = "Q" if first == "X" else "X"
            pairs.append(first + filler)
            index += 1
        else:
            pairs.append(first + letters[index + 1])
            index += 2
    return pairs


def make_matrix(key):
    chars = []
    for char in (key + ALPHABET).upper():
        if "A" <= char <= "Z":
            char = "I" if char == "J" else char
            if char not in chars:
                chars.append(char)
    return [chars[index:index + 5] for index in range(0, 25, 5)]


def _positions(matrix):
    return {
        char: (row, column)
        for row in range(5)
        for column, char in enumerate(matrix[row])
    }


def encrypt(text, matrix):
    positions = _positions(matrix)
    result = []
    for first, second in prepare_text(text):
        row1, col1 = positions[first]
        row2, col2 = positions[second]
        if row1 == row2:
            result.extend((matrix[row1][(col1 + 1) % 5], matrix[row2][(col2 + 1) % 5]))
        elif col1 == col2:
            result.extend((matrix[(row1 + 1) % 5][col1], matrix[(row2 + 1) % 5][col2]))
        else:
            result.extend((matrix[row1][col2], matrix[row2][col1]))
    return "".join(result)


def decrypt(ciphertext, matrix):
    letters = "".join(ch for ch in ciphertext.upper() if "A" <= ch <= "Z").replace("J", "I")
    if len(letters) % 2:
        raise ValueError("The ciphertext must contain an even number of letters.")

    positions = _positions(matrix)
    result = []
    for index in range(0, len(letters), 2):
        first, second = letters[index:index + 2]
        row1, col1 = positions[first]
        row2, col2 = positions[second]
        if row1 == row2:
            result.extend((matrix[row1][(col1 - 1) % 5], matrix[row2][(col2 - 1) % 5]))
        elif col1 == col2:
            result.extend((matrix[(row1 - 1) % 5][col1], matrix[(row2 - 1) % 5][col2]))
        else:
            result.extend((matrix[row1][col2], matrix[row2][col1]))
    return "".join(result)


def main():
    mode = input("Choose encrypt or decrypt: ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        raise ValueError("Choose either encrypt or decrypt.")

    key = input("Enter key: ")
    text = input("Enter plaintext: " if mode == "encrypt" else "Enter ciphertext: ")
    matrix = make_matrix(key)
    print("Matrix:", matrix)
    result = encrypt(text, matrix) if mode == "encrypt" else decrypt(text, matrix)
    print("Cipher:" if mode == "encrypt" else "Plaintext:", result)


if __name__ == "__main__":
    main()
