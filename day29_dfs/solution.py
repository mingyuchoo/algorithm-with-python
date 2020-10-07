# https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html


def dfs_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack += sorted(set(graph[vertex]) - set(visited), reverse=True)
    print(visited)
    return visited
