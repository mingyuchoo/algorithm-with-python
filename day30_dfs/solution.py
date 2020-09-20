from collections import defaultdict


def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        item = stack.pop()
        visited.append(item)
        if graph[item]:
            stack.append(graph[item].pop(0))
    return visited


def solution(matrix):
    graph = defaultdict(list)

    for array in matrix:
        graph[array[0]].append(array[1])
        graph[array[0]].sort()
    print(graph)
    return dfs(graph, "ICN")


if __name__ == "__main__":
    journey = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
    print(solution(journey))

    journey = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
    print(solution(journey))
