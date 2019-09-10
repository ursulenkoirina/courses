"""
Задание 2
Задание из класса «Записываем “Number: строка из файла” из одного файла в другой»:
1. Кто не успел доделываем / тем, кто успел: воспользуйтесь другим способом для записи в файл
(кто сделал с помощью методов – делают с помощью print, кто сделал с помощью print – делают с помощью методов)
2. Воспользуйтесь менеджером контекста для файла (with … as), в который вы записываете информацию.
"""
# Solution1
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "w")

l = file1.readlines()
j = 0
for i in l:
    c = "Number " + str(j) + ': ' + i.strip()+'\n'
    file2.write(c)
    j += 1

file1.close()
file2.close()

# # Solution2
# with open("file1.txt", "r") as file1:
#     l = file1.readlines()
#
# j = 0
# for i in l:
#     c = "Number " + str(j) + ': ' + i.strip()+'\n'
#     j += 1
#     with open("file2.txt", "a") as file2:
#         file2.write(c)



