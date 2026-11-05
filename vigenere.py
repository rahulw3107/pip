def _letters(text):
    return "".join(ch for ch in text.upper() if "A" <= ch <= "Z")


def _transform(text, key, direction):
    key = _letters(key)
    if not key:
        raise ValueError("The key must contain at least one English letter.")

    result = []
    key_index = 0
    for char in text:
        upper = char.upper()
        if len(upper) == 1 and "A" <= upper <= "Z":
            base = ord("A") if char.isupper() else ord("a")
            value = (
                ord(upper) - ord("A")
                + direction * (ord(key[key_index % len(key)]) - ord("A"))
            ) % 26
            result.append(chr(value + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


def encrypt(plaintext, key):
    return _transform(plaintext, key, 1)


def decrypt(ciphertext, key):
    return _transform(ciphertext, key, -1)


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
