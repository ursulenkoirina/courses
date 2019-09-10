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

department = []
new_department = []
max_salary = 0

for i in file[1:]:
    c = i.split()
    d = {}
    d['Фамилия'] = c[0]
    d['Имя'] = c[1]
    d['Отдел'] = c[2]
    d['Зарплата'] = c[3]
    new_department.append(d)

for i in new_department:
    if i.get('Отдел'):
        if i.get('Отдел') not in department:
            department.append(i.get('Отдел'))
    if int(i.get('Зарплата')) > max_salary:
        max_salary = int(i.get('Зарплата'))

print('Number of departments is: ', len(department))
print('Max salary is: ', max_salary)

for j in department:
    max_salary = 0
    temp = {}
    for i in new_department:
        if j == i.get('Отдел'):
            if int(i.get('Зарплата')) > max_salary:
                max_salary = int(i.get('Зарплата'))
                temp.update(i)
    print(temp)
    file2.write(str(temp) + '\n')

#close all files
file1.close()
file2.close()