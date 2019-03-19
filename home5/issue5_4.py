"""
* Задание 4 (на создание тестов c помощью unittest)
Создайте наборы тестов на тестирование класса ITEmployee, который вы реализовали в Задании 1
(или Employee, или Person в зависимости до куда вы дошли в выполнении Задания 1).
"""
import unittest
from home5 import ITEmployee


class Test(unittest.TestCase):

    def setUp(self):
        self.a = ITEmployee.ITEmployee(full_name='Irina Ursulenko', age=1991, position='Qa', experience=5, salary=2000)

    def test_full_name(self):
        self.assertEqual(self.a.full_name, "Irina Ursulenko")

    def test_names(self):
        self.assertEqual(self.a.name(), "Irina")
        self.assertEqual(self.a.surname(), "Ursulenko")

    def test_age(self):
        self.assertEqual(self.a.age, 1991)

    def test_add_skill(self):
        self.a.add_skill('english')
        self.assertIn('english', self.a.skills)

    def test_add_skills(self):
        self.a.add_skills('git', 'svn')
        self.assertIn('git', self.a.skills)
        self.assertIn('svn', self.a.skills)

    def test_no_skills(self):
        self.assertEquals(len(self.a.skills), 0)



if __name__ == "__main__":
    unittest.main()
