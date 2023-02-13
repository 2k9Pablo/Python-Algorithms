def selectMin(visited, distances):
    node = None
    bestDist = float('inf')

    for i in range(len(distances)):
        if not visited[i] and distances[i] < bestDist:
            node = i
            bestDist = distances[i]

    return node, bestDist

def coste(g):

    n = len(g)
    visited = [False] * n
    distances = [float('inf')] * n

    visited[0] = True
    distances[0] = 0

    for src, dst, weight in g[0]:
        distances[dst] = weight

    total = 0

    for i in range(1, n):

        nextNode, cost = selectMin(visited, distances)

        if cost < float('inf'):
            total += cost
            visited[nextNode] = True

            for src, dst, weight in g[nextNode]:
                if not visited[dst]:
                    distances[dst] = min(distances[dst], weight)

    if total % 5 == 0:
        return total // 5

    else:
        return total // 5 + 1

if __name__ == "__main__":
    n, m = map(int, input().strip().split())

    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        s, d, w = map(int, input().strip().split())
        g[s].append((s, d, w))
        g[d].append((d, s, w))

    print(coste(g))