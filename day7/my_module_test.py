import unittest
from day7.my_module import my_function


class MyTestCase(unittest.TestCase):
    def test_given_nothing_when_run_app_with_nothing_then_return_null_string(self):
        self.assertEqual('', my_function())

    def test_given_null_string_when_run_app_with_it_then_return_null_string(self):
        self.assertEqual('', my_function(''))

    def test_given__a__when_run_app_with_it_then_return__A(self):
        self.assertEqual('A', my_function('a'))

    def test_given__ab__when_run_app_with_it_then_return__Ab(self):
        self.assertEqual('Ab', my_function('ab'))

    def test_given__abc__when_run_app_with_it_then_return__AbC(self):
        self.assertEqual('AbC', my_function('abc'))

    def test_given__abcd__when_run_app_with_it_then_return__AbCd(self):
        self.assertEqual('AbCd', my_function('abcd'))

    def test_given__a_ab_abc_abcd__when_run_app_with_it_then_return__A_Ab_AbC_AbCd(self):
        self.assertEqual('A Ab AbC AbCd', my_function('a ab abc abcd'))

    def test_given__try_hello_world__when_run_app_with_it_then_return__TrY_HeLlO_WoRlD(self):
        self.assertEqual('TrY HeLlO WoRlD', my_function('try hello world'))


if __name__ == '__main__':
    unittest.main()
