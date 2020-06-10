import unittest
import string
from day20_linked_list.solution import LinkedList


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
        l.delete('W')
        l.delete('A')
        l.sort()


if __name__ == '__main__':
    unittest.main()
