def discrete_log(g, h, p):
    value = 1
    for x in range(p):
        if value == h:
            return x
        value = (value * g) % p
    return None

g = int(input("Enter g: "))
h = int(input("Enter h: "))
p = int(input("Enter prime p: "))
print("Discrete logarithm:", discrete_log(g, h, p))
