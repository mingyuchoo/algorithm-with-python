import unittest
from day12.my_module import my_function, masking_string, convert_binary


class MaskingStringTestCase(unittest.TestCase):
    def test_given_nothing_when_check_the_parameter_is_valid_then_return_None(self):
        self.assertEqual(None, masking_string())

    def test_given_not_string_parameter_when_check_the_parameter_is_valid_then_return_None(self):
        self.assertEqual(None, masking_string(0, ''))
        self.assertEqual(None, masking_string('', 0))
        self.assertNotEqual(None, masking_string('', ''))

    def test_given_different_size_of_two_list_when_check_whether_the_length_of_them_is_equal_or_not_then_return_None(self):
        self.assertEqual(None, masking_string('1', '12'))

    def test_given_two_string_consisted_of_just_one_character_when_check_masked_correctly_then_return_valid_result(self):
        self.assertEqual('#', masking_string('1', '1'))
        self.assertEqual(' ', masking_string('0', '0'))
        self.assertEqual('#', masking_string('0', '1'))
        self.assertEqual('#', masking_string('1', '0'))

    def test_given_two_binary_string_when_check_masked_correctly_then_return_valid_result(self):
        self.assertEqual('#####', masking_string('01001', '11110'))
        self.assertEqual('# # #', masking_string('10100', '00001'))
        self.assertEqual('### #', masking_string('11100', '10101'))


class ConvertBinaryTestCase(unittest.TestCase):
    def test_given_nothing_when_check_the_parameter_is_valid_then_return_negative_1(self):
        self.assertEqual(-1, convert_binary())

    def test_given_valid_parameters_when_check_the_number_is_converted_correctly_to_binary_string_then_return_right_value(self):
        self.assertEqual("01001", convert_binary(5, 9))
        self.assertEqual("10100", convert_binary(5, 20))
        self.assertEqual("00001", convert_binary(5, 1))


class MyFunctionTestCase(unittest.TestCase):
    def test_given_nothing_when_check_the_parameters_are_given_correctly_then_return_empty_list(self):
        self.assertEqual([], my_function())

    def test_given_0_and_empty_list_when_check_the_parameters_are_given_correctly_then_return_empty_list(self):
        self.assertEqual([], my_function(0, [], []))

    def test_given_17_and_empty_list_when_check_the_length_of_size_is_valid_then_return_empty_list(self):
        self.assertEqual([], my_function(17, [], []))

    def test_given_n_and_two_lists_when_check_whether_the_length_is_the_same_or_not_then_return_not_empty_list(self):
        self.assertNotEqual([], my_function(2, [1, 2], [2, 3]))
        self.assertEqual([], my_function(2, [1], [2, 3]))
        self.assertEqual([], my_function(2, [1, 2], [3]))

    def test_given_valid_parameters_when_try_to_draw_map_then_return_valid_map(self):
        self.assertEqual(["#####", "# # #", "### #", "#  ##", "#####"],
                         my_function(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
        self.assertEqual(["######", "###  #", "##  ##", " #### ", " #####", "### # "],
                         my_function(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))


if __name__ == '__main__':
    unittest.main()
