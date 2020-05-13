import unittest
from day17.solution import solution


class SolutionTestCase(unittest.TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_null_string(self):
        self.assertEqual(True, solution())

    def test_given_null_string_when_run_app_with_it_then_return_null_string(self):
        self.assertEqual(True, solution(0))

    def test_given_valid_parameters_when_run_with_them_then_return_valid_answer(self):
        self.assertEqual(False, solution(['119', '97674223', '1195524421']))
        self.assertEqual(True, solution(['123', '456', '789']))


if __name__ == '__main__':
    unittest.main()
