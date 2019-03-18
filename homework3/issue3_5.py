"""
Задание 5 (на исключения)
Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом (любым),
то должна выполняться конкатенация, т. е. соединение, строк. В остальных случаях введённые числа суммируются.
"""
a = input("Input value1: ")
b = input("Input value2: ")
try:
    value1 = int(a)
    value2 = int(b)
    print('Sum of numbers: ', value1+value2)
except ValueError:
    print('Concatenation: ', a+b)

