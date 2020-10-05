import unittest
from greedy.change import change


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(change(), True)


if __name__ == '__main__':
    unittest.main()
