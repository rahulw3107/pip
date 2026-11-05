def normalize_letters(text):
    return "".join(ch for ch in text.upper() if "A" <= ch <= "Z")


def _validate_key(key):
    key = normalize_letters(key)
    if not key:
        raise ValueError("The key must contain at least one letter.")
    return key


def encrypt(plaintext, key):
    plaintext = normalize_letters(plaintext)
    key = _validate_key(key)
    keystream = (key + plaintext)[:len(plaintext)]
    return "".join(
        chr((ord(char) - ord("A") + ord(shift) - ord("A")) % 26 + ord("A"))
        for char, shift in zip(plaintext, keystream)
    )


def decrypt(ciphertext, key):
    ciphertext = normalize_letters(ciphertext)
    key = _validate_key(key)
    plaintext = ""

    for index, char in enumerate(ciphertext):
        shift = key[index] if index < len(key) else plaintext[index - len(key)]
        value = (ord(char) - ord("A") - ord(shift) + ord("A")) % 26
        plaintext += chr(value + ord("A"))

    return plaintext


def main():
    mode = input("Choose encrypt or decrypt: ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        raise ValueError("Choose either encrypt or decrypt.")

    text = input("Enter plaintext: " if mode == "encrypt" else "Enter ciphertext: ")
    key = input("Enter keyword: ")
    result = encrypt(text, key) if mode == "encrypt" else decrypt(text, key)
    print("Cipher:" if mode == "encrypt" else "Plaintext:", result)


if __name__ == "__main__":
    main()
