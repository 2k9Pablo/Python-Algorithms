'''
Depth Firt Search
'''

def DFSUtil(g, visited, v):

    visited[v] = True
    for adj in g[v]:
        if not visited[adj]:
            DFSUtil(g, visited, adj)


def DFS(g):

    n = len(g)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            DFSUtil(g, visited, i)