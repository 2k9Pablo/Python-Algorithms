from collections import deque


def TopologicalSortUtil(g, node, visited, topo):
    visited[node] = True
    for i in g[node]:
        if not visited[i]:
            TopologicalSortUtil(g, i, visited, topo)

    topo.appendleft(node)

def TopologicalSort(g):
    n = len(g)
    visited = [False] * n
    topo = deque()

    for i in range(n):
        if not visited[i]:
            TopologicalSortUtil(g, i, visited, topo)

    return topo

if __name__ == '__main__':
    graph = [
        [1, 2, 4],
        [2],
        [3, 4],
        [],
        []
    ]

    print(TopologicalSort(graph))
