from unittest import TestCase, main
from day30_dfs_journey.solution import solution


class MyTestCase(TestCase):

    def test_case_1(self):
        journey = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
        self.assertEqual(solution(journey, "ICN"), ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'])

    def test_case_2(self):
        journey = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
        self.assertEqual(solution(journey, "ICN"), ['ICN', 'JFK', 'HND', 'IAD'])


if __name__ == '__main__':
    main()
