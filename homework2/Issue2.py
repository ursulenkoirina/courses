# Issue2.1
a = 179
b = 971
c = pow((a**2+b**2), 0.5)
print('Length of the hypotenuse:', c)
# Issue2.2
number = 98
print('Number of tens: ', number//10)
# Issue2.3
number1 = 123
number_str =str(number1)
a = int(number_str[0])
b = int(number_str[1])
c = int(number_str[2])
sum = a + b +c
print("Sum of numbers", sum)
# Issue2.4
n = 19
if n%2 ==0:
    print('Even number: ', n+2)
else:
    print('Even number:', n+1)
# Issue2.5
num = 445.665555
print('Float part of number: ', num - int(num))
# Issue2.6
num = 333444.66666
num_list = (str(num)).split('.')
print('The first number of float part of number:', num_list[1][0])
