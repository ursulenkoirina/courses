a = input("Input number 1: ")
b = input("Input number 2: ")
c = input("Input number 3: ")
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)