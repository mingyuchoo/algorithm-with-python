import unittest
from day23_feature.solution import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([2, 1], solution([93, 30, 55], [1, 30, 5]))


if __name__ == '__main__':
    unittest.main()
