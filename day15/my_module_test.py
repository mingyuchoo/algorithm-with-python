from unittest import TestCase, main
from day15.my_module import my_function


class MyTestCase(TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_None(self):
        self.assertEqual(None, my_function())

    def test_given_not_valid_type_when_run_app_with_them_then_return_None(self):
        self.assertEqual(None, my_function("", 0))

    def test_given_valid_parameters_when_run_with_them_then_return_valid_data(self):
        self.assertEqual(29, my_function([1, 4, 2], [5, 4, 4]))
        self.assertEqual(10, my_function([1, 2], [3, 4]))


if __name__ == '__main__':
    main()
