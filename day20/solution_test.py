import unittest
import string
from day20.solution import LinkedList


class MyTestCase(unittest.TestCase):

    def test_something(self):
        l = LinkedList()
        data = reversed(string.ascii_uppercase)
        for i in data:
            l.append(i)
        print(l.traversal())
        self.assertEqual(True, l.find('Z'))
        self.assertEqual(False, l.find('Hello'))

        l.delete('Z')
        print(l.traversal())

        l.delete('W')
        print(l.traversal())

        l.delete('A')
        print(l.traversal())

        l.sort()
        print(l.traversal())

if __name__ == '__main__':
    unittest.main()
