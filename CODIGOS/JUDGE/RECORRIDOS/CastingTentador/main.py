'''
Casting Tentador

A -> B -> C
A -> C
C -/> A

Grafo Dirigido
'''
from collections import deque

def searchUtil(v, g, visited):

    q = deque()
    visited[v] = True
    q.append(v)

    while q:

        node = q.popleft()
        for adj in g[node]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)


def search(g):

    n = len(g)
    visited = [False] * n

    for i in range(0, 1):
        if not visited[i]:
            searchUtil(i, g, visited)

    if False in visited:
        return False
    else:
        return True

if __name__ == "__main__":

    N, M = map(int, input().strip().split())
    g = []
    invg = []

    for i in range(N):
        g.append([])
        invg.append([])

    for i in range(M):
        a, b = map(int, input().strip().split())
        g[a].append(b)
        invg[b].append(a)

    if search(g) and search(invg):
        print("CASTING COMPLETO")
    else:
        print("HAY QUE REPETIR")