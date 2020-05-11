import unittest

from day0.my_module import greeting


class MyTestCase(unittest.TestCase):
    def test_given_no_name_when_call_greeting_should_print_nothing(self):
        self.assertEqual(greeting(), "")

    def test_given_name_when_call_greeting_should_print_hello(self):
        self.assertEqual(greeting("Mingyu"), "Hello, Mingyu")


if __name__ == '__main__':
    unittest.main()
