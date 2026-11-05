import random
import string


ALPHABET = string.ascii_uppercase


def _validate_key(key):
    key = key.upper()
    if len(key) != len(ALPHABET) or set(key) != set(ALPHABET):
        raise ValueError("The key must be a permutation of A through Z.")
    return key


def encrypt(text, key):
    key = _validate_key(key)
    return text.translate(str.maketrans(ALPHABET + ALPHABET.lower(), key + key.lower()))


def decrypt(text, key):
    key = _validate_key(key)
    return text.translate(str.maketrans(key + key.lower(), ALPHABET + ALPHABET.lower()))


def main():
    mode = input("Choose encrypt or decrypt: ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        raise ValueError("Choose either encrypt or decrypt.")

    text = input("Enter plaintext: " if mode == "encrypt" else "Enter ciphertext: ")
    if mode == "encrypt":
        key = "".join(random.sample(ALPHABET, len(ALPHABET)))
        print("Substitution key:", key)
        result = encrypt(text, key)
        print("Cipher:", result)
    else:
        key = input("Enter the substitution key: ")
        print("Plaintext:", decrypt(text, key))


if __name__ == "__main__":
    main()
