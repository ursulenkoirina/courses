a = int(input("Input number 1: "))
b = int(input("Input number 2: "))
c = int(input("Input number 3: "))
if (a+b>c) and (b+c>a) and (c+a>b):
    print("Yes")
else:
    print("No")