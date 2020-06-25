import unittest
from day25_iron_stick.solution import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(17, solution('()(((()())(())()))(())'))


if __name__ == '__main__':
    unittest.main()
