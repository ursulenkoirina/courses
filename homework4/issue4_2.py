"""
Задание 2
Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов. Учитываем, что может быть повторяющиеся значения аргументов.
"""
# solution1
def count_second_min1(*args):
    args = set(args)
    l = sorted(list(args))
    return l[1]
a = count_second_min1(6, 67, 1, 4, 6, 2, 3, 67, 2, 55,6)
print(a)

# solution2
def count_second_min2(*args):
    l = []
    for i in args:
        if i not in l:
            l.append(i)
    l = sorted(l)
    return l[1]
a = count_second_min2(73, 67, 67, 1, 55, 4, 2, 4, 1, 1,3)
print(a)
