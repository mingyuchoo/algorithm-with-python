import unittest


class MyTestCase(unittest.TestCase):

    def test_case_1(self):

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
