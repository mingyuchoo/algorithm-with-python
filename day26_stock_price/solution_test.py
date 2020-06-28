import unittest
from day26_stock_price.solution import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([4, 3, 1, 1, 0], solution([1, 2, 3, 2, 3]))


if __name__ == '__main__':
    unittest.main()
