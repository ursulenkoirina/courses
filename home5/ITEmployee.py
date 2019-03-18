from home5 import Employee

"""
3) ITEmployee (наследуемся от Employee)
1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым методом add_skill (см. презентацию).
2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список) новым методом add_skills.
Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы расширяете список-свойство skill,
или вы принимаете неопределённое количество аргументов, и все их добавляете в список-свойство skill
"""


class ITEmployee(Employee.Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)
        return self.skills

    def add_skills(self, *args):
        self.skills.extend(args)
        return self.skills


if __name__ == "__main__":
    p3 = ITEmployee(full_name='Irina Ursulenko')
    p3.add_skill('network')
    p3.add_skills('java', 'python')
    print(p3.skills)




