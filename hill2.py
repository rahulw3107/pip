MODULUS = 26


def mod_inverse(value, modulus):
    try:
        return pow(value, -1, modulus)
    except ValueError:
        return None


def _normalize(text):
    return "".join(ch for ch in text.upper() if "A" <= ch <= "Z")


def _inverse_key(key):
    if len(key) != 2 or any(len(row) != 2 for row in key):
        raise ValueError("The key must be a 2 by 2 matrix.")

    a, b = key[0]
    c, d = key[1]
    determinant = (a * d - b * c) % MODULUS
    inverse_determinant = mod_inverse(determinant, MODULUS)
    if inverse_determinant is None:
        raise ValueError("The key matrix is not invertible modulo 26.")

    return [
        [d * inverse_determinant % MODULUS, -b * inverse_determinant % MODULUS],
        [-c * inverse_determinant % MODULUS, a * inverse_determinant % MODULUS],
    ]


def encrypt(text, key):
    text = _normalize(text)
    if len(text) % 2:
        text += "X"

    result = []
    for index in range(0, len(text), 2):
        vector = [ord(text[index]) - 65, ord(text[index + 1]) - 65]
        result.extend(
            chr(sum(key[row][col] * vector[col] for col in range(2)) % MODULUS + 65)
            for row in range(2)
        )
    return "".join(result)


def decrypt(text, key, plaintext_length=None):
    text = _normalize(text)
    if len(text) % 2:
        raise ValueError("The ciphertext length must be even.")

    inverse_key = _inverse_key(key)
    result = []
    for index in range(0, len(text), 2):
        vector = [ord(text[index]) - 65, ord(text[index + 1]) - 65]
        result.extend(
            chr(sum(inverse_key[row][col] * vector[col] for col in range(2)) % MODULUS + 65)
            for row in range(2)
        )
    plaintext = "".join(result)
    if plaintext_length is not None:
        if not 0 <= plaintext_length <= len(plaintext):
            raise ValueError("The plaintext length is outside the decoded text.")
        plaintext = plaintext[:plaintext_length]
    return plaintext


def main():
    mode = input("Choose encrypt or decrypt: ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        raise ValueError("Choose either encrypt or decrypt.")

    key = [[3, 3], [2, 5]]
    if mode == "encrypt":
        text = input("Enter plaintext: ")
        print("Cipher:", encrypt(text, key))
    else:
        text = input("Enter ciphertext: ")
        length_text = input("Original plaintext length (optional): ").strip()
        length = int(length_text) if length_text else None
        print("Plaintext:", decrypt(text, key, length))
    print("Key:", key)


if __name__ == "__main__":
    main()
