import unittest
import sys

print(sys.platform)


class DistanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.something = "SET Up common"
        # print(cls.something)

    def setUp(self):
        self.something2 = "SET Up"
        # print(self.something2)

    def test_zero(self):
        number = [12,433,"sdfsd",0,1]
        for num in number:
            with self.subTest(num):
                print(num)
                res = num % 2
                self.assertEqual(res, 0)


    # @unittest.skipIf(sys.platform.startswith("win"), "Platform is Windows")
    @unittest.expectedFailure
    def test_one(self):
        # assert {"key1": 12, "key2": 10} == {"key1": 14, "key2": 10}
        self.assertDictEqual({"key1": 12, "key2": 10}, {"key1": 14, "key2": 10})


test1 = DistanceTests("test_zero")
test2 = DistanceTests("test_one")

suite1 = unittest.TestSuite([test1, test2])


if __name__ == "__main__":
    from HtmlTestRunner import HTMLTestRunner
    unittest.main(
        verbosity=2
        # testRunner=HTMLTestRunner(output=r"E:\workspace\untitled9")
    )
    # test1 = DistanceTests("test_zero")
    # test2 = DistanceTests("test_one")

    # print(test1.run())
    # print(test2.run())
    # suite1 = unittest.TestSuite([test1])
    #     # suite1.addTest(test2)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(DistanceTests)
    # result = unittest.TestResult()
    # suite1.run(result)
    # print(result)
