def _column_order(key):
    if not key:
        raise ValueError("The key must not be empty.")
    return sorted(range(len(key)), key=lambda index: (key[index], index))


def encrypt(text, key):
    order = _column_order(key)
    columns = len(key)
    return "".join(
        text[index]
        for column in order
        for index in range(column, len(text), columns)
    )


def decrypt(ciphertext, key):
    order = _column_order(key)
    columns = len(key)
    full_rows, extra_chars = divmod(len(ciphertext), columns)
    column_lengths = [
        full_rows + (1 if column < extra_chars else 0)
        for column in range(columns)
    ]

    decoded_columns = [""] * columns
    offset = 0
    for column in order:
        length = column_lengths[column]
        decoded_columns[column] = ciphertext[offset:offset + length]
        offset += length

    return "".join(
        decoded_columns[column][row]
        for row in range(full_rows + (1 if extra_chars else 0))
        for column in range(columns)
        if row < column_lengths[column]
    )


def main():
    mode = input("Choose encrypt or decrypt: ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        raise ValueError("Choose either encrypt or decrypt.")

    text = input("Enter plaintext: " if mode == "encrypt" else "Enter ciphertext: ")
    key = input("Enter key: ")
    result = encrypt(text, key) if mode == "encrypt" else decrypt(text, key)
    print("Cipher:" if mode == "encrypt" else "Plaintext:", result)


if __name__ == "__main__":
    main()
