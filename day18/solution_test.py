import unittest
from day18.solution import solution


class SolutionTestCase(unittest.TestCase):
    def test_given_nothing_when_run_app_without_nothing_then_return_0(self):
        self.assertEqual(0, solution())

    def test_given_not_valid_type_parameter_when_run_app_with_it_then_return_0(self):
        self.assertEqual(0, solution(0))

    def test_given_valid_parameters_when_run_app_with_them_then_return_right_cases(self):
        # self.assertEqual(3, solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))
        self.assertEqual(5, solution(
            [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))


if __name__ == '__main__':
    unittest.main()
