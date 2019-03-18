from home5 import Person
"""
2) Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы, зарплата)
** (только для продвинутых) Можете в конструкторе проверить, что в опыт работы и зарплата не отрицательные 😊
Реализовать новые методы:
1. возвращает должность с приставкой, которая зависит от опыта работы: Junior — менее 3 лет, Middle — от 3 до 6 лет, Senior — больше 6 лет.
Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior <position>. Если, например у вас объект имел должность “programmer”  с опытом 2 года, метод должен вернуть “Junior programmer”
2. метод, который увеличивает зарплату на сумму, которую вы передаёте аргументом.
"""


class Employee(Person.Person):
    def __init__(self, *args, position='', experience=1, salary=1000, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position

        try:
            assert experience > 0
            self.experience = experience
        except AssertionError:
            print('Experience must be positive number')

        try:
            assert salary > 0
            self.salary = salary
        except AssertionError:
            print('Salary must be positive number')

    def experience_level(self):
        if self.experience < 3:
            result = self.position + ' ' + 'Junior'
        elif 3 <= self.experience < 6:
            result = self.position + ' ' + 'Middle'
        elif self.experience >= 6:
            result = self.position + ' ' + 'Senior'
        return result

    def new_salary(self, sum =100):
        salary_update = self.salary * sum
        return salary_update


if __name__ == "__main__":
    p2 = Employee(full_name='Irina Ursulenko', age=1991, position='Qa', experience=5, salary=2000)
    print(p2.new_salary())
    print(p2.experience_level())
