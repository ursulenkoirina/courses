names =['vasya','Sasha', 'olena', '1234678', 'KOLYA']
names = [name.title() if name.isalpha() else int(name) for name in names]
# names.sort()
print(names)

names_dict =['vasya', 'Sasha', 'olena', '1234678', 'Kolya']
d = {i: len(i) for i in names_dict}
print(d)

d = {'a': 'V', 'b': 'W', 'age': 34}
d2 = {k: d[k].lower() for k in d if type(d[k])==str}
print(d2)

names =['vasya','Sasha', 'olena', '1234678', 'KOLYA']
names = (name.title() for name in names if name.isalpha())
print(next(names))
print(next(names))

for i in names:
    print(i)