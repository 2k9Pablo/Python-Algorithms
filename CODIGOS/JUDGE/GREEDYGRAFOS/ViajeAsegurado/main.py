'''
Viaje Asegurado
'''
def selectMin(visited, distances):
    node = None
    bestDist = float('inf')

    for i in range(len(visited)):
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

    return max(distances)

if __name__ == "__main__":

    n, m = map(int, input().strip().split())
    g = []
    for _ in range(n):
        g.append([])

    for _ in range(m):
        s, d, c = map(int, input().strip().split())
        g[s].append((s, d, c))
        g[d].append((d, s, c))


    result = [0] * n
    for i in range(n-1):
        result[i] = Dijkstra(g, i)

    print(max(result))