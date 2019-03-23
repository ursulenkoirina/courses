"""
Задание 3
Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом. Каждое слово на новой строке.
* (доп.) Рядом со словом укажите сколько раз оно встречалось в тексте
"""

file1 = open("file1.txt", "r")
file2 = open("file4.txt", "w")
l = sorted((file1.read()).split())
for word in l:
    file2.write(word + ' ' + ': ' + str(l.count(word)) + '\n')
file1.close()
file2.close()
