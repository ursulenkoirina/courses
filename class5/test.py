import unittest

from class5 import distance


class TestDistance(unittest.TestCase):

    def test_zero_coor(self):
        res = distance.distance(0, 0, 0, 0)
        self.assertEqual(res, 0)

    def test_1(self):
        res = distance.distance(0, 0, 1, 1)
        self.assertEqual(res, 2**0.5)

    def test_2(self):
        res = distance.distance(0, 0, 3, 4)
        self.assertEqual(res, 5)


if __name__ == "__main__":
    unittest.main()

