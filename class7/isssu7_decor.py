class A:
    title = 'ssss'
    def __init__(self,name = ''):
        self.name = name

    @classmethod
    def method(cls):
        cls.my_list = []

    @staticmethod
    def method():
        return A()
        # my_list = []

A.method()
print(A.my_list)

a = A('aaddd')
b = A('ssss')
print(a.my_list)
print(b.my_list)
print(a.my_list is b.my_list)