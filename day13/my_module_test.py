from unittest import TestCase, main
from day13.my_module import my_function


class MyTestCase(TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_None(self):
        self.assertEqual(None, my_function())

    def test_given_not_list_parameters_when_run_with_them_then_return_None(self):
        self.assertEqual(None, my_function([], 0))

    def test_given_null_list_when_run_app_with_it_then_return_None(self):
        self.assertEqual(None, my_function([], []))

    def test_given_valid_lists_when_run_app_with_them_then_return_valid_result(self):
        self.assertEqual([[4], [6]], my_function([[1], [2]], [[3], [4]]))
        self.assertEqual([[4, 6], [7, 9]], my_function([[1, 2], [2, 3]], [[3, 4], [5, 6]]))


if __name__ == '__main__':
    main()
