# class Person:
#     def printer_self(self):
#         print(self)
# if __name__ =="__main__":
#     p1 = Person()
#     print('p1: ', p1)
#     p1.printer_self()
#     print('\n')
#     p2 = Person()
#     print('p2: ',p2)
#     p2.printer_self()

class Person:
    title = 'All people'

    def printer_self(self):
        print(self)

    # def set_name(self, x):
    #     self.name = x
    def __init__(self,x):
        self.name = x




if __name__ =="__main__":

    p1 = Person("Ira")
    p2 = Person("Vova")
    print(p1.name)
    # p1.set_name('Kolya')
    # p2.set_name('Ira')

    # print(p1.title is p2.title)
    print('\n')

    # p2.set_name('Ira')
    print(p2.name)
    # print(p2.title)
    # print('p2: ',p2)
    # p2.printer_self()


a = 45
print('dd'.format())