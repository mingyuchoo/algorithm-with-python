from unittest import TestCase, main
from day9.my_module import my_function


class MyTestCase(TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_None(self):
        self.assertEqual(None, my_function())

    def test_given_a_parameter__n_50000000000001_when_run_app_with_it_then_return_None(self):
        self.assertEqual(None, my_function(50000000000001))

    def test_given_a_parameter__n_121__when_run_app_with_it_then_return_144(self):
        self.assertEqual(144, my_function(121))

    def test_given_a_parameter__n_3__when_run_app_with_it_then_return_negative_1(self):
        self.assertEqual(-1, my_function(3))


if __name__ == '__main__':
    main()
