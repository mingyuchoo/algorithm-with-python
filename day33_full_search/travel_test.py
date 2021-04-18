from unittest import TestCase, main
from day33_full_search.travel import travel


class MyTestCase(TestCase):
    def test_something(self):
        self.assertEqual(travel(5, ['R', 'R', 'R', 'U', 'D', 'D']), (3, 4))


if __name__ == '__main__':
    main()
