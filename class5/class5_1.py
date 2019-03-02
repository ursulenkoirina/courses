class Person:
    def __init__(self, name='', surname='', age = None):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return "Person object with name= {} and surname= {}".format(self.name, self.surname)

    def full_name(self):
        result = self.name + ' ' + self.surname
        return result

    def get_older(self, years=1):
        if self.age is None:
            self.age = years
        else:
            self.age += years

        return self.age



if __name__ =="__main__":
    p1 =Person('Irina', 'Ursulenko')
    # p2 = Person('Vova', age= 30)
    # print(p1.name,p1.age)
    # print(p2.surname, p1.age)
    # print(dir(p1))
    p1.get_older()
    print(p1.age)

    print(p1.full_name())
