import unittest
from day19.solution import driver


class SolutionTestCase(unittest.TestCase):
    def test_positive_01(self):
        self.assertEqual(20, driver([1, 10]))
        self.assertEqual(125, driver([100, 200]))
        self.assertEqual(89, driver([201, 210]))
        self.assertEqual(174, driver([900, 1000]))


if __name__ == '__main__':
    unittest.main()

