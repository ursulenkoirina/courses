import unittest


class MyTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(5+5, 10)

    def test_one(self):
        self.assertEqual(5+0, 5)

if __name__ == "__main__":
    from HtmlTestRunner import HtmlTestRunner
    unittest.main(
        verbosity=2,
        testRunner=HtmlTestRunner(output=r'path')
    )
    # unittest.main(verbosity=2)
    # test1 = MyTest("test_zero")
    # test2 = MyTest("test_one")
    #
    # print(test1.run())
    # print(test2.run())
    # suite1 = unittest.TestSuite([test1])
    # suite1.addTest(test2)
    # result = unittest.TestResult()
    # print(result)
    # suite1.run(result)
    # print(result)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    # result = unittest.TestResult()
    # suite1.run(result)
    # print(result)