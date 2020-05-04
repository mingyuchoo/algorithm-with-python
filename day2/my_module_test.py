import unittest

from .my_module import my_function


class MyTestCase(unittest.TestCase):

    def test_given_nothing_when_run_my_function_should_return_False(self):
        self.assertEqual(False, my_function())

    def test_given_null_string_when_input_the_value_then_get_False(self):
        self.assertEqual(False, my_function(""))

    def test_given_string_length_is_3_when_input_the_string_then_get_False(self):
        self.assertEqual(False, my_function(123))

    def test_given_string_length_is_4_when_input_the_string_then_get_True(self):
        self.assertEqual(True, my_function(1234))
        self.assertEqual(True, my_function("0000"))

    def test_given_string_length_is_8_when_input_the_string_then_get_True(self):
        self.assertEqual(True, my_function(12345678))

    def test_given_string_length_is_9_when_input_the_string_then_get_False(self):
        self.assertEqual(False, my_function(123456789))

    def test_given_string_negative_one_when_input_the_string_then_get_False(self):
        self.assertEqual(False, my_function(-1))

    def test_given_composite_string_with_number_and_alphabet_when_input_the_value_then_get_False(self):
        self.assertEqual(False, my_function("123a"));
        self.assertEqual(my_function("1234567a"), False);