def numbers(v):
    print(v, bin(v), hex(v), v)


def show_ascii(name):
    for letter in name:
        ascii_code = ord(letter)
        numbers(ascii_code)


show_ascii("ABC")

r = 200
g = 240
b = 64

rgb = [r, g, b]

for v in rgb:
    numbers(v)
