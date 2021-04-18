from unittest import TestCase, main
from day8.my_module import my_function


class MyTestCase(TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_None(self):
        self.assertEqual(None, my_function())

    def test_given__x_negative_10000001__when_run_with_it_then_return_None(self):
        self.assertEqual(None, my_function(-10000001, 1))

    def test_given__x_10000001_when_run_with_it_then_return_None(self):
        self.assertEqual(None, my_function(10000001, 1))

    def test_given__n_negative_1__when_run_with_it_then_return_None(self):
        self.assertEqual(None, my_function(1, -1))

    def test_given__n_1001__when_run_with_it_then_return_None(self):
        self.assertEqual(None, my_function(1, 1001))

    def test_given__n_2_x_5__when_run_with_them_then_return_list_of_2_4_6_8_10(self):
        self.assertEqual([2, 4, 6, 8, 10], my_function(2, 5))

    def test_given__n_4_x_3__when_run_with_them_then_return_list_of_4_8_12(self):
        self.assertEqual([4, 8, 12], my_function(4, 3))

    def test_given_n_negative_4_x_2__when_run_with_them_then_return_list_of_negative_4_negative_8(self):
        self.assertEqual([-4, -8], my_function(-4, 2))


if __name__ == '__main__':
    main()
