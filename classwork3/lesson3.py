"""
x = 'a'
y = 'ww'
print(x, y, 11, 12,sep=',', end=' ')
print(x, y, 11, 12, sep=',')
print('hello')

# l = ['hello', 'a', 'n', 12, 90 ]
# # print(l[::-2])
# print(l[2:-1:-1])
s = "Hi there"
print(s[-2:0:-1])

#Віводить список пока не будет l empty
l = ['1', '2', '3', 'a']
while l:
    print(l.pop())
"""
# even = []
# odd = []
# l = [1, 10, 3, 5, 6, 7, 11]
# for item in l:
#     if item % 2 == 0:
#         even.append(item)
#     elif item % 2 == 1:
#         odd.append(item)
#     else:
#         print(item, 'is not intefer number')
# print(even)
# print(odd)

# l = [1, 10, 3, 5, 6, 7, 11]
# for item in l:
#     if item % 2 ==0:
#         print("Even number", item)
#     elif item %2 == 1:
#         print("Not even number",item+1)

#class1
# l = [1, 10, 3, 5, 6, 7, 11]
# for item in l:
#     if item % 2 == 1:
#         item_new = item+1
#         print(item_new)
#
# print(l)

#class2
# Заменить значение в списке
# l = [1, 10, 3, 5, 6, 7, 11]
#
# for i in range(len(l)):
#     if l[i] % 2 == 1:
#         l[i] = l[i] + 1
# print(l)

# Вввести слово, без пробела бесконечно.
# while True:
#     a = input("Input world: ")
#     if ' ' in a:
#         a = input("Input world once more: ")
#
# while True:
#     a = input("Input world: ")
#     if not ' ' in a:
#         break
#     print("Input world once more without space: ")


# # проверить число ли єто.
# while True:
#     a = input("Enter number: ")
#     if a.isdigit():
#         break
#     print("Not a number")

# s, i = 's', 0
# try:
#     s = int(s)/i
# except ValueError as e:
#     print(e)
# except ZeroDivisionError:
#     print('Zero Division Error')
# print("ddd")

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(unknow_var)
# finally:
#     print('This is last expect')
#
# print("ddd")

while True:
    a = input("Enter number: ")
    try:
       b = float(a)
       print(b)
    except ValueError:
        print("Bad number input once more")
    else:
        break



