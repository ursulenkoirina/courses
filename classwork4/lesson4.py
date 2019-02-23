# while True:
#     a = input('Input less than 10 symbols: ')
#     if len(a) < 10: break
# assert len(a) < 10
# print(a)

# #Function:
# def func(*args):
#     return args
#
# print(type(func(1, 2, 3, 'abc'))) #(1, 2, 3, 'abc')
# print(func()) #()
# print(func(1)) #(1,)

# # Пишем ф-ю которая выводим второе по возрастанию значение из переданных аргументов
# def min_function(*args):
#     l = sorted(args)
#     return l[1]
#
# print(min_function(1, 3, 5, 6))

# def func(**kwargs):
#     # return kwargs
#     return '{} is {}'.format(kwargs.get('name'), kwargs.get('job'))
#
# print(func(a=1, job='lazybum', name='Bob'))

l = ['ddd', 'aa', '2223']
print(*l, sep='\n')

d = {'end': '!!!!\n', 'sep': '-'}
print('aaa', 'ddd', 'dss', **d)