import unittest
from day22_bridge.solution import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(8, solution(2, 10, [7, 4, 5, 6]))
        self.assertEqual(101, solution(100, 100, [10]))
        self.assertEqual(110, solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))



if __name__ == '__main__':
    unittest.main()
