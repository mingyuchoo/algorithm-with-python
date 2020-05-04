import unittest

from .my_module import my_function


class MyTestCase(unittest.TestCase):
    def test_given_nothing_when_input_nothing_to_my_function_then_return_negative_1(self):
        self.assertEqual(-1, my_function())

    def test_given_5_when_input_5_then_it_return_6(self):
        self.assertEqual(6, my_function(5))

    def test_given_12_when_input_12_then_it_return_28(self):
        self.assertEqual(28, my_function(12))


if __name__ == '__main__':
    unittest.main()
