def encrypt(text, key):
    return _shift(text, key)


def decrypt(text, key):
    return _shift(text, -key)


def _shift(text, key):
    result = []
    for char in text:
        if "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + key) % 26 + ord("A")))
        elif "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + key) % 26 + ord("a")))
        else:
            result.append(char)
    return "".join(result)


def main():
    mode = input("Choose encrypt or decrypt: ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        raise ValueError("Choose either encrypt or decrypt.")

    text = input("Enter plaintext: " if mode == "encrypt" else "Enter ciphertext: ")
    key = int(input("Enter shift key: "))
    result = encrypt(text, key) if mode == "encrypt" else decrypt(text, key)
    print("Cipher:" if mode == "encrypt" else "Plaintext:", result)


if __name__ == "__main__":
    main()
