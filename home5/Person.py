
"""
1) Person (два свойства: 1. теперь full_name пусть будет свойством а не функцией (одно поле, мы ожидаем - тип строка и состоит из двух слов «имя фамилия»), а свойств name и surname нету, 2. год рождения).
Реализовать методы, которые:
1.	выделяет только имя из full_name
2.	выделяет только фамилию из full_name;
3.	вычисляет сколько лет есть/исполнится в году, который передаётся параметром (obj.age_in(year)); если не передавать параметр, по умолчанию, сколько лет в этом году;
** (только для продвинутых) Можете в конструкторе проверить, что в full_name передаётся строка, состоящая из двух слов, если нет, вызывайте исключение 😊
** (только для продвинутых) Можете в конструкторе проверить, что в год рождения меньше 2019, но больше 1900, если нет вызывайте исключение
"""


class Person:
    def __init__(self, full_name='', age=1991):
        try:
            assert len(full_name.split()) == 2
            self.full_name = full_name
        except AssertionError:
            print('Full Name must be consists of two words')

        try:
            assert age >= 1900 and age <= 2019
            self.age = age
        except AssertionError:
            print('Year of birth must be less than 2019, but more than 1900')

    def name(self):
        result = self.full_name.split()[0]
        return result

    def surname(self):
        result = self.full_name.split()[1]
        return result

    def age_in(self, years=None):
        if years is None:
            age = 2019 - self.age
        else:
            age = years - self.age
        return age

if __name__ == "__main__":

    p1 = Person('Irina Ursulenko', 1981)
    print(p1.name())
    print(p1.surname())
    print(p1.age_in())
    print(p1.full_name)
