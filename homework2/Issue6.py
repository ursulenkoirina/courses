number1 = input("Input number 1: ")
number2 = input("Input number 2: ")
number3 = input("Input number 3: ")
if number1 == number2 == number3:
    print(3)
elif number1 == number2 or number2 == number1 or number1 == number3 or  number2 == number3:
    print(2)
else:
    print(0)