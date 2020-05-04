import unittest
from .my_module import my_function


class MyTestCase(unittest.TestCase):
    def test_given_a_parameter_greater_than_100000_when_input_the_parameter_then_occur_exception(self):
        self.assertEqual(False, my_function("a"*100001, "b"*100001))

    def test_given_a_parameter_smaller_than_or_equal_to_100000_when_input_the_parameter_then_return_True(self):
        self.assertEqual(True, my_function("a"*100000, "a"*100000))

    def test_given__ABCDE1__and__bc1deee__when_check_only_alphabet_then_return_False(self):
        self.assertEqual(False, my_function("ABCDE1", "bc1deee"))

    def test_given__listen__and__silent__when_check_anagram_then_return_True(self):
        self.assertEqual(True, my_function("listen", "silent"))

    def test_given__Debit_card__and__Bad_credit__when_check_anagram_then_return_True(self):
        self.assertEqual(False, my_function("Debit card", "Bad credit"))


if __name__ == '__main__':
    unittest.main()
