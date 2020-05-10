import unittest
from day14.my_module import my_function


class MyTestCase(unittest.TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_None(self):
        self.assertEqual(None, my_function())

    def test_given_null_string_when_run_app_with_it_then_return_None(self):
        self.assertEqual(None, my_function(0, ""))

    def test_given_number_and_remove_count_when_run_with_them_then_return_the_biggest_number(self):
        self.assertEqual(775841, my_function("4177252841", 4))


if __name__ == '__main__':
    unittest.main()
