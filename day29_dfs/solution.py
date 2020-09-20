# https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
#

# graph = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}

graph = {1: {3, 4},
         2: {3, 4, 5},
         3: {1, 5},
         4: {1},
         5: {2, 6},
         6: {3, 5}
         }

root = 1


def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited


print(DFS_with_adj_list(graph, root))
