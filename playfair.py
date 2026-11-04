def prepare_text(text):
    text = "".join(ch for ch in text.upper() if ch.isalpha()).replace("J", "I")
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        if i + 1 == len(text):
            pairs.append(a + "X")
            i += 1
        elif text[i] == text[i + 1]:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(text[i] + text[i + 1])
            i += 2

    return pairs

def make_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    chars = ""

    for ch in key.upper() + alphabet:
        if ch.isalpha() and ch != "J" and ch not in chars:
            chars += ch

    return [list(chars[i:i + 5]) for i in range(0, 25, 5)]

def encrypt(text, matrix):
    pairs = prepare_text(text)
    result = ""

    for a, b in pairs:
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == a:
                    r1, c1 = i, j
                if matrix[i][j] == b:
                    r2, c2 = i, j

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

key = input("Enter key: ")
text = input("Enter plaintext: ")
matrix = make_matrix(key)
print("Matrix:", matrix)
print("Cipher:", encrypt(text, matrix))
