# from class5 import class5_1
from class5 import class5_1


class Employee(class5_1.Person):
    def __init__(self, *args, position='', salary=0, **kwargs):
    # def __init__(self, name='', surname='', age=None, position='', salary=0):
    #     class5_1.Person.__init__(self, *args, **kwargs)
        # class5_1.Person.__init__(self, name, surname, age)
        super().__init__(*args, **kwargs)
        self.position = position
        self.salary = salary

    def income(self, month=1):
        self.salary = self.salary * month
        return self.salary

    def __str__(self):
        old = super().__str__()
        result = old.replace("Person",'Employee')
        return result


# e1 = Employee('Irina', salary=1000)
# print(e1.income(2))
# print(e1)



class ITemployee(Employee):

    """ Class description"""

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)
        return self.skills

    def __str__(self):
        old = super().__str__()
        result = old.replace("Employee", 'ITemployee')
        return result

if __name__ =="__main__":
    a = ITemployee(name='Olya', surname="Ivanova", salary=1000, age=20)
    a.add_skill('comp')
    a.add_skill('netw')
    a.add_skill('lit')
    a.income(4)
    a.get_older(4)
    print(a)
    print(a.skills)
    print(a.salary)
    print(a.age)

