# class MyClass:
#     def __init__(self, const):
#         self.const = const
#
#     def __call__(self, a, b):
#         print((a + b) * self.const)
#
#
# obj = MyClass(123)
# obj2 = MyClass(1111)
#
# obj(1,2)
# obj2(1,0)

class MyClass:
    def __init__(self, const):
        self.const = const

    def __call__(self, a):
        print(a ** self.const)


pow_2 = MyClass(2)
pow_10 = MyClass(10)

pow_2(5)
pow_10(5)