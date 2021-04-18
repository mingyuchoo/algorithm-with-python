from unittest import TestCase, main
from day23_feature.solution import solution


class MyTestCase(TestCase):
    def test_something(self):
        self.assertEqual([2, 1], solution([93, 30, 55], [1, 30, 5]))


if __name__ == '__main__':
    main()
