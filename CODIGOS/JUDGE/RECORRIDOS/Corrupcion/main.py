'''
Corrupción

A -> B
B -> A

Relaciones Bidireccionales
Grafo no dirigido
'''

def isCyclicUtil(g, v, visited, parent):

    visited[v] = True

    for adj in g[v]:
        if not visited[adj]:
            if isCyclicUtil(g, adj, visited, v):
                return True

        elif parent != adj:
            return True

    return False

def isCyclic(g):

    n = len(g)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            if isCyclicUtil(g, i, visited, -1):
                return True

    return False

if __name__ == "__main__":

    N, M = map(int, input().strip().split())
    g = []
    for i in range(N):
        g.append([])

    for i in range(M):

        a, b = map(int, input().strip().split())
        g[a].append(b)
        g[b].append(a)

    if isCyclic(g):
        print("CORRUPTOS")
    else:
        print("INOCENTES")