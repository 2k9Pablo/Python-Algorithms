'''
Hostia Pilotes

A -> B
B -> A

Relaciones bidireccionales, Grafo no dirigido
'''
from collections import deque

def BFSUtil(g, v, visited):

    q = deque()
    visited[v] = True
    q.append(v)

    while q:
        node = q.popleft()
        for adj in g[node]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)

def BFS(g):

    n = len(g)
    visited = [False] * n

    contador = 0

    for i in range(n):
        if not visited[i]:
            BFSUtil(g, i, visited)
            contador += 1

    print(contador)


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    g = []

    for i in range(N):
        g.append([])

    for i in range(M):
        a, b = map(int, input().strip().split())
        g[a].append(b)
        g[b].append(a)

    BFS(g)