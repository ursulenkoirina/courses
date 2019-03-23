"""
Задание 5 * (доп.)
Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата (В первой строке заголовки колонок)
Посчитайте сколько отделов на фирме
Определите максимальную зарплату
Определите максимальную зарплату в каждом отделе
Выведите «Отдел Макс_Зарплата  Фамилия_человека_с_такой_зарплатой» в новый файл
Подсказка: используйте словари.
"""
file1 = open("file3.txt", "r")
file2 = open("file4.txt", "w")
file = file1.readlines()
print(file)
all_dict = {}
d = {}
for i in file[1:]:
    c = i.split()
    d['Фамилия'] = c[0]
    d['Имя'] = c[1]
    d['Отдел'] = c[2]
    d['Зарплата'] = c[3]
    print(d)
all_dict.update(d)

print(all_dict)

# max_salary = max(d.values())

# print(d.values())
# print(max_salary)
def max_salary():
    d_new = []
    for k, v in d.items():
        if k == 'Зарплата':
            print(v)
            if v not in d_new:
                d_new.append(v)
    return d_new
print(max_salary())