from unittest import TestCase, main
from day5.my_module import my_function


class MyTestCase(TestCase):
    def test_given_Nothing_when_run_without_anything_then_return_null_string(self):
        self.assertEqual("", my_function())

    def test_given_null_string_when_run_with_it_then_return_null_string(self):
        self.assertEqual("", my_function(""))

    def test_given__a__when_run_with_it_return__a(self):
        self.assertEqual("a", my_function("a"))

    def test_given__ab__when_run_with_it_return__ab(self):
        self.assertEqual("ab", my_function("ab"))

    def test_given__abc__when_run_with_it_return__abc(self):
        self.assertEqual("b", my_function("abc"))

    def test_given__abcd__when_run_with_it_return__abcd(self):
        self.assertEqual("bc", my_function("abcd"))


if __name__ == '__main__':
    main()
