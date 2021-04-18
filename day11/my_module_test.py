from unittest import TestCase, main
from day11.my_module import my_function


class MyTestCase(TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_null_list(self):
        self.assertEqual([], my_function())

    def test_given_null_string_when_run_app_with_it_then_return_null_list(self):
        self.assertEqual([], my_function(""))

    def test_given_three_parameters_when_run_app_with_them_then_return_list_including_one_item(self):
        self.assertEqual([5], my_function([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3]]))
        self.assertEqual([6], my_function([1, 5, 2, 6, 3, 7, 4], [[4, 4, 1]]))
        self.assertEqual([3], my_function([1, 5, 2, 6, 3, 7, 4], [[1, 7, 3]]))

    def test_given_three_parameters_when_run_app_with_them_then_return_list_including_three_item(self):
        self.assertEqual([5, 6, 3], my_function([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


if __name__ == '__main__':
    main()
