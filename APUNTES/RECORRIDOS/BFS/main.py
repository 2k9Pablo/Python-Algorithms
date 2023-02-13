'''
Breath-First-Search
'''
from collections import deque

def BFSUtil(g, visited, v):

    q = deque()
    visited[v] = True
    q.append(v)

    while q:
        node = q.popleft()

        for adj in g[node]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True


def BFS(g):
    n = len(g)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            BFSUtil(g, visited, i)