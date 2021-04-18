from unittest import TestCase, main
from day27_workout_clothes.solution import solution


class MyTestCase(TestCase):
    def test_something(self):
        self.assertEqual(5, solution(5, [2, 4], [1, 3, 5]))
        self.assertEqual(4, solution(5, [2, 4], [3]))
        self.assertEqual(2, solution(3, [3], [1]))


if __name__ == '__main__':
    main()
