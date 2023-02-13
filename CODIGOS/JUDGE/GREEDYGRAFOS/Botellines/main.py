'''
Botellines
'''
def selectMin(visited, distances):
    node = None
    bestDist = float('inf')

    for i in range(len(distances)):
        if not visited[i] and distances[i] < bestDist:
            node = i
            bestDist = distances[i]

    return node, bestDist


def Dijkstra(g, initial, destination):

    n = len(g)
    visited = [False] * n
    distances = [float('inf')] * n
    path = []
    for i in range(n):
        path.append([])

    visited[initial] = True
    distances[initial] = 0

    for src, dst, weight in g[initial]:
        distances[dst] = weight
        path[dst].append(src)
        path[dst].append(dst)

    for i in range(1, n):

        nextNode, cost = selectMin(visited, distances)

        if cost < float('inf'):
            visited[nextNode] = True

            for src, dst, weight in g[nextNode]:
                if distances[src] + weight < distances[dst]:
                    distances[dst] = min(distances[dst], distances[src] + weight)
                    path[dst] = list(path[src])
                    path[dst].append(dst)

    print(distances[destination])
    print(*path[destination])

if __name__ == "__main__":

    n, m = map(int, input().strip().split())
    g = []
    for _ in range(n):
        g.append([])

    for _ in range(m):
        s, d, w = map(int, input().strip().split())

        g[s].append((s,d,w))
        g[d].append((d,s,w))

    s, d = map(int,input().strip().split())
    Dijkstra(g, s, d)