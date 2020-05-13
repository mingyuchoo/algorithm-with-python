import unittest
from template.solution import solution


class SolutionTestCase(unittest.TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_null_string(self):
        self.assertEqual(None, solution())

    def test_given_null_string_when_run_app_with_it_then_return_null_string(self):
        self.assertEqual(None, solution(0))


if __name__ == '__main__':
    unittest.main()
