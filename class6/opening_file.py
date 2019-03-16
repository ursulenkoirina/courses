#1 Записать песню
from la import generates_song
a = generates_song(5, 10, 1)
f = open("song.txt", "a")
f.write(a)

#2 Напечать файл
f = open("Person.py", "r")
# print(f.read())

#3 Считать построчно
f = open("Person.py", "r")
# a = f.readlines()
# print(a)
l = []
for i in f:
    c = (i.rstrip('\n')).strip() + '!'
    l.append(c)
print(l)

input_file = open("Person.py")
for line in input_file:
    print(line.rstrip() + '!')