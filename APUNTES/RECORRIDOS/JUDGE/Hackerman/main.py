'''
Hackerman

A -> B
B -> A

Relaciones Bidireccionales, Grafo no dirigido
'''
def APUtil(g, node, visited, ap, parent, low, disc, time):

    children = 0
    visited[node] = True

    disc[node] = time
    low[node] = time
    time += 1

    for adj in g[node]:

        if not visited[adj]:
            parent[adj] = node
            children += 1

            APUtil(g, adj, visited, ap, parent, low, disc, time)

            low[node] = min(low[adj], low[node])

            if parent[node] == -1 and children > 1:
                ap[node] = True

            if parent[node] != -1 and low[adj] >= disc[node]:
                ap[node] = True

        elif adj != parent[node]:
            low[node] = min(low[node], disc[adj])


def AP(g, cost):

    n = len(g)
    visited = [False] * n

    parent = [-1] * n
    disc = [float('inf')] * n
    low = [float('inf')] * n
    ap = [False] * n

    time = 0

    for i in range(n):
        if not visited[i]:
            APUtil(g, i, visited, ap, parent, low, disc, time)

    total = 0

    for i in range(n):
        if ap[i]:
            total += cost[i]

    return total

if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    g = []
    cost = []
    for i in range(N):
        g.append([])
        cost.append(int(input()))

    for i in range(M):
        a, b = map(int, input().strip().split())
        g[a].append(b)
        g[b].append(a)

    print(AP(g, cost))