import unittest
from template.my_module import my_function


class MyTestCase(unittest.TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_null_string(self):
        self.assertEqual(None, my_function())

    def test_given_null_string_when_run_app_with_it_then_return_null_string(self):
        self.assertEqual(None, my_function(0))


if __name__ == '__main__':
    unittest.main()
