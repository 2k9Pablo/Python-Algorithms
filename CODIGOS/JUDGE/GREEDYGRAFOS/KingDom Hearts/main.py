'''
KingDom Hearts
'''
def selectMin(visited, distances):
    node = None
    bestDist = float('inf')

    for i in range(len(visited)):
        if not visited[i] and distances[i] < bestDist:
            node = i
            bestDist = distances[i]

    return node, bestDist

def Prim(g):

    n = len(g)
    visited = [False] * n
    distances = [float('inf')] * n

    initial = 0
    visited[initial] = True
    distances[initial] = 0

    for src, dst, enem in g[initial]:
        distances[dst] = enem


    total = 0
    for i in range(1, n):
        nextNode, cost = selectMin(visited, distances)

        if cost < float('inf'):
            total += cost
            visited[nextNode] = True

            for src, dst, enem in g[nextNode]:
                if not visited[dst]:
                    distances[dst] = min(distances[dst], enem)

    return total

if __name__ == "__main__":

    n, m = map(int, input().strip().split())
    g = []

    for _ in range(n):
        g.append([])

    for _ in range(m):
        u, v, e = map(int, input().strip().split())

        g[u].append((u, v, e))
        g[v].append((v, u, e))

    print(Prim(g))