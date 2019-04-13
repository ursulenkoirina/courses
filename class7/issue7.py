import unittest
import sys

print(sys.platform)

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.something = 'Set up common'
        print(cls.something)

    def setUp(self):
        self.something2 = 'Set up'
        # print(self.something2)

    @unittest.skipIf(sys.platform.startswith('win'), 'Platforma')
    def test_zero(self):
        # print(cls.something)
        # print(self.something2)
        self.assertEqual(5+5,10)

    @unittest.expectedFailure
    def test_one(self):
        self.assertEqual(5+0,5)
        # self.assertDictEqual({'key1': 12,})

    def test_a(self):
        number = [12, 443,5,0,1,'dddd']
        for num in number:
            with self.subTest(num):
                print(num)
                res = num %2
                self.assertEqual(res, 0)


#
# test1 = MyTest("test_zero")
# test2 = MyTest("test_one")
#
# suite1 = unittest.TestSuite([test1,test2])
# suite1.run(test1)

unittest.main(verbosity=2)
