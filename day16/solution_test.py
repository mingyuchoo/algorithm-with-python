import unittest
from day16.solution import solution


class SolutionTestCase(unittest.TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_null_string(self):
        self.assertEqual('', solution())

    def test_given_null_string_when_run_app_with_it_then_return_null_string(self):
        self.assertEqual('', solution(0))

    def test_given_valid_parameters_when_run_with_them_then_return_valid_results(self):
        self.assertEqual('leo', solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
        self.assertEqual('vinko', solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
                                           ['josipa', 'filipa', 'marina', 'nikola']))
        self.assertEqual('mislav', solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))


if __name__ == '__main__':
    unittest.main()
