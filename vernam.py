def _letters(text):
    return "".join(ch for ch in text.upper() if "A" <= ch <= "Z")


def _is_ascii_letter(char):
    upper = char.upper()
    return len(upper) == 1 and "A" <= upper <= "Z"


def _transform(text, key, direction):
    key = _letters(key)
    if any(not _is_ascii_letter(char) for char in text if char.isalpha()):
        raise ValueError("Text must use English letters A through Z.")

    text_letters = _letters(text)
    if len(key) != len(text_letters):
        raise ValueError("The key must have one letter for each plaintext letter.")

    result = []
    key_index = 0
    for char in text:
        if _is_ascii_letter(char):
            base = ord("A") if char.isupper() else ord("a")
            value = (ord(char.upper()) - ord("A") + direction * (ord(key[key_index]) - ord("A"))) % 26
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
    key = input("Enter key (one letter per text letter): ")
    result = encrypt(text, key) if mode == "encrypt" else decrypt(text, key)
    print("Cipher:" if mode == "encrypt" else "Plaintext:", result)


if __name__ == "__main__":
    main()
