#1 Посчитать кол-во строк с нечетніми длинами
l = ['ddd', 'da', 'dswrrr', 'd11', 'a']
length=0
for i in l:
    a = len(i)
    if a % 2 != 0:
        length += 1
print(" Numbers of odd lines in my list", length)

#2
# 2.1 Есть словарь, выведи на экран ключ значения
# 2.2 тип каждого значения
d = {'1': 'a', '2': 44, '3': 55, '4': 'ddd'}
# for i in d.items():
#     print(i)
# for v in d.values():
#     print("Type values: ", type(v))
for i in d:
    print('key: ', i, ":", 'value: ', d[i])
    print("Type values: ", type(d[i]))

