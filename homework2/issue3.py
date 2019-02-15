a = int(input("Input year: "))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print("Yes")
else:
    print("No")
