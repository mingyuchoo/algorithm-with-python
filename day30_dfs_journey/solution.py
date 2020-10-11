from collections import defaultdict


def dfs(graph, root):
    stack = [root]
    visited = []

    while stack:
        print(stack)
        item = stack.pop()
        visited.append(item)
        if graph[item]:
            stack.append(graph[item].pop(0))
    return visited


def solution(matrix, root):
    graph = defaultdict(list)

    for array in matrix:
        graph[array[0]].append(array[1])
        graph[array[0]].sort()
    return dfs(graph, root)
