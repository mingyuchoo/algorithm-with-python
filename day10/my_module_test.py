from unittest import TestCase, main
from day10.my_module import my_function


class MyTestCase(TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_None(self):
        self.assertEqual(None, my_function())

    def test_given_a_list__1_2_3_4__when_run_app_with_it_then_return__2_point_5(self):
        self.assertEqual(2.5, my_function([1, 2, 3, 4]))

    def test_given_a_list__5_5__when_run_app_with_it_then_return__5(self):
        self.assertEqual(5, my_function([5, 5]))


if __name__ == '__main__':
    main()
