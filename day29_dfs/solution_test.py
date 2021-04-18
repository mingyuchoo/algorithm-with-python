from unittest import TestCase, main
from day29_dfs.solution import dfs_with_adj_list


class MyTestCase(TestCase):

    def test_something(self):

        graph = {1: [3, 4],
                 2: [3, 4, 5],
                 3: [1, 5],
                 4: [1],
                 5: [2, 6],
                 6: [3, 5]
                 }
        root = 1
        self.assertEqual(dfs_with_adj_list(graph, root), [1, 3, 5, 2, 4, 6])

    def test_case_2(self):
        graph = {
            1: [2, 3, 8],
            2: [1, 7],
            3: [1, 4, 5],
            4: [3, 5],
            5: [3, 4],
            6: [7],
            7: [2, 6, 8],
            8: [1, 7]
        }
        root = 1
        self.assertEqual(dfs_with_adj_list(graph, root), [1, 2, 7, 6, 8, 3, 4, 5])


if __name__ == '__main__':
    main()
