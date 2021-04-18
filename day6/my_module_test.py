from unittest import TestCase, main
from day6.my_module import my_function


class MyTestCase(TestCase):

    def test_given_no_parameter_when_run_app_then_return_null_string(self):
        self.assertEqual("", my_function())

    def test_given_null_string_parameter_when_run_app_with_it_then_return_null_string(self):
        self.assertEqual("", my_function(""))

    def test_given__3333__when_run_pp_with_it_then_return__3333(self):
        self.assertEqual("3333", my_function("3333"))

    def test_given__0290008282__when_run_app_with_it_then_return__XXXXXX8282(self):
        self.assertEqual("******8282", my_function("0290008282"))

    def test_given__01012345678__when_run_app_with_it_then_return__XXXXXXX5678(self):
        self.assertEqual("*******5678", my_function("01012345678"))


if __name__ == '__main__':
    main()
