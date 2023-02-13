'''
La Fiesta de Arquimedes

A -> B -> C
A -> C
C -> A

Relaciones bidireccionales, Grafo no dirigido
'''
from collections import deque

def BFSUtil(g, v, visited):

    q = deque()
    friends = deque()
    visited[v] = True

    q.append(v)
    friends.append(v)

    while q:
        node = q.popleft()
        for adj in g[node]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)
                friends.append(adj)

    # *sorted porque si no nos imprime el deque con []
    if len(friends) > 1:
        print(*sorted(friends), sep=" ")

def BFS(g):

    n = len(g)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            BFSUtil(g, i, visited)

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