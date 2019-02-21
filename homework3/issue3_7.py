a = """
We are not what we should be! We are not what we need to be. But at least we are not what we used to be (Football Coach)
"""
# 7.1 Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
line_list = a.split(' ')
print(line_list)
print(len(line_list))
# 7.2 Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
l = []
for i in line_list:
    if '(' in i:
        i = i.strip('(')
    if '\n' in i:
        i = i.strip('\n')
    if '!' in i:
        i = i.strip('!')
    if '.' in i:
        i = i.strip('.')
    if ')' in i:
        i = i.strip(')')
    l.append(i)
print(l)
#7.3 Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
sort_list = sorted(l)
print(sort_list)
#7.4
"""
Посчитать, сколько раз встречается каждое слово.
(Подсказка: создавать словарь, где ключи — это слова из текста,
а в значениях подсчитываем количество «встречаний» этого слова)
"""
j = 0
value_dict = {}
for i in sort_list:
    j = sort_list.count(i)
    value_dict[i] = j
print('My dict is : \n', value_dict)

