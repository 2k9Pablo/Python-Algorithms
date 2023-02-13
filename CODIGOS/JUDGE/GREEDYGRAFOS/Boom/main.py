'''
Boom
'''
def selectMin(visited, distances):

    node = None
    bestDist = float('inf')
    for i in range(len(distances)):
        if not visited[i] and distances[i] < bestDist:
            node = i
            bestDist = distances[i]

    return node, bestDist

def Dijkstra(g, initial):

    n = len(g)
    visited = [False] * n
    distances = [float('inf')] * n

    visited[initial] = True
    distances[initial] = 0

    for src, dst, weight in g[initial]:
        distances[dst] = weight

    for i in range(1, n):
        nextNode, cost = selectMin(visited, distances)

        if cost < float('inf'):
            visited[nextNode] = True


        for src, dst, weight in g[nextNode]:

            distances[dst] = min(distances[dst], distances[src] + weight)

    return distances



if __name__ == "__main__":

    n, m = map(int, input().strip().split())
    tipos = list(map(int, input().strip().split()))

    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        c, d, l = map(int, input().strip().split())
        g[c].append((c, d, l))
        g[d].append((d, c, l))

    result = [float('inf')] * len(set(tipos))

    for i in range(n):

        bestDist = float('inf')

        if g[i]:

            distances = Dijkstra(g, i)

            for j in range(n):
                if tipos[j] == tipos[i] and j != i:
                    if distances[j] < bestDist:
                        bestDist = distances[j]

            if bestDist < result[tipos[i]]:
                result[tipos[i]] = bestDist

    print(*result)