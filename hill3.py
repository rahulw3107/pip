MODULUS = 26


def mod_inverse(value, modulus):
    try:
        return pow(value, -1, modulus)
    except ValueError:
        return None


def _normalize(text):
    return "".join(ch for ch in text.upper() if "A" <= ch <= "Z")


def _inverse_key(key):
    if len(key) != 3 or any(len(row) != 3 for row in key):
        raise ValueError("The key must be a 3 by 3 matrix.")

    a, b, c = key[0]
    d, e, f = key[1]
    g, h, i = key[2]
    cofactors = [
        [e * i - f * h, f * g - d * i, d * h - e * g],
        [c * h - b * i, a * i - c * g, b * g - a * h],
        [b * f - c * e, c * d - a * f, a * e - b * d],
    ]
    determinant = sum(key[0][column] * cofactors[0][column] for column in range(3))
    inverse_determinant = mod_inverse(determinant % MODULUS, MODULUS)
    if inverse_determinant is None:
        raise ValueError("The key matrix is not invertible modulo 26.")

    return [
        [cofactors[column][row] * inverse_determinant % MODULUS for column in range(3)]
        for row in range(3)
    ]


def _transform(text, key):
    result = []
    for index in range(0, len(text), 3):
        vector = [ord(text[index + offset]) - 65 for offset in range(3)]
        result.extend(
            chr(sum(key[row][col] * vector[col] for col in range(3)) % MODULUS + 65)
            for row in range(3)
        )
    return "".join(result)


def encrypt(text, key):
    text = _normalize(text)
    text += "X" * (-len(text) % 3)
    return _transform(text, key)


def decrypt(text, key, plaintext_length=None):
    text = _normalize(text)
    if len(text) % 3:
        raise ValueError("The ciphertext length must be a multiple of 3.")

    plaintext = _transform(text, _inverse_key(key))
    if plaintext_length is not None:
        if not 0 <= plaintext_length <= len(plaintext):
            raise ValueError("The plaintext length is outside the decoded text.")
        plaintext = plaintext[:plaintext_length]
    return plaintext


def main():
    mode = input("Choose encrypt or decrypt: ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        raise ValueError("Choose either encrypt or decrypt.")

    key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
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
