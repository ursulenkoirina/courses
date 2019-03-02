
a = """
We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)
"""
# 7.1 Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
line_list = a.split()
print('Number of words: ', len(line_list))
# 7.2 Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
l = []
for i in line_list:
    if '(' in i or ')' in i or '.' in i or '!' in i:
        i = i.strip('().!')
    l.append(i)
print('List without punctuation marks: \n', l)
# 7.3 Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
sort_list = sorted(l)
print('Sorted list: \n', sort_list)
#7.4
"""
Посчитать, сколько раз встречается каждое слово.
(Подсказка: создавать словарь, где ключи — это слова из текста,
а в значениях подсчитываем количество «встречаний» этого слова)
"""
#Solution1
j = 0
value_dict = {}
for i in sort_list:
    j = sort_list.count(i)
    value_dict[i] = j
print('Solution1 My dict is : \n', value_dict)
#Solution2
value_dict = {}
for i in sort_list:
    if i in value_dict:
        value_dict[i] +=1
    else:
        value_dict[i] = 1
print('Solution2 My dict is : \n', value_dict)
