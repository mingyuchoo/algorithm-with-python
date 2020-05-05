import unittest
from day1.my_module import my_function


class MyTestCase(unittest.TestCase):
    def test_given_nothing_when_run_my_function_should_return_even(self):
        self.assertEqual(my_function(), "Even")

    def test_given_zero_when_run_my_function_should_return_even(self):
        self.assertEqual(my_function(0), "Even")

    def test_given_one_when_run_my_function_should_return_odd(self):
        self.assertEqual(my_function(1), "Odd")


if __name__ == '__main__':
    unittest.main()
