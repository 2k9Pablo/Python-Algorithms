'''
Edsger
'''
from collections import deque

def selectMin(visited, distances):
    node = None
    bestDist = float('inf')

    for i in range(1, len(visited)):
        if not visited[i] and distances[i] < bestDist:
            node = i
            bestDist = distances[i]

    return node, bestDist

def Dijkstra(g, a, end):

    n = len(g)
    visited = [False] * n
    distances = [float('inf')] * n
    path = []

    for _ in range(n):
        path.append([])

    initial = 1
    visited[initial] = True
    distances[initial] = 0

    for src, dst, weight in g[initial]:
        distances[dst] = weight
        path[dst].append(src)
        path[dst].append(dst)

    for i in range(2, n):
        nextNode, cost = selectMin(visited, distances)

        if cost < float('inf'):
            visited[nextNode] = True

            for src, dst, weight in g[nextNode]:
                if distances[src] + weight < distances[dst]:
                    distances[dst] = distances[src] + weight
                    path[dst] = list(path[src])
                    path[dst].append(dst)

    q = deque()
    for i in range(0, len(path[end])):
        q.append(path[end][i])

    while q:
        node = q.pop()
        if node != 1 and distances[node] <= a:
            print(node, end = " ")
    print()
if __name__ == "__main__":

    n, m = map(int, input().strip().split())
    g = []

    for _ in range(n+1):
        g.append([])

    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        g[u].append((u, v, w))
        g[v].append((v, u, w))

    c, d = map(int, input().strip().split())
    for _ in range(c):
        aux = int(input())
        Dijkstra(g, d, aux)
