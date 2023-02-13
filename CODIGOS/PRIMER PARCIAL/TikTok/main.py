'''
TikTok
'''
from collections import deque

def bfs(g, a):

    n = len(g)
    visited = [False] * n
    distances = [float('inf')] * n
    q = deque()

    initial = 0
    visited[initial] = True
    distances[initial] = 1
    q.append(initial)

    while q:
        node = q.popleft()

        for adj in g[node]:
            if not visited[adj]:
                visited[adj] = True
                distances[adj] = distances[node] + 1
                q.append(adj)

    total = 0
    for i in range(len(distances)):
        if distances[i] <= a:
            total += 1

    print(total)

if __name__ == "__main__":

    n = int(input())

    for _ in range(n):
        g = []

        m, k, c = map(int, input().strip().split())

        for _ in range(k):
            g.append([])

        for _ in range(c):
            s, d = map(int, input().strip().split())
            g[s].append(d)
            g[d].append(s)

        bfs(g, m)
